# main.py
# Limosnero, Sherwin P.
# J2S <3

from display import Display
from backend import Mechanism

if __name__ == "__main__":
    display = Display()
    mechanism = Mechanism(display)
    mechanism.get_user_input()
