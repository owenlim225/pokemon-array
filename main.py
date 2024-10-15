#Limosnero, Sherwin P.
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
    
    # Print out all the names of the pokemon
    def pokemon_list_display(self) -> None:
        for count, pokemon in enumerate(pokemons, start=1):
            print(f"[{count}] {pokemon[0]}", end="\t\t" if count % 2 else "\n")
    
    
    
    
    # Choose four Pokémon for the given player
    def choose_Pokemon(self, player) -> None:
        while len(player) < 4:
            self.pokemon_list_display()
            choices = list(map(int, input("Choose 1-4 Pokemon/s: ").split()))
            
            if len(choices) == 4 and all(1 <= choice <= len(pokemons) for choice in choices):
                # Replace player's Pokémon with selected choices
                player.clear()
                player.extend([pokemons[choice - 1] for choice in choices])
                print(f"Player has chosen: {[pokemon[0] for pokemon in player]}")
            else:
                print("Invalid selection. Please choose exactly 4 valid Pokémon.")

class Display(Mechanics):
    def __init__(self) -> None:
        super().__init__()
    
    def run(self) -> None:
        while not (self.player1 and self.player2):
            print("\nPlayer 1, choose your Pokémon:")
            self.choose_Pokemon(self.player1)
            
            print("\nPlayer 2, choose your Pokémon:")
            self.choose_Pokemon(self.player2)
            
        print("\nSelection complete!")
        print(f"Player 1's team: {[pokemon[0] for pokemon in self.player1]}")
        print(f"Player 2's team: {[pokemon[0] for pokemon in self.player2]}")
        

if __name__ == "__main__":
    display = Display()
    display.run()
