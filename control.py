from os import walk


def get_host_info():
    hosts = [a, b]

    for (dirpath, dirname, filename) in walk("cmds"):
        filename = filename[:-4]
        hosts += [filename]

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
            print(host_num, ": ", host)
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

        cmd_file = open(host_list[host_num - 1] + ".txt")
        cmd_file.truncate()
        cmd_file.writelines(command)
        cmd_file.close()


if __name__ == "__main__":
    main()