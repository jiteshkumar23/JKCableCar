import os
import subprocess
import sys
import time

import keyboard
from autoit import autoit

from CoreMethods.CoreMethods import (debounce_key, firstPageFill,setImagePath)


def exit_program():
    print("r+4 keys pressed - Exiting... Goodbye!")
    os._exit(0)  # Exit the current process


def main():
    print("Press - r+1 - For filling first page only")
    print("Press - r+4 - For exiting the script")

    # Add listener
    keyboard.add_hotkey('r+4', exit_program)

    while True:

        if keyboard.is_pressed("r+1"):
            print("Keys Pressed - r+1 - Filling first page only")
            setImagePath()
            firstPageFill()
            debounce_key("r+1")  # Wait until the key is released


if __name__ == "__main__":
    main()
