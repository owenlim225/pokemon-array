import os
import GameManager
import DisplayManager

class Gameplay:
    def __init__(self) -> None:

        # initialize import manager classes
        self.GM = GameManager()
        self.DM = DisplayManager()
        
        # Battle var flag
        self.all_pokemon_is_used = False
        
        # Start the game
        self.startGame()


    def startGame(self) -> None:
        
        # Select pokemon
        self.selectPokemonArray()

        # select pokemon used for battle
        while not self.all_pokemon_is_used:
            self.all_pokemon_is_used = self.selectBattlePokemon()
            
            if self.all_pokemon_is_used:
                os.system('cls') # clear terminal
                break
            
            # main functions to start battle
            self.battlePreparation()
            self.mainBattle()
            self.postBattleAdjustment()

        self.GM.endBattle()
        
        
    

    

    def selectBattlePokemon(self) -> None:
        pass


if __name__ == "__main__":
    Gameplay()