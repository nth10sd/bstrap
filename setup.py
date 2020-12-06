# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""setuptools install script"""

from setuptools import find_packages
from setuptools import setup

# def read(filename):
#     filename = os.path.join(os.path.dirname(__file__), filename)
#     text_type = type(u"")
#     with io.open(filename, mode="r", encoding="utf-8") as fd:
#         return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())

EXTRAS = {
    "test": [
        "coverage ~= 5.3",
        "flake8==3.8.4",
        "flake8-commas ~= 2.0.0",
        "flake8-isort ~= 4.0.0",
        "flake8-quotes ~= 3.2.0",
        "isort ~= 5.6.4",
        "mypy==0.790",
        "pycodestyle ~= 2.6.0",
        "pydocstyle ~= 5.1.1",
        "pylint ~= 2.6.0",
        "pytest ~= 6.1.2",
        "pytest-pycodestyle ~= 2.2.0",
        "pytest-pydocstyle ~= 2.2.0",
        "pytest-cov ~= 2.10.1",
        "pytest-flake8 ~= 1.0.6",
        "pytest-mypy ~= 0.8.0",
        "pytest-pylint ~= 0.18.0",
        "sphinx ~= 3.3.1",
    ]}

setup(
    name="bstrap",
    version="0.0.1",
    url="REPLACEME",
    license="MPL 2.0",

    author="REPLACEME",
    author_email="REPLACEME",

    description="Bootstrap a project easily",
    # long_description=read("README.rst"),

    # entry_points={
    #     "console_scripts": ["bstrap = bstrap.start:main"],
    # },
    packages=find_packages(exclude=("tests",)),
    package_data={"bstrap": [
        "py.typed",
    ]},

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
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
)
