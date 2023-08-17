# 1.1.0 (2021-05-22)

1. Bump to Python 3.9 as a minimum version for new projects
1. Support more tools, such as pyupgrade and vulture for finding dead code
1. Turn on code coverage integration via GitHub Actions
1. Support Windows, Ubuntu Linux and macOS on GitHub Actions
1. Dependency version bumps

# 1.0.1 (2020-08-31)

1. Add CHANGELOG.md
1. Add Sphinx documentation generation
1. Add notes for codecov submission

# 1.0.0 (2020-08-13)

First version. To adapt this to something desirable:

1. Remember to rename everything away from `bstrap`, including `.coveragerc` and the `bstrap/` folder.
1. Update the `py38bootstrap` name, and update the README.md file.
1. `devices/` folder demonstrates how inherited objects can be placed in a subfolder, while `util` folder demonstrates regular functions.
1. `tests/` folder demonstrates an example `pytest` test structure.
