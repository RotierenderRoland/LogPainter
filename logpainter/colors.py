BLUE = '\033[34m'
CYAN = '\033[36m'
GREEN = '\033[32m'
RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[0m'


def blue(text: str) -> str:
    return f'{BLUE}{text}{RESET}'


def cyan(text: str) -> str:
    return f'{CYAN}{text}{RESET}'


def green(text: str) -> str:
    return f'{GREEN}{text}{RESET}'


def red(text: str) -> str:
    return f'{RED}{text}{RESET}'


def yellow(text: str) -> str:
    return f'{YELLOW}{text}{RESET}'


color_map = {
    "red": red,
    "yellow": yellow,
    "green": green,
    "blue": blue,
    "cyan": cyan
}
