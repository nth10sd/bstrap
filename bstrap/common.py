# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Define objects common to all devices."""


class LOSDeviceError(Exception):
    """Error class unique to LOSDevice objects."""


class LOSDevice:  # pylint: disable=too-few-public-methods
    """This object represents a device that supports Lineage OS."""

    def __init__(self) -> None:
        pass

    # @classmethod
    # def main(cls) -> None:
    #     """Main function of LOSDevice class.
    #     """

    # @staticmethod
    # def compile() -> None:
    #     """Build a shell
    #     """
