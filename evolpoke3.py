import json

pokedex = {
    "Pokemon": [
        {"name": "Charmander", "type": "Fire", "level": 1, "evolution": "Charizard"},
        {"name": "Bulbasaur", "type": "Grass", "level": 3, "evolution": "Ivysaur"},
        {"name": "Squirtle", "type": "Water", "level": 5, "evolution": "Wartortle"}
    ]
}

with open("pokedex.json", "w") as file:
    json.dump(pokedex, file, indent=4)

with open("pokedex.json", "r") as file:
    data = json.load(file)

print(json.dumps(data, indent=4))


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
    Pokemon("Charmander", 1, "Charizard"),
    Pokemon("Bulbasaur", 3, "Ivysaur"),
    Pokemon("Squirtle", 5, "Wartortle")
]

for pokemon in pokemon_list:
    pokemon.check_evolution()
    print(pokemon.name) 

pokemon_list[0].level = 5 
pokemon_list[1].level = 5 
pokemon_list[2].level = 6  

print("\nAfter leveling up:")

for pokemon in pokemon_list:
    pokemon.check_evolution() 
    print(pokemon.name)  
