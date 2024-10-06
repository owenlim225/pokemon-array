# Limosnero, Sherwin P.
# J2S
# Machine Problem #1M

# Pokémon names, health, power, poison, and potions
pokemons = [
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

class Mechanics:
    def __init__(self) -> None:
        self.player1 = []
        self.player2 = []
    
    # Print out all the names of the Pokémon
    def pokemon_list_display(self, available_pokemons) -> None:
        for count, pokemon in enumerate(available_pokemons, start=1):
            print(f"[{count}] {pokemon[0]}", end="\t\t" if count % 2 else "\n")

    # Choose Pokémon for the given player
    def choose_Pokemon(self, player, available_pokemons) -> None:
        while len(player) < 4:
            self.pokemon_list_display(available_pokemons)
            max_choices = 4 - len(player)
            choices = list(map(int, input(f"Choose up to {max_choices} Pokémon/s (separate numbers with space): ").split()))
            
            # Validate choice: must select at least 1 Pokémon and up to the maximum allowed
            if (1 <= len(choices) <= max_choices) and all(1 <= choice <= len(available_pokemons) for choice in choices):
                # Add selected Pokémon to player's list and remove from available list
                player.extend([available_pokemons[choice - 1] for choice in choices])
                available_pokemons = [pokemon for i, pokemon in enumerate(available_pokemons) if i + 1 not in choices]
                print(f"Player has chosen: {[pokemon[0] for pokemon in player]}")
            else:
                print("Invalid selection. Please choose valid Pokémon.")

class Display(Mechanics):
    def __init__(self) -> None:
        super().__init__()
    
    def run(self) -> None:
        available_pokemons = pokemons.copy()
        
        # Allow Player 1 to choose Pokémon first
        print("\nPlayer 1, choose your Pokémon:")
        self.choose_Pokemon(self.player1, available_pokemons)
        available_pokemons = [pokemon for pokemon in available_pokemons if pokemon not in self.player1]
        
        # Allow Player 2 to choose Pokémon second
        print("\nPlayer 2, choose your Pokémon:")
        self.choose_Pokemon(self.player2, available_pokemons)
        
        print("\nSelection complete!")
        print(f"Player 1's team: {[pokemon[0] for pokemon in self.player1]}")
        print(f"Player 2's team: {[pokemon[0] for pokemon in self.player2]}")

if __name__ == "__main__":
    display = Display()
    display.run()
