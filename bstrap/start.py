# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""start.py"""

import logging

from bstrap.common import LOSDevice
from bstrap.util.utils import add_one

RUN_LOG = logging.getLogger("run_log")
logging.basicConfig(
    format="%(asctime)s %(name)-8s %(levelname)-8s {%(module)s} [%(funcName)s] %(message)s",
    datefmt="%m-%d %H:%M:%S", level=logging.INFO,
)
logging.getLogger("filelock").setLevel(logging.WARNING)


def main() -> None:
    """main function"""
    LOSDevice("NewType")
    RUN_LOG.warning(add_one(2))
    RUN_LOG.error("foo")
