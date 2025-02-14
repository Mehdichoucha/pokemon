class Pokemon:
    def __init__(self, name, level, evolution=None):
        self.name = name
        self.level = level
        self.evolution = evolution

    def evolut(self):
        if self.evolution:
            print(f"{self.name} evolves into {self.evolution}!")
            self.name = self.evolution
            self.evolution = None
        else:
            print(f"{self.name} can't evolve")

salameche = Pokemon("Salameche", 15, "Dragofeu")
salameche.evolut()
print(salameche.name)