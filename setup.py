# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""setuptools install script"""

from pathlib import Path

from setuptools import find_packages
from setuptools import setup

MODULE_NAME = "bstrap"

INIT_FILE = "__init__.py"
VERSION_INDICATOR = "__version__"  # This sets the version in INIT_FILE

with open(
    (Path(MODULE_NAME) / INIT_FILE).expanduser().resolve(),
    "r",
) as f:  # Look in module's __init__ for __version__
    for line in f:
        if line.startswith(VERSION_INDICATOR):
            MODULE_VER = line.split("=", 1)[1].strip()[1:-1]
            break
    if not MODULE_VER:
        raise ValueError(
            f"{VERSION_INDICATOR} is not defined in {MODULE_NAME}/{INIT_FILE}",
        )

EXTRAS = {
    "test": [
        "black ~= 20.8b1",
        "coverage ~= 5.5",
        "flake8==3.9.0",
        "flake8-bugbear ~= 21.4.3",
        "flake8-commas ~= 2.0.0",
        "flake8-comprehensions ~= 3.4.0",
        "flake8-isort ~= 4.0.0",
        "flake8-print ~= 4.0.0",
        "flake8-quotes ~= 3.2.0",
        "isort ~= 5.8.0",
        "mypy==0.812",
        "pep8-naming ~= 0.11.1",
        "pylint ~= 2.7.4",
        "pytest ~= 6.2.3",
        "pytest-black ~= 0.3.12",
        "pytest-cov ~= 2.11.1",
        "pytest-dependency ~= 0.5.1",
        "pytest-flake8 ~= 1.0.7",
        "pytest-mypy ~= 0.8.1",
        "pytest-pylint ~= 0.18.0",
        "sphinx ~= 3.5.3",
    ],
}

setup(
    name=MODULE_NAME,
    version=MODULE_VER,
    url="REPLACEME",
    license="MPL 2.0",
    author="REPLACEME",
    author_email="REPLACEME",
    description="Bootstrap a project easily",
    # long_description=read("README.rst"),
    # entry_points={
    #     "console_scripts": [f"{MODULE_NAME} = {MODULE_NAME}.start:main"],
    # },
    packages=find_packages(exclude=("tests",)),
    package_data={
        MODULE_NAME: [
            "py.typed",
        ],
    },
    install_requires=[
        # "<dependency>",
    ],
    extras_require=EXTRAS,
    python_requires=">= 3.8",
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
)
