import pygame


class Pokemon:
    def __init__(self, name, lvl, pv, atk, dfc, vts, sprite1, sprite2):
        self.__name = name #name
        self.__lvl = lvl
        self.__pv = pv # life points stat
        self.__atk = atk # attack stat
        self.__dfc = dfc # defence stat
        self.__satk = atk # special attack stat
        self.__sdfc = dfc # special defence stat
        self.__vts = vts # speed stat
        self.__sprite1 = sprite1
        self.__sprite2 = sprite2

        def get_name(self):
            return self.__name
        def get_lvl(self):
            return self.__lvl
        def get_pv(self):
            return self.__pv
        def get_atk(self):
            return self.__atk
        def get_dfc(self):
            return self.__dfc
        def get_satk(self):
            return self.__satk
        def get_sdfc(self):
            return self.__sdfc
        def get_vts(self):
            return self.__vts
        def get_sprite1(self):
            return self.__sprite1
        def get_sprite2(self):
            return self.__sprite2
        
# pokemon of the player
#    def pokemon1(self):
#        self.__name = name #name
#        self.__lvl = lvl
#        self.__pv = pv # life points stat
#        self.__atk = atk # attack stat
#        self.__dfc = dfc # defence stat
#        self.__satk = atk # special attack stat
#        self.__sdfc = dfc # special defence stat
#        self.__vts = vts # speed stat
#        self.__sprite1 = sprite1
#        self.__sprite2 = sprite2
        
# pokemon of the opponent
#    def pokemon2(self):
#        self.__name = name #name
#        self.__lvl = lvl
#        self.__pv = pv # life points stat
#        self.__atk = atk # attack stat
#        self.__dfc = dfc # defence stat
#        self.__satk = atk # special attack stat
#        self.__sdfc = dfc # special defence stat
#        self.__vts = vts # speed stat
#        self.__sprite1 = sprite1
#        self.__sprite2 = sprite2

class Attacks:
    def __init__(self, name, type, power, accuracy, pp):
        self.name = name
        self.type = type
        self.power = power # damage
        self.accuracy = accuracy # the attack can miss
        self.pp = pp # uses of the attack


slash = Attacks("Tranche", "normal", 70, 100, 20)
air_slash = Attacks("Lame d'Air", "fly", 70, 95, 10)
flamethrower = Attacks("Lance Flame", "fire", 90, 100, 15)
dragon_claw = Attacks("Draco Griffe", "dragon", 90, 100, 15)
wave_crash = Attacks("Aqua Tacle", "water", 120, 75, 10)
meteor_mash = Attacks("Poing Météore", "steel", 90, 90, 10)
iron_tail = Attacks("Queue de fer", "steel", 100, 75, 15)
low_sweep = Attacks("Baleyette", "fight", 65, 100, 20)
aura_sphere = Attacks("Aura Sphère", "fight", 80, 100, 15)
luster_purge = ("Lumi-Éclat", "psy", 95, 100, 5)
blizzard = Attacks("Blizzard", "ice", 110, 75, 5)
ice_punch = Attacks("Poing Glace", "ice", 75, 100, 15)




charmander_sprite1 = pygame.image.load("images/pokemon/charmender.png")
charmander_sprite2 = pygame.image.load("images/pokemon/charmender.png")
charmender = Pokemon("salamèche", 10, 39, 52, 43, 65, charmander_sprite1, charmander_sprite2)

pikachu_sprite1 = pygame.image.load("images/pokemon/pikachu.png")
pikachu_sprite2 = pygame.image.load("images/pokemon/pikachu.png")
pikachu = Pokemon("pikachu", 10, 35, 55, 40, 90, pikachu_sprite1, pikachu_sprite2)

squirtle_sprite1 = pygame.image.load("images/pokemon/squirtle.png")
squirtle_sprite2 = pygame.image.load("images/pokemon/squirtle.png")
squirtle = Pokemon("carapuce", 10,  44, 48, 64, 43, squirtle_sprite1, squirtle_sprite2)

bulbasaur_sprite1 = pygame.image.load("images/pokemon/bulbasaur.png")
bulbasaur_sprite2 = pygame.image.load("images/pokemon/bulbasaur.png")
bulbasaur = Pokemon("bulbizarre", 10, 45, 55, 40, 90, bulbasaur_sprite1, bulbasaur_sprite2)

