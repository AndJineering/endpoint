from directories import Directory
import os
import sys

def process_commands(commands):
    # Interprets and orchestrates the commands given to the program
    root = Directory("")

    for command in commands:
        print(command)
        parts = command.split()
        action = parts[0]

        if action == "CREATE":
            root.add(parts[1])
        elif action == "LIST":
            root.list()
        elif action == "MOVE":
            root.move(parts[1], parts[2])
        elif action == "DELETE":
            root.delete(parts[1])

    return root

def read_commands_from_file(filename):
    # Reads commands from a file and returns them as a list of strings
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return []

    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py {filename}")
        sys.exit(1)

    filename = sys.argv[1]
    commands = read_commands_from_file(filename)
    process_commands(commands)
