from test1 import Pokemon  
from battle import Battle    

# instances  of Pokémon
pokemon1 = Pokemon("Salameche", 100, 1, 20, 10, "fire")
pokemon2 = Pokemon("Carapuce", 100, 3, 15, 12, "water")


battle = Battle(pokemon1, pokemon2)
battle.start_battle()