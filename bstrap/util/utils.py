# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Place utility functions here."""

import logging

UTIL_RUN_LOG = logging.getLogger("util_run_log")


def add_one(inp: int) -> int:
    """Returns input added one.

    :param inp: Input number
    :return: Input added one
    """
    UTIL_RUN_LOG.info("Adding one...")
    return inp + 1
