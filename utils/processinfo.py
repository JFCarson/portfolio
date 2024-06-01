from termcolor import colored


def info(response):
    return print(f'[{colored("INFO", "blue")}] {response}')


def warn(response):
    return print(f'[{colored("WARN", "yellow")}] {response}')


def error(response):
    return print(f'[{colored("ERROR", "red")}] {response}')
