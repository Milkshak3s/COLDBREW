# COLDBREW
Python Flask-based command and control framework


## Usage
setup.py to clear out docs and create filesystem

server.py to start c2 server

control.py to stage commands for agents to grab

cleanup.py to remove existing log and cmd files


## Connecting implants
Agents connect back to the server with the following format:
    Get commands:   [c2 domain]/conn/[hostname]/[username]
    Send Data:      [c2 domain]/out/[hostname]/[exfil data]

Note, server cannot handle data that would break URL


## Command format
[prefix]: [commands]

e.e.
bash: whoami


### setup.py
Removes garbage files and creates necessary directories and files


### server.py
Flask http server


### control.py
UI for staging commands to agents