# This project builds a CLI app to manage the todos.

## Setup environment

In this project, `Poetry` is used as Python dependency management and packaging tool.  
To install Poetry, follow the instruction [here](https://python-poetry.org/docs/#installation).

We have to prepare the python environment only once at the beginning:

```shell
bash dev/prepare.bash
```

Activate the virtual environment with the following command:

```shell
source dev/venv/bin/activate
```

## Show commands

```shell
python3 todocli.py --help
```

# Show usage of a command

```shell
python todocli.py <command> --help
```
