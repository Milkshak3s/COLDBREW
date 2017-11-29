# COLDBREW
Python Flask-based command and control framework


## Usage
Run setup.py to clear out docs and create filesystem

Run server.py to start c2 server

Run control.py to stage commands for agents to grab


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