import hashlib
import json
import os
import pefile
def calculate_md5(file_path):
    """Berechnet den MD5-Hash einer Datei."""
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        # Dateiinhalte in Blöcken lesen, um den Speicherverbrauch zu minimieren
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()


def get_file_version(file_path):
    """Liest die Version einer EXE-Datei aus den Metadaten."""
    try:
        pe = pefile.PE(file_path)
        #print(pe.VS_FIXEDFILEINFO)
        file_info  = pe.VS_FIXEDFILEINFO[0]
        version = file_info.FileVersionLS
        # Zerlege die Version in Major.Minor.Build.Revision
        major = (version >> 16) & 0xffff
        minor = version & 0xffff
        
        version = file_info.FileVersionMS
        build = (version >> 16) & 0xffff
        revision = version & 0xffff
        
        # Rückgabe im gewünschten Format: Major.Minor.Build.Revision
        return f"{build}.{revision}.{major}.{minor}"
        return version_str
    except Exception as e:
        print(e)
        return None

def save_hash_to_json(file_path, output_dir):
    """Berechnet den MD5-Hash der Datei und speichert ihn als JSON-Datei."""
    hash = calculate_md5(file_path)
    version = get_file_version(file_path)
    # JSON-Daten erstellen
    data = {
        "file": os.path.basename(file_path),
        "version": version,
        "hash": hash,
        "type": "md5"
    }
    
    # Verzeichnis erstellen, falls es noch nicht existiert
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Pfad der JSON-Datei festlegen
    json_file_path = os.path.join(output_dir, "hash.json")
    
    # JSON-Datei speichern
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"MD5-Hash für {file_path} berechnet und in {json_file_path} gespeichert.")

file_path = r"C:\entwicklung\arkivadoCONNECTOR\dist\ArkivadoCONNECTOR.exe"
output_dir = r"C:\entwicklung\arkivadoCONNECTOR-docs\docs\static"  # Verzeichnis für JSON-Dateien

if os.path.isfile(file_path):
    save_hash_to_json(file_path, output_dir)

