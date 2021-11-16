# Import module
import os
import sys
import wget
from colorama import Fore

if os.name == "nt":
    winpcap_url = "https://www.winpcap.org/install/bin/WinPcap_4_1_3.exe"
    winpcap_dir = os.environ["ProgramFiles(x86)"] + "\\WinPcap"
    if not os.path.exists(winpcap_dir):
        print(
            f'{Fore.MAGENTA}[!] {Fore.YELLOW}Warning! The component "WinPcap" has not been installed!\n    is needed to do a syn, udp, etc attack\n    Do you want to install it automatically? (y/n){Fore.RESET}'
        )
        if input(f"{Fore.MAGENTA} >>> {Fore.BLUE}").lower() in ("y", "yes", "1"):
            print(f"{Fore.YELLOW}[~] {Fore.CYAN}installing installer...{Fore.BLUE}\n")
            winpcap_installer = wget.download(winpcap_url)
            os.startfile(winpcap_installer)
            print(
                f"\n\n{Fore.GREEN}[?] {Fore.YELLOW}restart the program{Fore.RESET}"
            )
            sys.exit(1)
