import os
import tarfile
import argparse
from datetime import datetime

class ShellEmulator:
    def __init__(self, username, vfs):
        self.username = username
        self.vfs = vfs
        self.history = []

    def run(self):
        while True:
            command_input = input(f"{self.username}@virtual:{self.vfs.current_dir}$ ")
            self.history.append(command_input)
            self.execute_command(command_input)

    def execute_command(self, command):
        parts = command.split()
        if not parts:
            return
        cmd = parts[0]

        if cmd == "ls":
            self.ls()
        elif cmd == "cd":
            if len(parts) > 1:
                self.cd(parts[1])
            else:
                print("cd: missing operand")
        elif cmd == "exit":
            print("Exiting shell.")
            exit(0)
        elif cmd == "history":
            self.history_cmd()
        elif cmd == "wc":
            self.wc(parts[1] if len(parts) > 1 else None)
        else:
            print(f"{cmd}: command not found")


def main():
    parser = argparse.ArgumentParser(description="Shell Emulator")
    parser.add_argument('--user', required=True, help="Username for shell prompt")
    parser.add_argument('--vfs', required=True, help="Path to the virtual file system (tar archive)")

    args = parser.parse_args()

if __name__ == "__main__":
    main()
