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

def identify_attacker_ip():
    print("In progress")

def remove_malware_files(filename):
    try:
        for root, _, files in os.walk("C:\\"):
            if filename in files:
                file_path = os.path.join(root, filename)
                os.remove(file_path)
                print(f"'{filename}' removed successfully from: {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    malware = "Mal-Track"
    kill_malware_process("maltrack.exe")
    remove_startup_entry(malware)
    remove_malware_files(malware.lower() + ".exe")
    identify_attacker_ip()

if __name__ == "__main__":
    main()