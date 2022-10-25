# Generate diff

[![Github Actions Status](https://github.com/stigsanek/python-project-50/workflows/python-ci/badge.svg)](https://github.com/stigsanek/python-project-50/actions)
[![Actions Status](https://github.com/stigsanek/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/stigsanek/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/308bfcb1ebd5980a7e7e/maintainability)](https://codeclimate.com/github/stigsanek/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/308bfcb1ebd5980a7e7e/test_coverage)](https://codeclimate.com/github/stigsanek/python-project-50/test_coverage)

Generate diff is a tool that determines the difference between two data structures.

Features:

* Support for different input formats: `yaml`, `json`.
* Report generation in the form of plain text, stylish and json

## Install

1. Install [poetry](https://python-poetry.org/).
2. Run `make install` or `poetry install` in the project directory.

## Usage

### From project

```
poetry run gendiff --format plain filepath1.json filepath2.yml

Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
```

### Wheel

You can build the wheel for later installation in a separate virtual environment with command `make build`
or `poetry build`. After installing the package in the virtual environment, the games can be launched using the
command:

```
gendiff filepath1.json filepath2.yml
```

## Example formats

### Plain

```
gendiff --format plain filepath1.json filepath2.yml

Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
```

### Stylish

```
gendiff --format stylish filepath1.json filepath2.yml

{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

### Json

```
gendiff --format json filepath1.json filepath2.yml

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
