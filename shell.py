import os
import tarfile
import argparse
from datetime import datetime

class VirtualFileSystem:
    def __init__(self, tar_path):
        self.tar_path = tar_path
        self.tar = tarfile.open(tar_path, 'r')
        self.current_dir = '/.'
        self.file_tree = self.build_file_tree()


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

    def ls(self):
        dirs, files = self.vfs.list_dir(self.vfs.current_dir)
        output = dirs + files
        if output:
            print("\n".join(output))
        else:
            print("No files or directories found.")

    def cd(self, path):
        try:
            self.vfs.change_dir(path)
        except FileNotFoundError as e:
            print(e)

    def history_cmd(self):
        for idx, cmd in enumerate(self.history):
            print(f"{idx + 1}  {cmd}")

    def wc(self, filename):
        node = self.vfs.get_node(os.path.join(self.vfs.current_dir, filename))
        if node and not isinstance(node, dict):  # Ensure it's a file
            file_size = node.size
            print(f"{filename}: {file_size} bytes")
        else:
            print(f"wc: {filename}: No such file")




def main():
    parser = argparse.ArgumentParser(description="Shell Emulator")
    parser.add_argument('--user', required=True, help="Username for shell prompt")
    parser.add_argument('--vfs', required=True, help="Path to the virtual file system (tar archive)")

    args = parser.parse_args()

if __name__ == "__main__":
    main()
