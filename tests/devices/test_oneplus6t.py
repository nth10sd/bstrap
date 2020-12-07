# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Tests for oneplus6t.py"""

from bstrap.devices.oneplus6t import OP6T


def test_op6t() -> None:
    """Test the OP6T class."""
    assert OP6T()
