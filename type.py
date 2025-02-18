import pygame
import random
import time

# le type défini est le pokemon qui se fait attaqué, les faiblesses / résistances dépendes de l'attaque recue, c'est le type du pokemon defensif
# une attaque ne possède qu'un seul et unique type, alors que le pokemon peut avoir deux types au maximum
# faiblesses du type = 1/2 de dégats recue
# résistances du type =  fois 2 de dégats recus
# certains types ont des immunités et les dégats recus seront de 0

# des combinaisons sont possibles 
# 1 faiblesse et 0 resistance : si un pokemon est plante pure ( sans autre type ) recois une attaque feu, il prend fois 2 de degats
# 0 faiblesse et 1 resistance : si un pokemon est eau pure ( sans autre type ) recois une attaque feu, il prend fois 1/2 de degats
# 2 faiblesse et 0 resistance : si un pokemon plante et acier recois une attaque feu, il prend fois 4 de degats
# 0 faiblesse et 2 resistance : si un pokemon eau et electik recois une attaque acier il prend 1/4 de degats
# 1 faiblesse et 1 resistance : si un pokemon eau et feu recois une attaque plante il prend des degats sans multiplicateur, les faiblesses et résistances seront annulées entre elles
# 0 faiblesse et 0 resistance et 1 immunité : si un pokemon spectre recois une attaque normal il prend 0 degats
# si un pokemon avec 2 types a 1 faiblesse et 1 immunité, il prendra 0 degats, l'immunité est prioritaire

# exemple : 
# un pokemon feu et acier aura comme multiplicateur de degat : 
# de fois 4 avec une attaque sol, 2 faiblesse et 0 resistance
# de fois 2 avec une attaque combat ou eau, 1 faiblesse et 0 resistance
# de fois 1/2 avec une attaque dragon, normal, psy, ou vol, 0 faiblesse et 1 resistance
# de fois 1/4 avec une attaque acier, fée, glace, insecte, ou plante, 0 faiblesse et 2 resistance
# de fois 0 avce une attaque poison, 1 immunité
# et pour les types d'attaques restants, les degats seront basiques, ils ne prennent pas en compte les faiblesses et resistances

normal = pygame.image.load("images/types/normal.png")
fire = pygame.image.load("images/types/fire.png")
water = pygame.image.load("images/types/water.png")
grass = pygame.image.load("images/types/grass.png")
electric = pygame.image.load("images/types/electric.png")
steel = pygame.image.load("images/types/steel.png")
fightning = pygame.image.load("images/types/fightning.png")
psychic = pygame.image.load("images/types/psychic.png")
poison = pygame.image.load("images/types/poison.png")
dragon = pygame.image.load("images/types/dragon.png")
ghost = pygame.image.load("images/types/ghost.png")
dark = pygame.image.load("images/types/dark.png")
ground = pygame.image.load("images/types/ground.png")
fairy = pygame.image.load("images/types/fairy.png")
flying = pygame.image.load("images/types/flying.png")
rock = pygame.image.load("images/types/rock.png")
bug = pygame.image.load("images/types/bug.png")
ice = pygame.image.load("images/types/ice.png")

"####"

# type
# resistances : 
# faiblesses : 
# immunités : 

# normal
# resistances : 0
# faiblesses : 1 ["combat"]
# immunités : 1 ["spectre"]

def normal_type():
    normal_strength = []
    normal_weakness = [fightning]
    normal_immunity = [ghost]

# feu
# resistances : 6 ["acier", "fée", "glace", "insecte", "feu", plante]
# faiblesses : 3 ["roche", "eau", "sol"]
# immunités : 0

def fire_type():
    fire_strength = [steel, fairy, ice, bug, fire, grass]
    fire_weakness = [rock, water, ground]
    fire_immunity = []

# eau
# resistances : 3 ["feu", "glace", "acier"]
# faiblesses : 2 ["plante", "electrik"]
# immunités : 0

def water_type():
    water_strength = [fire, ice, steel]
    water_weakness = [grass, electric]
    water_immunity = []

# plante
# resistances : 4 ["eau", "electrik", "sol", "plante"]
# faiblesses : 5 ["vol", "insecte", "feu", "glace", "poison"]
# immunités : 0

def grass_type():
    grass_strength = [water, electric, ground, grass]
    grass_weakness = [flying, bug, fire, ice, ]
    grass_immunity = [ghost]

