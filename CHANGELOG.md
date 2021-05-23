# 1.1.0

* Bump to Python 3.9 as a minimum version for new projects
* Support more tools, such as pyupgrade and vulture for finding dead code
* Turn on code coverage integration via GitHub Actions
* Support Windows, Ubuntu Linux and macOS on GitHub Actions
* Dependency version bumps

# 1.0.1

* Add CHANGELOG.md
* Add Sphinx documentation generation
* Add notes for codecov submission

# 1.0.0

First version. To adapt this to something desirable:

* Remember to rename everything away from `bstrap`, including `.coveragerc` and the `bstrap/` folder.
* Update the `py38bootstrap` name, and update the README.md file.
* `devices/` folder demonstrates how inherited objects can be placed in a subfolder, while `util` folder demonstrates regular functions.
* `tests/` folder demonstrates an example `pytest` test structure.
