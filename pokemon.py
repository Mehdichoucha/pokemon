import pygame

pikachu = pygame.image.load("image/pikachu.png")
bulbazaur = pygame.image.load("image/bulbizarre.png")
charmander_sprite1 = pygame.image.load("image/salameche")
squirtle = pygame.image.load("image/carapuce.png")


class Pokemon:
    def __init__(self, nom, pv, atk, dfc, vts, sprite1, sprite2):
        self.__nom = nom #name
        self.__pv = pv # life points stat
        self.__atk = atk # attack stat
        self.__dfc = dfc # defence stat
        self.__vts = vts # speed stat
        self.__sprite1 = sprite1
        self.__sprite2 = sprite2

        def get_nom(self):
            return self.__nom
        def get_pv(self):
            return self.__pv
        def get_atk(self):
            return self.__atk
        def get_dfc(self):
            return self.__dfc
        def get_vts(self):
            return self.__vts
        def get_sprite1(self):
            return self.__sprite1
        def get_sprite2(self):
            return self.__sprite2
        
# pokemon of the player
    def pokemon1(self):
        self.__nom = nom #name
        self.__pv = pv # life points stat
        self.__atk = atk # attack stat
        self.__dfc = dfc # defence stat
        self.__vts = vts # speed stat
        self.__sprite1 = sprite1
        self.__sprite2 = sprite2
        
# pokemon of the opponent
    def pokemon2(self):
        self.__nom = nom #name
        self.__pv = pv # life points stat
        self.__atk = atk # attack stat
        self.__dfc = dfc # defence stat
        self.__vts = vts # speed stat
        self.__sprite1 = sprite1
        self.__sprite2 = sprite2


charmander_sprite1 = pygame.image.load("image/salameche")
charmander_sprite2 = pygame.image.load("image/salameche")
charmender = Pokemon("salamèche", 39, 52, 43, 65, charmander_sprite1, charmander_sprite2)

pikachu_sprite1 = pygame.image.load("image/pikachu.png")
pikachu_sprite2 = pygame.image.load("image/pikachu.png")
pikachu = Pokemon("pikachu", 35, 55, 40, 90, pikachu_sprite1, pikachu_sprite2)

squirtle_sprite1 = pygame.image.load("image/carapuce.png")
squirtle_sprite2 = pygame.image.load("image/carapuce.png")
squirtle = Pokemon("carapuce", 44, 48, 64, 43, squirtle_sprite1, squirtle_sprite2)

bulbazaur_sprite1 = pygame.image.load("image/bulbizarre.png")
bulbazaur_sprite2 = pygame.image.load("image/bulbizarre.png")
bulbazaur = Pokemon("bulbizarre", 45, 55, 40, 90, bulbazaur_sprite1, bulbazaur_sprite2)
