import os


def main():
    os.remove("README.md")
    os.makedirs("logs")
    os.makedirs("cmds")

    cmd_file = open("command.txt", "a").close()


if __name__ == '__main__':
    main()