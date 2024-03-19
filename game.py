# main script
import subprocess

try:
    import plotext
except ImportError:
    subprocess.check_call(["pip", "install", "plotext"])

from controls import main_menu


if __name__ == "__main__":

    print("Welcome to the basic finance concepts minigame!\n")
    main_menu()
