from os import listdir
from os.path import isfile, join


def get_host_info():
    hosts = [f for f in listdir("cmds") if isfile(join("cmds", f))]

    return hosts


def main():
    escape = 0
    command = ''
    host_num = 1

    host_list = get_host_info()

    while escape == 0:
        print("Available Hosts:")
        print("-----------------")
        
        for host in host_list:
            print(host_num, ": ", host[:-4])
            host_num = host_num + 1
        
        print("")

        host_escape = 0
        while host_escape == 0:
            host_num = int(input("Host to command (0 for all): "))

            if host_num >= 0 and host_num <= len(host_list):
                host_escape = 1
            else:
                print("Error, invalid host")

        command = input("Command to send: ")

        if host_num == 0:
            for host in host_list:
                cmd_file = open("cmds/" + host_list[host_num], "w")
                cmd_file.truncate()
                cmd_file.writelines(command)
                cmd_file.close()
                host_num = host_num + 1
        else:
            cmd_file = open("cmds/" + host_list[host_num - 1], "w")
            cmd_file.truncate()
            cmd_file.writelines(command)
            cmd_file.close()
        
        escape = 1


if __name__ == "__main__":
    main()