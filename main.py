# main.py
exit_flag = False  # Global variable

from display import Display
from backend import Mechanism

def main():
    display = Display()
    mechanism = Mechanism(display)

    # This will run the input loop
    mechanism.get_user_input()

if __name__ == "__main__":
    main()
