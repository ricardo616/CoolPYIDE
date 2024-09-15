import os
import sys

# Funções de Comando

def log(message=""):
    """Prints a message to the console."""
    print(message)

def echo(message=""):
    """Repeats the provided message."""
    print(message)

def clear():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def help():
    """Displays this help message."""
    print("Available commands:")
    print(" log <message>  - Prints a message to the console.")
    print(" echo <message> - Repeats the provided message.")
    print(" clear          - Clears the console screen.")
    print(" help           - Displays this help message.")
    print(" exit           - Exits the command line interface.")
    print(" list           - Lists all files and directories in the current directory.")
    print(" cd <dir>       - Changes the current directory to the specified directory.")
    print(" pwd            - Prints the current working directory.")
    print(" mkdir <dir>    - Creates a new directory.")
    print(" rmdir <dir>    - Removes an existing directory.")
    print(" touch <file>   - Creates a new file.")
    print(" rm <file>      - Deletes a file.")
    print(" cat <file>     - Displays the contents of a file.")

def exit_cli():
    """Exits the CLI."""
    print("Exiting...")
    sys.exit(0)

def list_files(_):
    """Lists all files and directories in the current directory."""
    for item in os.listdir('.'):
        print(item)

def change_directory(path):
    """Changes the current directory."""
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")
    except NotADirectoryError:
        print(f"'{path}' is not a directory.")

def print_working_directory(_):
    """Prints the current working directory."""
    print(os.getcwd())

def make_directory(directory):
    """Creates a new directory."""
    try:
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    except FileExistsError:
        print(f"Directory '{directory}' already exists.")

def remove_directory(directory):
    """Removes an existing directory."""
    try:
        os.rmdir(directory)
        print(f"Directory '{directory}' removed.")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except OSError:
        print(f"Directory '{directory}' is not empty or could not be removed.")

def create_file(file):
    """Creates a new file."""
    with open(file, 'w') as f:
        pass
    print(f"File '{file}' created.")

def remove_file(file):
    """Deletes a file."""
    try:
        os.remove(file)
        print(f"File '{file}' removed.")
    except FileNotFoundError:
        print(f"File '{file}' not found.")

def display_file(file):
    """Displays the contents of a file."""
    try:
        with open(file, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File '{file}' not found.")
    except IOError:
        print(f"Could not read file '{file}'.")

# Mapear comandos para funções
COMMANDS = {
    'log': log,
    'echo': echo,
    'clear': clear,
    'help': help,
    'exit': exit_cli,
    'list': list_files,
    'cd': change_directory,
    'pwd': print_working_directory,
    'mkdir': make_directory,
    'rmdir': remove_directory,
    'touch': create_file,
    'rm': remove_file,
    'cat': display_file
}

def execute_command(command):
    """Executes a given command."""
    parts = command.split(maxsplit=1)
    cmd = parts[0]
    args = parts[1] if len(parts) > 1 else ""
    if cmd in COMMANDS:
        # Funções que não aceitam argumentos adicionais
        if cmd in ['clear', 'help', 'exit']:
            COMMANDS[cmd]()
        else:
            # Funções que aceitam um argumento
            COMMANDS[cmd](args)
    else:
        print(f"Unknown command: {cmd}")

def main():
    """Main CLI function."""
    print("CoolPy Command Line Interface (CLI) - Type 'help' for available commands.")
    while True:
        try:
            command = input("CoolPy> ").strip()
            if command:
                execute_command(command)
        except KeyboardInterrupt:
            print("\nExiting due to keyboard interrupt.")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
