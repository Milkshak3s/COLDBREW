import os


def main():
    os.remove("READEME.md")
    os.makedirs("logs")

    cmd_file = open("command.txt")
    cmd_file.close()


if __name__ == '__main__':
    main()