# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Define objects common to all devices."""

from __future__ import annotations

# class LOSDeviceError(Exception):
#     """Error class unique to LOSDevice objects."""


class LOSDevice:
    """This object represents a device that supports Lineage OS.

    :param new_type: This is a new type for LOSDevice
    """

    def __init__(self, new_type: str):
        self.new_type = new_type

    @classmethod
    def main(cls) -> None:
        """Main function of LOSDevice class."""

    @staticmethod
    def compile() -> str:
        """Build a shell

        :return: A testing string
        """
        return "FOO"
