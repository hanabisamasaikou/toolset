from settings import *


def check(content: str) -> str:
    for key, value in types.items():
        if value in content:
            return key
    return ""


def error(content: str) -> None:
    print(f"\nERROR {content}\n")


def hint() -> None:
    print("\nPlease enter the url (enter quit to exit)\n")


def info(content: str) -> None:
    print(f"\nINFO {content}\n")


def logo() -> None:
    print(
        "  _   _      _      _   _      _      ____    ___     ____       _      __  __      _     "
    )
    print(
        " | | | |    / \    | \ | |    / \    | __ )  |_ _|   / ___|     / \    |  \/  |    / \    "
    )
    print(
        " | |_| |   / _ \   |  \| |   / _ \   |  _ \   | |    \___ \    / _ \   | |\/| |   / _ \   "
    )
    print(
        " |  _  |  / ___ \  | |\  |  / ___ \  | |_) |  | |     ___) |  / ___ \  | |  | |  / ___ \  "
    )
    print(
        " |_| |_| /_/   \_\ |_| \_| /_/   \_\ |____/  |___|   |____/  /_/   \_\ |_|  |_| /_/   \_\ "
    )
