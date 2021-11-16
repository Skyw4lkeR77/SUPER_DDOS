# Importa os modulos
import os
import sys
import platform
from time import ctime
from colorama import Fore

""" Fungsi ini akan menghentikan program ketika terjadi Error """


def CriticalError(message, error):
    print(f"""
    {Fore.RED}:=== Critical error:
    {Fore.MAGENTA}MESSAGE: {message}.
    {Fore.MAGENTA}ERROR: {error}
    {Fore.RED}:=== Python info:
    {Fore.MAGENTA}PYTHON VERSION: {platform.python_version()}
    {Fore.MAGENTA}PYTHON BUILD: {'{}, DATE: {}'.format(*platform.python_build())}
    {Fore.MAGENTA}PYTHON COMPILER: {platform.python_compiler()}
    {Fore.MAGENTA}SCRIPT LOCATION: {os.path.dirname(os.path.realpath(sys.argv[0]))}
    {Fore.MAGENTA}CURRENT LOCATION: {os.getcwd()}
    {Fore.RED}:=== System info:
    {Fore.MAGENTA}SYSTEM: {platform.system()}
    {Fore.MAGENTA}RELEASE: {platform.release()}
    {Fore.MAGENTA}VERSION: {platform.version()}
    {Fore.MAGENTA}ARCHITECTURE: {'{} {}'.format(*platform.architecture())}
    {Fore.MAGENTA}PROCESSOR: {platform.processor()}
    {Fore.MAGENTA}MACHINE: {platform.machine()}
    {Fore.MAGENTA}NODE: {platform.node()}
    {Fore.MAGENTA}TIME: {ctime()}
    {Fore.RED}:=== Report:
    {Fore.MAGENTA}Jika Error laporkan di sini: https://github.com/Skyw4lkeR77/POWER_DDOS/issues/new
    {Fore.RESET}
    """)
    sys.exit(5)
