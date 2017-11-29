import os
from os import listdir
from os.path import isfile, join

def get_host_info():
    hosts = [f for f in listdir("cmds") if isfile(join("cmds", f))]

    return hosts


def main():
    host_list = get_host_info()

    for host in host_list:
        os.remove('logs/' + host)
        os.remove('cmds/' + host)


if __name__ == "__main__":
    main()