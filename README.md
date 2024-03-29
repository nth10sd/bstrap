(Insert GitHub Actions/codecov status badges here)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# README

## Prerequisites
Create a new repository for your module on GitHub with no files.

Create a new Python 3.10 (install it beforehand) virtual environment using `venv` and switch to it.

```
python3.10 -u -m venv ~/venv-ls-py310 ;
```

```
source ~/venv-ls-py310/bin/activate && pip install --upgrade pip setuptools wheel ;
```

## Create a new module

Running in the above venv:

```
(venv-ls-py310) $ git clone git@github.com:nth10sd/bstrap.git

(venv-ls-py310) $ git clone REPLACEME
                            ^^^^^^^^^

(venv-ls-py310) $ cd REPLACEME
                     ^^^^^^^^^

(venv-ls-py310) $ cp -r ../bstrap/* ../bstrap/.gitignore ../bstrap/.vulture_allowlist ../bstrap/.github . && rm -rf *.egg-info/

(venv-ls-py310) $ mv bstrap/ REPLACEME
                             ^^^^^^^^^

(venv-ls-py310) $ find . ! \( -path ./.git -prune \) -type f | xargs sed -i 's/bstrap/REPLACEME/g'
                                                                                      ^^^^^^^^^
```

Install your module by running:

```
(venv-ls-py310) $ pip install --upgrade -r requirements.txt && pip install --upgrade -e .
```

Run your new module using:

```
(venv-ls-py310) $ python -u -m REPLACEME
                               ^^^^^^^^^
```

## Run tools on your package

(All commands here must be run within the `venv`, in the main repository directory - not any subfolders)

For linters only:
```
for TOOL in flake8 mypy pylint ; do "$TOOL" tests/ $(python -c "import subprocess; out = subprocess.run([\"rg\", \"MODULE_NAME =\", \"setup.py\"], capture_output=True).stdout.decode(\"utf-8\"); print(out.split(\" = \\\"\", maxsplit=1)[-1].rstrip().removesuffix(\"\\\"\") + \"/\")") ; done;
```

For comprehensive tests and all linters:
```
pytest --bandit --black --cov --flake8 --mypy --pylint
```

For comprehensive tests and all linters **except** slow tests:
```
pytest --bandit --black --cov --flake8 --mypy --pylint -m "not slow"
```

## Documentation generation via Sphinx

* Change into `docs/` folder: `cd docs/`
* Run generation command - you **must** first be in the `docs/` directory: `./gen-sphinx-html.sh`
* Your generated HTML files are now in `docs/build/html/` directory
* Open `index.html` to start
