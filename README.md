(Insert GitHub Actions/codecov status badges here)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# README

## Prerequisites
Create a new repository for your module on GitHub with no files.

Create a new Python 3.9 (install it beforehand) virtual environment using `venv` and switch to it.

```
python3.9 -u -m venv ~/venv-ls-py39 ;
```

```
source ~/venv-ls-py39/bin/activate && pip install --upgrade pip setuptools wheel ;
```

## Create a new module

Running in the above venv:

```
(venv-ls-py39) $ git clone git@github.com:nth10sd/bstrap.git

(venv-ls-py39) $ git clone REPLACEME
                           ^^^^^^^^^

(venv-ls-py39) $ cd REPLACEME
                    ^^^^^^^^^

(venv-ls-py39) $ cp -r ../bstrap/* ../bstrap/.gitignore ../bstrap/.vulture_allowlist ../bstrap/.github . && rm -rf *.egg-info/

(venv-ls-py39) $ mv bstrap/ REPLACEME
                            ^^^^^^^^^

(venv-ls-py39) $ find . ! \( -path ./.git -prune \) -type f | xargs sed -i 's/bstrap/REPLACEME/g'
                                                                                     ^^^^^^^^^
```

Install your module by running:

```
(venv-ls-py39) $ pip install --upgrade -r requirements.txt && pip install --upgrade -e .
```

Run your new module using:

```
(venv-ls-py39) $ python -u -m REPLACEME
                              ^^^^^^^^^
```
