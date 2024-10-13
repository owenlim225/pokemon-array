# main.py
exit_flag = False  # Global variable

import display as DP
import backend as BE


class Gameplay:
    def __init__(self) -> None:
        # Initialize Managers Class
        self.game_display = DP.Display()
        self.game_backend = BE.Mechanism()

        # Battle Variable Flag
        self.all_pokemons_used = False

        # Start the program
        self.main()



def main():
    display = Display()
    mechanism = Mechanism(display)

    # This will run the input loop
    mechanism.get_user_input()

if __name__ == "__main__":
    main()
