![pytest](https://REPLACEME)

# README

## Prerequisites
Create a new repository for your module on GitHub with no files.

Create a new Python virtual environment using `venv` and switch to it.

```
$ python3 -u -m venv venv-new && source venv-new/bin/activate && pip install --upgrade pip setuptools wheel
```

## Create a new module

Running in the above venv:

```
(venv-new) $ git clone git@github.com:nth10sd/bstrap.git

(venv-new) $ git clone <link to new empty repo>

(venv-new) $ cd <new repo>

(venv-new) $ cp -r ../bstrap/* ../bstrap/.gitignore .

(venv-new) $ mv bstrap/ <new module name>

(venv-new) $ find . ! \( -path ./.git -prune \) -type f | xargs sed -i 's/bstrap/<new module name>/g'
```

Install your module by running:

```
(venv-new) $ pip install --upgrade -r requirements.txt -e .
```

Run your new module using:

```
(venv-new) $ python3 -u -m <new module name>
```
