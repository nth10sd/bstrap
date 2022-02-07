"""Template generated from Briefcase 0.3.5, replace TempApp here with your desired name,
as well as in __main__.py, rename the whole directory and icon files, then update
pyproject.toml

Briefcase caches seem to be at:
* `.android`
* `.briefcase`
* `.cookiecutter_replay`
* `.gradle`
"""
import toga
from toga.style import Pack  # noqa: F401  # pylint: disable=unused-import
from toga.style.pack import COLUMN  # noqa: F401  # pylint: disable=unused-import
from toga.style.pack import ROW  # noqa: F401  # pylint: disable=unused-import


class TempApp(toga.App):  # type: ignore[misc]
    """Template App class."""

    def startup(self) -> None:
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main() -> TempApp:
    """Main function.

    :return: TempApp class
    """
    return TempApp()
