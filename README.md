# Educational Game: Recursions

## Table of Contents
* [Setup](#Setup)
* [Running](#Running)
* [Linting](#Linting)

## Setup
Make sure you are using `Python 3.7.x`:

`python --version` or `python3 --version`

Install all required packages:
```bash
pip install -r requirements.txt
```

## Running
Run the program:
```
python src/game.py
```

## Linting
### Running Linting
Run linting on the entire project:
```bash
pylint src
```

Please resolve any issues and look for a rating of 10/10.
```
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

### Disabling Errors

If you believe a certain style should not apply to a certain file/function/line
you can disable them with a comment like the following:

```python
def print_list_twice(items):
    """Prints all elements in items twice"""
    for e in items: print(e) # pylint: disable=multiple-statements
    for e in items: print(e) # pylint: disable=multiple-statements
```

or

```python
def print_list_twice(items):
    """Prints all elements in items twice"""
    # pylint: disable=multiple-statements
    for e in items: print(e)
    for e in items: print(e)
```
