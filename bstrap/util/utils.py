# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Place utility functions here."""

from __future__ import annotations

from logging import INFO as INFO_LOG_LEVEL

from bstrap.util.logging import get_logger

UTIL_RUN_LOG = get_logger(__name__, fmt="%(message)s")
UTIL_RUN_LOG.setLevel(INFO_LOG_LEVEL)


def add_one(inp: int) -> int:
    """Returns input added one.

    :param inp: Input number
    :return: Input added one
    """
    UTIL_RUN_LOG.info("Adding one...")
    return inp + 1
