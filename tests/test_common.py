# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Tests for common.py"""

from bstrap.common import LOSDevice


def test_losdevice() -> None:
    """Test the LOSDevice class."""
    device = LOSDevice("NewType")
    assert device.new_type == "NewType"
    assert device.compile() == "FOO"
