# Courtesy to @Ellisia-Chan

import random 

class PokemonArray:
    def __init__(self) -> None:  
        self.pokemon_list = [
                    # [Name, Health, Power, Poisons, Potions, isUsed]
                    ["Pikachu", 50, 80, 0, 0, False],
                    ["Charmander", 50, 70, 0, 0, False],
                    ["Bulbasaur", 60, 60, 0, 0, False],
                    ["Squirtle", 70, 50, 0, 0, False],
                    ["Jigglypuff", 70, 45, 0, 0, False],
                    ["Eevee", 95, 40, 0, 0, False],
                    ["Snorlax", 150, 90, 0, 0, False],
                    ["Gengar", 85, 75, 0, 0, False],
                    ["Machamp", 90, 70, 0, 0, False],
                    ["Mewtwo", 100, 85, 0, 0, False]
                ]
        
        self.RandomeValueGenerator()
    
    def RandomeValueGenerator(self) -> None:
        # Poison and Potion
        for i in range(len(self.pokemon_Array)):
            randomNum1 = random.randint(0, 3)
            randomNum2 = random.randint(0, 3)
            
            self.pokemon_Array[i][3] = randomNum1
            self.pokemon_Array[i][4] = randomNum2
    @property
    def GetPokemonArray(self) -> list:
        # ============================================
        # Returns the pokemon_Array.
        #
        # Return:
        #     list: A 2D list where each sublist contains the following:
        #     [Name (str), Health (int), Power (int), Poisons (int), Potions (int)].
        # ============================================
        return self.pokemon_Array