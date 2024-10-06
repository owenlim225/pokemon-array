# Limosnero, Sherwin P.
# J2S
# Machine Problem #1M

from tabulate import tabulate


class PokemonGame:
    def __init__(self):
        self.player1 = []
        self.player2 = []

        # Pokémon names, health, power, poison, and potions
        self.available_pokemons = [
            ["Pikachu", 35, 55, 12, 2],
            ["Bulbasaur", 45, 49, 15, 3],
            ["Charmander", 39, 52, 8, 1],
            ["Squirtle", 44, 48, 10, 2],
            ["Jigglypuff", 115, 45, 20, 4],
            ["Gengar", 60, 65, 25, 5],
            ["Machamp", 90, 130, 14, 3],
            ["Lapras", 130, 85, 6, 4],
            ["Psyduck", 50, 52, 9, 2],
            ["Snorlax", 160, 110, 5, 4],
        ]

    def pokemon_list_display(self, available_pokemons):
        headers = ["Name", "HP", "Attack", "Poison", "Potion"]
        print(tabulate(available_pokemons, headers, tablefmt="pretty"))

    def choose_Pokemon(self, player, available_pokemons, max_choices) -> None:
        while True:
            self.pokemon_list_display(available_pokemons)
            choices = list(map(int, input(f"Choose up to {max_choices} Pokémon/s (separate numbers with space): ").split()))

            # Validate choice: must select at least 1 Pokémon and up to the maximum allowed
            if (1 <= len(choices) <= max_choices) and all(1 <= choice <= len(available_pokemons) for choice in choices):
                # Add selected Pokémon to player's list and remove from available list
                player.extend([available_pokemons[choice - 1] for choice in choices])
                available_pokemons = [pokemon for i, pokemon in enumerate(available_pokemons) if i + 1 not in choices]
                print(f"Player has chosen: {[pokemon[0] for pokemon in player]}")
                break  # Exit the loop after successful selection
            else:
                print("Invalid selection. Please choose valid Pokémon.")

    def start_game(self):
        max_choices_player1 = 4
        # Player 1 chooses Pokémon
        self.choose_Pokemon(self.player1, self.available_pokemons, max_choices_player1)

        # Player 2 must choose the same number of Pokémon as Player 1
        num_choices_player2 = len(self.player1)

        # Filter available Pokémon for Player 2
        available_for_player2 = [pokemon for pokemon in self.available_pokemons if pokemon not in self.player1]

        # Player 2 chooses Pokémon
        self.choose_Pokemon(self.player2, available_for_player2, num_choices_player2)

        print()
        print(f"Player 1's Pokémon: {self.player1}")
        print(f"Player 2's Pokémon: {self.player2}")

# Example usage:
game = PokemonGame()
game.start_game()
