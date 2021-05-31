(Insert GitHub Actions/codecov status badges here)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# README

## Prerequisites
Create a new repository for your module on GitHub with no files.

Create a new Python 3.9 (install it beforehand) virtual environment using `venv` and switch to it.

```
$ python3.9 -u -m venv venv-new && source venv-new/bin/activate && pip install --upgrade pip setuptools wheel
```

## Create a new module

Running in the above venv:

```
(venv-new) $ git clone git@github.com:nth10sd/bstrap.git

(venv-new) $ git clone REPLACEME
                       ^^^^^^^^^

(venv-new) $ cd REPLACEME
                ^^^^^^^^^

(venv-new) $ cp -r ../bstrap/* ../bstrap/.gitignore ../bstrap/.coveragerc ../bstrap/.pylintrc .

(venv-new) $ mv bstrap/ REPLACEME
                        ^^^^^^^^^

(venv-new) $ find . ! \( -path ./.git -prune \) -type f | xargs sed -i 's/bstrap/REPLACEME/g'
                                                                                 ^^^^^^^^^
```

Install your module by running:

```
(venv-new) $ pip install --upgrade -r requirements.txt -e .
```

Run your new module using:

```
(venv-new) $ python -u -m REPLACEME
                           ^^^^^^^^^
```
