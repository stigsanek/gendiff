# Generate diff

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/stigsanek/gendiff/pyci.yml?branch=main)
![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/stigsanek/gendiff)
![Code Climate coverage](https://img.shields.io/codeclimate/coverage/stigsanek/gendiff)

## Description

"Generate diff" is a tool that determines the difference between two data structures.

Features:

* Support for different input formats: `yaml`, `json`.
* Report generation in the form of plain text, stylish and json

## Install

### Python

Before installing the package, you need to make sure that you have Python version 3.8 or higher installed.

```bash
>> python --version
Python 3.8.0+
```

If you don't have Python installed, you can download and install it
from [the official Python website](https://www.python.org/downloads/).

### Poetry

The project uses the Poetry manager. Poetry is a tool for dependency management and packaging in Python. It allows you
to declare the libraries your project depends on and it will manage (install/update) them for you. You can read more
about this tool on [the official Poetry website](https://python-poetry.org/)

### Package

To work with the package, you need to clone the repository to your computer. This is done using the `git clone` command.
Clone the project on the command line:

```bash
# clone via HTTPS:
>> git clone https://github.com/stigsanek/gendiff.git
# clone via SSH:
>> git@github.com:stigsanek/gendiff.git
```

It remains to move to the directory and install the package:

```bash
>> cd gendiff
>> poetry build
>> python -m pip install --user dist/*.whl
```

Finally, we can move on to using the project functionality!

## Usage

### Plain format

```bash
>> gendiff --format plain filepath1.json filepath2.yml

Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
```

### Stylish format

```bash
>> gendiff --format stylish filepath1.json filepath2.yml

{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

### Json format

```bash
>> gendiff --format json filepath1.json filepath2.yml

{
    "follow": [
        "D",
        false
    ],
    "host": [
        "U",
        "hexlet.io"
    ],
    "proxy": [
        "D",
        "123.234.53.22"
    ],
    "timeout": [
        "C",
        50,
        20
    ],
    "verbose": [
        "A",
        true
    ]
}
```

## Development

### Useful commands

* `make install` - install all dependencies in the environment.
* `make build` - build the wheel.
* `make lint` - checking code with linter.
* `make test` - run tests.
