import re
import subprocess
import winreg
import os

def kill_malware_process(filename):
    subprocess.run(["taskkill", "/IM", filename, "/F"])

def remove_startup_entry(malware):
    startup_key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, startup_key_path, 0, winreg.KEY_WRITE) as startup_key:
            try:
                winreg.DeleteValue(startup_key, malware)
                print(f"'{malware}' startup entry removed successfully.")
            except FileNotFoundError:
                print(f"'{malware}' startup entry not found.")
    except Exception as e:
        print(f"Error: {e}")

def identify_attacker_ip(filename):
    filepath = file_location(filename)
    try:
        with open(filepath, "rb") as f:
            strings = re.findall(b"([\x20-\x7E]{4,})", f.read())
            for s in strings:
                decoded_string =  s.decode("utf-8")
                match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", decoded_string)
                if match:
                    print(f"potential attacker IP:{match.group()}")
    except OSError as e:
        print(e)

def file_location(filename):
    try:
        for root, _, files in os.walk("C:\\"):
            if filename in files:
                return os.path.join(root, filename)
    except Exception as e:
        print(f"Error: {e}")

def remove_malware_files(filename):
    file_path = file_location(filename)
    os.remove(file_path)
    print(f"'{filename}' removed successfully from: {file_path}")

def main():
    kill_malware_process("maltrack.exe")
    remove_startup_entry("Mal-Track")
    identify_attacker_ip("mal-track.exe")
    remove_malware_files("maltrack.exe")
    remove_malware_files("mal-track.exe")

if __name__ == "__main__":
    main()