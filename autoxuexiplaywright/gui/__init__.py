"""Main module when runs in gui mode."""

from platform import system
from platform import release
from PySide6.QtCore import QTranslator
from PySide6.QtWidgets import QApplication
from autoxuexiplaywright.config import get_runtime_config
from autoxuexiplaywright.events import EventID
from autoxuexiplaywright.events import find_event_by_id
from autoxuexiplaywright.logger import info
from autoxuexiplaywright.defines import APPID
from autoxuexiplaywright.defines import APPVER
from autoxuexiplaywright.defines import APPNAME
from autoxuexiplaywright.defines import APPAUTHOR
from autoxuexiplaywright.defines import APPAUTHORDOMAIN
from autoxuexiplaywright.languages import get_language_string
from autoxuexiplaywright.gui.windows import MainWindow


SYSREL_WIN7 = 7


def _on_qr_updated(image: bytes):
    if image == "".encode():
        return
    info(get_language_string("ui-info-failed-to-print-qr"))


def lang_to_locale(lang: str) -> str:
    """Convert lang string to qt locale string.

    Like: zh-cn -> zh_CN

    Args:
        lang (str): The lang string

    Returns:
        str: The local string
    """
    parts = lang.split("-")
    extra = (
        "_"
        + "-".join(
            [parts[1].upper(), *parts[2:-1]],
        )
        if len(parts) > 1
        else ""
    )
    return parts[0] + extra


def register_callbacks():
    """Register required callbacks."""
    find_event_by_id(EventID.QR_UPDATED).add_callback(_on_qr_updated)


def start():
    """Main entrance of gui mode."""
    match system():
        case "Windows":
            try:
                rel = int(release())
            except ValueError:
                pass
            else:
                if rel >= SYSREL_WIN7:
                    # only windows 7 and higher needs this
                    import ctypes

                    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                        APPID,
                    )
        case "Linux":
            # Wayland needs this
            QApplication.setDesktopFileName(APPID)
        case _:
            pass
    QApplication.setApplicationName(APPNAME.lower())
    QApplication.setApplicationDisplayName(APPNAME)
    QApplication.setApplicationVersion(APPVER)
    QApplication.setOrganizationName(APPAUTHOR.lower())
    QApplication.setOrganizationDomain(APPAUTHORDOMAIN)
    app = QApplication()
    translator = QTranslator()
    translator.load("qt_" + lang_to_locale(get_runtime_config().lang))
    app.installTranslator(translator)
    main_window = MainWindow()
    main_window.show()
    app.exec()
