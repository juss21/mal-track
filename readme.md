# Mal-track
The goal of this project is to understand the basic operation of a computer virus on a Windows environment and simple methods to eradicate them.

### Requirements
- Python3
- Windows OS

### How to run 
- Install python to your Windows machine.
- Open cmd
- Go to file directory and type `python mal_remove.py`
## Audit

### [Audit questions](https://github.com/01-edu/public/tree/master/subjects/cybersecurity/mal-track/audit)
### [Video](https://youtu.be/qguXiBgSV0w)

- Is the student able to explain clearly how we can manage the startup programs in windows?
    - To manage Windows startup programs, open Settings > Apps > Startup.

- Is the student able to explain clearly how he get the ip of the attacker from the malware?
    - I open the file, decoding the content and then use regex to filter out all IP addresses used in the program.

- Is the student able to explain clearly how his program works?
    - Sure, It kills the malwares process > removes it from startup > finds IP addresses > searches for and deletes the malware files.

##
### Author: [Juss](https://01.kood.tech/git/juss)