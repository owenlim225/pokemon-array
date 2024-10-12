# backend.py
# Limosnero, Sherwin P.
# J2S <3

import random

pokemon_char = {
    "Mewtwo": 90,
    "Snorlax": 80,
    "Machamp": 75,
    "Gengar": 70,
    "Bulbasaur": 60,
    "Squirtle": 58,
    "Charmander": 55,
    "Eevee": 52,
    "Pikachu": 50,
    "Jigglypuff": 45,
}

class Mechanism:
    def __init__(self, display):
        self.display = display
        self.first_time = True
        self.selecting_pokemon = False 

    def get_user_input(self):
        global exit_flag
        self.display.layout["side"].visible = False
        self.display.layout["footer"].visible = False

        while True:
            user_input = input()
            if user_input.lower() == 'x':
                exit_flag = True
                break
            elif user_input.lower() == 'c':
                self.display.update_main_window("Continue selected")
            elif user_input.lower() == 'p':
                self.display.pokedex()
            elif user_input.lower() == 'q':
                self.display.layout["side"].visible = True
            elif user_input.lower() == 's':
                self.display.select_pokemon()
                self.display.layout["footer"].visible = True
                self.selecting_pokemon = True
            elif user_input.lower() == 'b':
                self.display.update_battle_results(self.get_battle_results())
            elif self.selecting_pokemon and user_input.isdigit():
                self.handle_pokemon_selection(int(user_input))
            else:
                self.display.invalid_input()

            if not self.selecting_pokemon:
                self.selecting_pokemon = False

    def handle_pokemon_selection(self, choice):
        # Handle the user's selection of Pokemon here
        if 1 <= choice <= len(pokemon_char):
            pokemon_list = list(pokemon_char.keys())
            selected_pokemon = pokemon_list[choice - 1]
            print(f"You chose {selected_pokemon}")
            return selected_pokemon
        else:
            print("Invalid choice. Please select a valid number.")
            self.selecting_pokemon = True

    def get_battle_results(self):
        results = [
            (1, 120, 110, "Player wins"),
            (2, 130, 140, "CPU wins"),
            (3, 150, 150, "Draw"),
            # ... (other results)
        ]
        return results

    def bot_pokemon(self):
        return random.choice(list(pokemon_char.keys()))

    def calculate_power(self, base_power):
        return base_power + random.randint(1, 100)

    def battle(self, user_pokemon, bot_pokemon):
        # Implement battle logic here
        pass
