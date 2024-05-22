
# AirBnB Clone - The Console

## Project Description

This project is the first step towards building a full web application similar to AirBnB. In this part of the project, we focus on creating a command interpreter that allows us to manage various AirBnB objects such as users, places, states, cities, and more.

The console is a command-line interface (CLI) that enables users to create, update, delete, and retrieve objects stored in a JSON file.

## Command Interpreter

The command interpreter is built using Python's `cmd` module and provides several commands to interact with the application's objects.

### How to Start the Command Interpreter

To start the command interpreter, run the following command from the root directory of the project:

```bash
./console.py
```

You should see a prompt like this:

```bash
(hbnb)
```

### How to Use the Command Interpreter

Below are the commands you can use in the interpreter:

- `create <ClassName>`: Creates a new instance of the specified class.
- `show <ClassName> <id>`: Shows the details of an instance based on its class and id.
- `destroy <ClassName> <id>`: Deletes an instance based on its class and id.
- `all [ClassName]`: Shows all instances of the specified class, or all instances if no class is specified.
- `update <ClassName> <id> <attribute name> "<attribute value>"`: Updates the attribute of an instance based on its class and id.
- `quit`: Exits the command interpreter.
- `EOF`: Exits the command interpreter.

### Examples

Here are some examples of how to use the command interpreter:

```bash
(hbnb) create User
(hbnb) show User 1234-5678-9012
(hbnb) destroy User 1234-5678-9012
(hbnb) all User
(hbnb) update User 1234-5678-9012 name "John Doe"
(hbnb) quit
```

## Project Structure

The project follows this structure:

```
AirBnB_clone/
├── console.py
├── models/
│   ├── base_model.py
│   ├── user.py
│   └── engine/
│       └── file_storage.py
├── tests/
│   ├── test_models/
│   │   ├── test_base_model.py
│   │   └── test_user.py
│   └── test_engine/
│       └── test_file_storage.py
├── README.md
└── AUTHORS
```

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AirBnB_clone.git
   cd AirBnB_clone
   ```

2. Make the console executable:
   ```bash
   chmod +x console.py
   ```

3. Run the console:
   ```bash
   ./console.py
   ```

## Authors

See the `AUTHORS` file for a list of contributors.
