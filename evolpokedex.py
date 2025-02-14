import json

with open("pokedex.json", "r") as file:
    data = json.load(file)
class Pokemon:
    def __init__(self, name, level, evolution=None):
        self.name = name
        self.level = level
        self.evolution = evolution

    def check_evolution(self):
        if self.level >= 5 and self.evolution:
            print(f"{self.name} evolves into {self.evolution}!")
            self.name = self.evolution
            self.evolution = None

    def evolve(self):
        if self.evolution:
            print(f"{self.name} evolves into {self.evolution}!")
            self.name = self.evolution
            self.evolution = None
        else:
            print(f"{self.name} can't evolve")

pokemon_list = [
    Pokemon(pokemon["name"], pokemon["level"], pokemon["evolution"])
    for pokemon in data["Pokemon"]
]

for pokemon in pokemon_list:
    pokemon.check_evolution()
    print(pokemon.name)

pokemon_list[0].level = 3
pokemon_list[1].level = 4 
pokemon_list[2].level = 6  

print("\nAfter leveling up:")

for pokemon in pokemon_list:
    pokemon.check_evolution() 
    print(pokemon.name)
