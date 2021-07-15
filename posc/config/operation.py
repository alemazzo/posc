
import os
import subprocess
from threading import Thread


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class STATUS:
    PROGRESS = '[.]'
    OK = f'[{colors.OKGREEN}\u2714{colors.ENDC}]'
    ERROR = f'[{colors.FAIL}\u2714{colors.ENDC}]'


class Operation:

    def __init__(self, command: str):
        self.command = command

    def execute(self, depth: int, forceyes=True):
        preamble = "  " * depth
        message = f'{preamble}{STATUS.PROGRESS} {self.command}'
        print(message, end='', flush=True)

        _cmd = f'yes | {self.command}'
        process = subprocess.Popen(
            _cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        process.wait()

        if process.returncode == 0:
            message = f'{preamble}{STATUS.OK} {self.command}'
        else:
            message = f'{preamble}{STATUS.ERROR} {self.command}'
        print(f'\r{message}')
