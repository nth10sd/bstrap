# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Place utility functions here."""

import logging

RUN_LOG = logging.getLogger("run_log")
logging.basicConfig(
    format="%(asctime)s %(name)-8s %(levelname)-8s {%(module)s} [%(funcName)s] %(message)s",
    datefmt="%m-%d %H:%M:%S", level=logging.INFO,
)
logging.getLogger("flake8").setLevel(logging.ERROR)


def add_one(inp: int) -> int:
    """Returns input added one.

    :param inp: Input number
    :return: Input added one
    """
    return inp + 1
