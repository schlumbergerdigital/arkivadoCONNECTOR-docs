"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
'  Python Skript -  Verbindet sich via SSH mit einem Server und schickt befehle 

' 				
'  
' Benötigt: paramiko und die Pfade zu den Keyfiles 
'				   			  
'					   
' Zur Verwendung mit: zb. meister_docarchiv, oder andere
' 
' Erstellt von:	Max Schwesig	  
' Version:	1.12
' Codierung:	UTF-8
' Stand:	04.05.2023 Max Schwesig		
' 
' Copyright (c) 2023 by schlumberger digital. Alle Rechte vorbehalten.
' www.schlumberger.digital
'\*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

import paramiko
import socket
import os
import sys  
import json 
import tkinter as tk
from tkinter import simpledialog
import datetime
from test_dns import dns_resolver
import time 



class its_ssh():
    def __init__(self,kundenname=None,username = "root",server_ip=None,keyfile_passwort=None,password=None,DIR_PATH=None,max_rety=5,kundenKeyPaths=None,top_domain= "docarchiv.de",quit_on_error=True):
        backslash = "\\"
        if kundenKeyPaths is None:
            if top_domain == "docarchiv.de":
                kundenKeyPaths = r"D:\Zertifikate\Hetzner.cloud\Kunden"
            else:
                
                kundenKeyPaths = f"""D:{backslash}Zertifikate{backslash}Hetzner.cloud{backslash}{top_domain}{backslash}Kunden"""
        if DIR_PATH is None:
            self.DIR_PATH =  os.path.dirname(os.path.realpath(__file__))
        else:
            self.DIR_PATH = DIR_PATH

        application_window = tk.Tk()
        application_window.withdraw()
        self.max_rety = max_rety
        self.kundenname = kundenname
        self.top_domain = top_domain
        self.kundenKeyPaths = kundenKeyPaths
        self.username = username
        self.password = password
        self.keyfile_passwort = keyfile_passwort
        self.keyfile = None
        self.hostname =  str(str(self.kundenname)+'.'+str(self.top_domain))
        if server_ip is None:
            try:
                self.server_ip = self._get_ip_from_name(self.hostname)
            except:
                print("Konnte",str(self.hostname),"nicht in IP umrechnen")
        else:
            self.server_ip = server_ip
        self.connversuch = 1
        self.client = None 
        self.client = self.connect()
        self.command_max_retry = 3
        self.sleep_time_between_command = 0.00
        self.quit_on_error = quit_on_error
        self.false_errors = [
                {
                "command":"htpasswd -b -B",
                "text": ["Updating password", "Adding password for user"],
                "search_text_at_start": True 
                },
                {
                "command":"curl https://rclone.org/install.sh | sudo bash",
                "text": ["The latest version of reclone"],
                "search_text_at_start": True 
                }

        ]
        


    def _get_ip_from_name(self,name):
        ip_list =  dns_resolver(name)
        if len(ip_list) > 0:
            return ip_list[0]
        else:
            return None

    def _get_key_path(self,name= None):
        if not name:
            name = self.kundenname
        kundenKeyPaths = self.kundenKeyPaths
        paths ={}
        paths["ecodmsscanner_public"] = f"{kundenKeyPaths}\{name}\{name}_scanner.public"
        paths["ecodmsftpbackup_public"] = f"{kundenKeyPaths}\{name}\{name}_backup.public"
        paths["admin_public"] = f"{kundenKeyPaths}\{name}\{name}_admin.public"
        paths["ecodmsscanner_private"] = f"{kundenKeyPaths}\{name}\{name}_scanner_openssh.ppk"
        paths["ecodmsftpbackup_private"] = f"{kundenKeyPaths}\{name}\{name}_backup_openssh.ppk"
        paths["admin_private"] = f"{kundenKeyPaths}\{name}\{name}_admin_openssh.ppk"
        self.paths = paths
        return paths 

    def _get_key_from_keyfile(self,keyfile, keyfile_passwort=None):
        print(datetime.datetime.now(),"lese keyfile: ",keyfile)
        if keyfile_passwort:
            print(datetime.datetime.now(),"Öffne Keyfile mit pasephrase")
            k = paramiko.RSAKey.from_private_key_file(keyfile,password=keyfile_passwort)
        else:
            k = paramiko.RSAKey.from_private_key_file(keyfile)
        return k


    def send_exec(self,command):

        _, stdout, stderr = self.client.exec_command(command)
   
        time.sleep(self.sleep_time_between_command)
        return stdout,stderr

    def test_error(self,command,err):
        is_error = True 
        command = command.lower().strip()
        err = err.lower().strip()
        for false_error in self.false_errors:
            if command.startswith(false_error['command'].lower().strip()):
                for text in false_error['text']:
                    if false_error["search_text_at_start"]:
                        if err.startswith(text.lower().strip()):
                            is_error = False
                    elif  false_error["search_text_at_start"] is False:
                        if err.endswith(text.lower().strip()):
                            is_error = False
        return is_error
                        




    def exec(self,commands,client=None,auto_retry=False):
        errcount = 0 

        for command in commands:
            retry = 0
            have_to_send = True
            is_error = False 
            while have_to_send:
                retry += 1
                print("tryNr.",retry,"send:")
                print(command)
                stdout, stderr = self.send_exec(command)
                try:
                    print("got:")
                    print(str(stdout.read().decode()))
                    err = str(stderr.read().decode())
                except:
                    print("SSH: Fehler, Ausgabe konnte nicht gelesen werden. Muss KEIN Linux Fehler sein...")
                if err:
                    try:
                        is_error = self.test_error(command,err)
                    except:
                        is_error = False

                if (retry > self.max_rety) and is_error:
                    have_to_send = False
                    errcount += 1
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("FEHLER KONNTE NICHT BEHOBEN WERDEN! ÜBERSPRINNGE:")
                    print(command)
                    print("Fehlermeldung:")
                    print(err)
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


                elif is_error:
                    print("FHELER:")
                    print(err)
                    if auto_retry is False:
                        have_to_send = False     
                else:
                    have_to_send = False 
                
        if errcount > 0:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("    ")
            print("    ")
            print("    ")
            print( '''    .-""""""-. ''')
            print( '''  .'  \\  //  '. ''')
            print( ''' /   O      O   \ ''')
            print( ''':                : ''')
            print( '''|                |   ''')
            print( ''':       __       : ''')
            print( ''' \  .-"`  `"-.  / ''')
            print( '''  '.          .' ''')
            print( '''    '-......-' ''') 
            print("FEHLER BEIM BEFEHL AUSFÜHREN!!!!!")
            print("    ")
            print("Es wurden ",errcount,"Fehler gezählt!" )
            print("(ಠ_ಠ)")
            print("    ")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
 

    def connect(self,name=None,server_ip = None, keyfile_passwort = None,quit_on_error=True):
        if not keyfile_passwort:
            application_window = tk.Tk()
            application_window.withdraw()
            if not keyfile_passwort:
                keyfile_passwort = self.keyfile_passwort
            if not keyfile_passwort:
                try:
                    filepath = os.path.join(self.kundenKeyPaths,self.kundenname,f"admin_{self.hostname}_pw.json")
                    with open(filepath,'r') as f:
                        config_dict = json.load(f)
                        keyfile_passwort = config_dict['root']
                except Exception as e:
                    print("konnte Konfig json unter",filepath)
                    keyfile_passwort = None


            if not keyfile_passwort:
                keyfile_passwort = simpledialog.askstring("Input", f"Passphrase für KeyFile für {self.hostname} / {self.server_ip} / {self.username}")
            if name is None:
                name = self.kundenname
                if not self.hostname.startswith(self.kundenname):
                    self.hostname = f"{self.kundenname}.{self.top_domain}"
        paths = self._get_key_path(name)
        pkey = self._get_key_from_keyfile(paths["admin_private"],keyfile_passwort)
        if server_ip:
            connect_to = server_ip
        elif self.server_ip:
            connect_to = self.server_ip
        else:
            connect_to =self.hostname
        if self.client is None and self.connversuch < 4:
            print("Verbindungsversuch",self.connversuch,f" - {connect_to} / {self.username}")
        retry = True 
        while retry:
                self.connversuch += 1
                client = self._connect(connect_to,self.username,password=self.password,pkey=pkey)
                if client:
                    retry = False 
                elif self.connversuch > self.max_rety:
                    retry = False
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("BRECHE SSH VERBINDUNG AB! SSH Befehle an ", self.hostname, "können nicht geschickt werden.")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    
                    if quit_on_error:
                        #input("Progamm beendet. Drücke eine belibige Taste um dieses Fenster schließen")
                        raise ConnectionError(f"Verbindung zu  {connect_to} mit {self.username} gescheitert.")
                    
                else:
                    print("Warte 20 Sekunden und versuche es nochmal")
                    time.sleep(20)

        return client 

    def _connect(self,hostname,username,password=None,pkey=None):
        # initialize the SSH client
        client = paramiko.SSHClient()
        # add to known hosts
        hostname = str(hostname).strip()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("Verbinde mit:",hostname)
        try:
            if pkey:
                client.connect(hostname=hostname, username=username, password=password, pkey = pkey )
            else:
                client.connect(hostname=hostname, username=username, password=password )
            print("Verbunden mit ",hostname)
        except Exception as err:
            print("[!] Cannot connect to the SSH Server:",hostname)
            print(err)
            self.connversuch += 1
            return None
        return client

    def test_domain(self):
        name = self.hostname
       
        ip_list =  dns_resolver(name)
        if len(ip_list) > 0 :
            print(datetime.datetime.now(),"Der Name ", name, " ist belegt")
            belegt = True
        else:
            print(datetime.datetime.now()," Der Name ", name, " ist noch frei.")
            belegt = False
        return belegt