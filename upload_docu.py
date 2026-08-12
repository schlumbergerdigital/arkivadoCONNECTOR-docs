
import json
import os 
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog
from ssh_connect import its_ssh


class upload_docu():

    def __init__(self,kundenname=None,username = "root",top_domain = "docarchiv.de",keyfile_passwort=None,
                 password=None,DIR_PATH=None,server_ip = None,
                 exclude:list|None=None
                ,delete_old_nginx_config:bool = False ):
        if DIR_PATH is None:
            self.DIR_PATH =  os.path.dirname(os.path.realpath(__file__))
        else:
            self.DIR_PATH = DIR_PATH
        application_window = tk.Tk()
        application_window.withdraw()
        self.top_domain = top_domain
        self.kundenKeyPaths = r"D:\Zertifikate\Hetzner.cloud\Kunden"
        self.username = username
        self.password = password
        self.keyfile_passwort = keyfile_passwort
        self.keyfile = None
        if not kundenname:
            kundenname = simpledialog.askstring("Input", "Name des Kunden (xxxx."+self.top_domain+")")
        self.hostname = str(kundenname) +"."+self.top_domain
        self.kundenname = kundenname
        if exclude is None:
            exclude = []
        self.exclude = exclude
       
        self.ssh = its_ssh(kundenname=self.kundenname,username=username,server_ip=server_ip,keyfile_passwort=keyfile_passwort,password=password,DIR_PATH=self.DIR_PATH,top_domain=top_domain)
        self.sftp = None
        if self.ssh:
            self.upload_docu()      
        else:
            print(datetime.now(),"Domain",self.hostname,"nicht gefunden breche ab!")


    def upload(self,source,destination,make_executable=False):
        if self.sftp is None:
            self.sftp = self.ssh.client.open_sftp()
        print(datetime.now(),"sftp put:",source,destination)
        self.sftp.put(source,destination)
        if make_executable:
            command = [f"""chmod +x '{destination}'""",]
            self.ssh.exec(command)

    def upload_dir(self,source,destination):
        print("beginne mit:",source,destination)
        if self.sftp is None :
            self.sftp = self.ssh.client.open_sftp()

        for item in os.listdir(source):
            dest = f"""{destination}/{item}"""
            sour = os.path.join(source, item)
            if os.path.isfile(sour):
                print(datetime.now(),"Lade Datei hoch:",dest)
                self.sftp.put(sour, dest)
            else:
                print(datetime.now(),"Erstelle Vezeichnis:",dest)
                try:
                    self.sftp.mkdir(dest)
                except IOError as e:
                    print("Fehler beim erstellen:",sour,"-",dest,e,"überspringe das anlegen")
                print("untersuche subpfad",sour)
                self.upload_dir(sour, dest)

    def upload_docu(self,source_folder="site",dest_folder ="/var/www/docs"):
        source_folder =os.path.join(self.DIR_PATH,source_folder)
        print("Altes Verzeichnis entfernen")
        command = [f"rm -R '{dest_folder}'",
                   f"""mkdir -p '{dest_folder}'"""
                   ]
        self.ssh.exec(command )
        print("Neuen Content hochladen")
        self.upload_dir(source_folder,dest_folder)
        command = [
            f"sudo chown -R www-data:www-data '{dest_folder}'",
            f"sudo chmod -R 755 '{dest_folder}'"
        ]
        print("Berechtigung anpassen")
        self.ssh.exec(command )

    #def upload_nginx_redirects(self,source_file=os.path.join("nginx","docs-legacy-redirects.conf"),
    #                           snippet_path="/etc/nginx/snippets/docs-legacy-redirects.conf"):
    #    source = os.path.join(self.DIR_PATH,source_file)
    #    if not os.path.isfile(source):
    #        print(datetime.now(),"Redirect-Snippet nicht gefunden, ueberspringe:",source)
    #        return
    #    print("Legacy-Weiterleitungen ausrollen")
    #    self.ssh.exec(["mkdir -p /etc/nginx/snippets"])
    #    self.upload(source,snippet_path)
#
    #    snippet_name = os.path.basename(snippet_path)
    #    # include idempotent hinter die erste server_name-Zeile des Doku-vhosts setzen,
    #    # bei fehlgeschlagenem "nginx -t" wird das Backup zurueckgespielt
    #    include_cmd = (
    #        'bash -c \'set -u; '
    #        f'vhost=$(grep -rls "server_name.*{self.hostname}" /etc/nginx/conf.d/ | head -n1); '
    #        'if [ -z "$vhost" ]; then echo "KEIN VHOST GEFUNDEN - include bitte manuell setzen"; exit 0; fi; '
    #        f'if grep -q "{snippet_name}" "$vhost"; then echo "include bereits vorhanden in $vhost"; exit 0; fi; '
    #        'cp "$vhost" "$vhost.bak"; '
    #        'sed -i "0,/server_name/s|\\(server_name[^;]*;\\)|\\1\\n    include snippets/'
    #        f'{snippet_name};|" "$vhost"; '
    #        'nginx -t || { cp "$vhost.bak" "$vhost"; echo "NGINX-TEST FEHLGESCHLAGEN - vhost wiederhergestellt"; exit 1; }; '
    #        'echo "include ergaenzt in $vhost"\''
    #    )
    #    self.ssh.exec([include_cmd])
    #    self.ssh.exec(["nginx -t && systemctl reload nginx"])


uploader = upload_docu(kundenname="docs",top_domain="arkivado.digital")