# electrik
# resistances : 3 ["vol", "electrik", "acier"]
# faiblesses : 1 ["sol"]
# immunités : 0

def electric_type():
    grass_strength = [water, electric, ground, grass]
    grass_weakness = [flying, bug, fire, ice, ]
    grass_immunity = [ghost]

# acier ( meilleur type défensif pour moi )
# resistances : 9 ["acier", "dragon", "fée", "glace", "insecte", "normal", "plante", "psy", "roche", "vol"]
# faiblesses : 3 ["sol", "feu", "combat"]
# immunités : 1 ["poison"]

def steel_type():
    grass_strength = [steel, dragon, fairy, ice, bug, normal, grass, psychic, rock, flying]
    grass_weakness = [ground, fire, fightning]
    grass_immunity = [poison]

# combat
# resistances : 2 ["roche", insecte]
# faiblesses : 3 ["fée", "psy", "vol"]
# immunités : 0

def fightning_type():
    grass_strength = [bug, rock]
    grass_weakness = [fairy, psychic , flying]
    grass_immunity = []

# dragon
# resistances : 4 ["eau", "plante", "feu", "electrik"]
# faiblesses : 3 ["fée", "dragon", "glace"]
# immunités : 0

def dragon_type():
    grass_strength = [water, grass, fire, electric]
    grass_weakness = [fairy, dragon , ice]
    grass_immunity = []

# fée
# resistances : 3 ["combat", "ténèbres", "insecte"]
# faiblesses : 2 ["acier", "poison"]
# immunités : 0 ["dragon"]

def fairy_type():
    grass_strength = [fightning, dark, bug]
    grass_weakness = [steel, poison]
    grass_immunity = [dragon]

# glace
# resistances : 1 ["glace"]
# faiblesses : 4 ["feu", "acier", "combat", "roche"]
# immunités : 0

def ice_type():
    grass_strength = [ice]
    grass_weakness = [fire, steel, fightning, rock]
    grass_immunity = []

# insecte
# resistances : 2 ["combat", "plante"]
# faiblesses : 3 ["feu", "roche", "vol"]
# immunités : 0

def bug_type():
    grass_strength = [bug, rock]
    grass_weakness = [fairy, psychic , flying]
    grass_immunity = []

# poison
# resistances : 5 ["poison", "fée", "combat", "plante", "insecte"]
# faiblesses : 2 ["psy", "sol"]
# immunités : 0

def poison_type():
    grass_strength = [poison, fairy, fightning, grass, bug]
    grass_weakness = [psychic, ground]
    grass_immunity = []

# psy
# resistances : 2 ["psy", "combat"]
# faiblesses : 3 ["ténèbre", "spectre", "insecte"]
# immunités : 0

def psychic_type():
    grass_strength = [psychic, fightning]
    grass_weakness = [dark, ghost, bug]
    grass_immunity = []

# roche
# resistances : 4 ["feu","normal", "vol", "poison"]
# faiblesses : 5 ["acier", "combat", "eau", "plante", "sol"]
# immunités : 0

def rock_type():
    grass_strength = [fire, normal, flying, poison]
    grass_weakness = [steel, fightning, water, grass, ground]
    grass_immunity = []

# sol
# resistances : 2 ["poison", "roche"]
# faiblesses : 3 ["eau", "glace", plante]
# immunités : 1 ["electrik"]

def ground_type():
    grass_strength = [poison, rock]
    grass_weakness = [water, ice , grass]
    grass_immunity = [electric]

# spectre
# resistances : 2 ["insecte", "poison"]
# faiblesses : 2 ["spectre", "ténèbre"]
# immunités : 2 ["combat", "normal"]

def ghost_type():
    grass_strength = [bug, poison]
    grass_weakness = [ghost, dark]
    grass_immunity = [fightning, normal]

# ténèbre
# resistances : 2 ["spectre", "ténèbre"]
# faiblesses : 3 ["insecte", "fée", "combat"]
# immunités : 1 ["psy"]

def dark_type():
    grass_strength = [ghost, dark]
    grass_weakness = [bug, fairy , fightning]
    grass_immunity = [psychic]

# vol
# resistances : 3 ["combat", "insecte", "plante"]
# faiblesses : 3 ["roche", "glace", "electrik"]
# immunités : 1 ["sol"]

def flying_type():
    grass_strength = [fightning, bug, grass]
    grass_weakness = [rock, ice , electric]
    grass_immunity = [ground]