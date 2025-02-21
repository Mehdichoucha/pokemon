class Pokemon:
    def __init__(self, name, pv, level, atk, dfc, type_pokemon,gain_xp):
        self.__name = name
        self.__pv = pv
        self.__atk = atk
        self.__dfc = dfc
        self.__type_pokemon = type_pokemon
        self.__level = level 
        self.__xp = 0
        self.__xp_to_next_level = 1000
        self.__gain_xp = gain_xp
    # Getter methods
    def get_name(self):
        return self.__name

    def get_pv(self):
        return self.__pv

    def get_atk(self):
        return self.__atk

    def get_dfc(self):
        return self.__dfc

    def get_level(self):
        return self.__level

    def get_type_pokemon(self):
        return self.__type_pokemon
    
    def get_xp(self):
        return self.__xp
    
    def get_xp_to_next_level(self):
        return self.__xp_to_next_level
    
    def get_gain_xp(self):
        return self.__gain_xp

    # Setter methods
    def set_atk(self, atk):
        self.__atk = atk

    def set_dfc(self, dfc):
        self.__dfc = dfc

    def set_level(self, level):
        self.__level = level
    
    def set_gain_xp(self,gain_xp):
        self.__gain_xp = gain_xp

    # Method to receive damage
    def receive_damage(self, damage):
        self.__pv -= damage
        if self.__pv < 0:
            self.__pv = 0

    # Method to calculate damage
    def calculate_damage(self, defense):
        type_advantages = {
        ("fire", "water"): 0.5,
        ("fire", "steel"): 2,
        ("fire", "dragon"): 0.5,
        ("fire", "fire"): 0.5,
        ("fire", "ice"): 2,
        ("fire", "bug"): 2,
        ("fire", "plant"): 2,
        ("fire", "rock"): 0.5,
        ("water", "dragon"): 0.5,
        ("water", "water"): 0.5,
        ("water", "grass"): 0.5,
        ("water", "rock"): 2,
        ("water", "ground"): 2,
        ("water", "fire"): 2,
        ("ground", "fire"): 2,
        ("electric", "grass"): 0.5,
        ("grass", "electric"): 2,
        ("steel", "steel"): 2,
        ("steel", "water"): 0.5,
        ("steel", "electric"): 0.5,
        ("steel", "fairy"): 2,
        ("steel", "fire"): 0.5,
        ("steel", "ice"): 2,
        ("steel", "rock"): 2,
        ("fighting", "steel"): 2,
        ("fighting", "fairy"): 0.5,
        ("fighting", "ice"): 2,
        ("fighting", "bug"): 0.5,
        ("fighting", "normal"): 2,
        ("fighting", "poison"): 0.5,
        ("fighting", "psychic"): 0.5,
        ("fighting", "rock"): 2,
        ("fighting", "ghost"): 0,
        ("fighting", "dark"): 2,
        ("fighting", "flying"): 0.5,
        ("dragon", "steel"): 0.5,
        ("dragon", "dragon"): 2,
        ("dragon", "fairy"): 0,
        ("electric", "dragon"): 0.5,
        ("electric", "water"): 2,
        ("electric", "electric"): 0.5,
        ("electric", "grass"): 0.5,
        ("electric", "ground"): 0,
        ("electric", "flying"): 2,
        ("fairy", "steel"): 0.5,
        ("fairy", "fighting"): 2,
        ("fairy", "dragon"): 2,
        ("fairy", "fire"): 0.5,
        ("fairy", "poison"): 0.5,
        ("fairy", "dark"): 2,
        ("ice", "steel"): 0.5,
        ("ice", "dragon"): 2,
        ("ice", "water"): 0.5,
        ("ice", "fire"): 0.5,
        ("ice", "ice"): 0.5,
        ("ice", "grass"): 2,
        ("ice", "ground"): 2,
        ("ice", "flying"): 2,
        ("bug", "steel"): 0.5,
        ("bug", "fighting"): 0.5,
        ("bug", "fairy"): 0.5,
        ("bug", "fire"): 0.5,
        ("bug", "grass"): 2,
        ("bug", "poison"): 0.5,
        ("bug", "psychic"): 2,
        ("bug", "ghost"): 0.5,
        ("bug", "dark"): 2,
        ("bug", "flying"): 0.5,
        ("normal", "steel"): 0.5,
        ("normal", "rock"): 0.5,
        ("normal", "ghost"): 0,
        ("grass", "steel"): 0.5,
        ("grass", "dragon"): 0.5,
        ("grass", "water"): 2,
        ("grass", "fire"): 0.5,
        ("grass", "bug"): 0.5,
        ("grass", "grass"): 0.5,
        ("grass", "poison"): 0.5,
        ("grass", "rock"): 2,
        ("grass", "ground"): 2,
        ("grass", "flying"): 0.5,
        ("poison", "steel"): 0,
        ("poison", "fairy"): 2,
        ("poison", "grass"): 2,
        ("poison", "poison"): 0.5,
        ("poison", "rock"): 0.5,
        ("poison", "ground"): 0.5,
        ("poison", "ghost"): 0.5,
        ("psychic", "steel"): 0.5,
        ("psychic", "fighting"): 2,
        ("psychic", "poison"): 2,
        ("psychic", "psychic"): 0.5,
        ("psychic", "dark"): 0,
        ("rock", "steel"): 0.5,
        ("rock", "fighting"): 0.5,
        ("rock", "fire"): 2,
        ("rock", "ice"): 2,
        ("rock", "bug"): 2,
        ("rock", "ground"): 0.5,
        ("rock", "flying"): 2,
        ("ground", "steel"): 2,
        ("ground", "electric"): 2,
        ("ground", "fire"): 2,
        ("ground", "bug"): 0.5,
        ("ground", "grass"): 0.5,
        ("ground", "poison"): 2,
        ("ground", "rock"): 2,
        ("ground", "flying"): 0,
        ("ghost", "normal"): 0,
        ("ghost", "psychic"): 2,
        ("ghost", "ghost"): 2,
        ("ghost", "dark"): 0.5,
        ("dark", "fighting"): 0.5,
        ("dark", "fairy"): 0.5,
        ("dark", "ghost"): 2,
        ("dark", "psychic"): 2,
        ("dark", "dark"): 0.5,
        ("flying", "steel"): 0.5,
        ("flying", "fighting"): 2,
        ("flying", "electric"): 0.5,
        ("flying", "bug"): 2,
        ("flying", "grass"): 2,
        ("flying", "rock"): 0.5
        }            

        multiple = type_advantages.get((self.__type_pokemon, defense.get_type_pokemon()), 1)
        damage = self.__atk * multiple - int(defense.get_dfc())
        return max(damage, 0)
    
    def level_up(self):
        self.__level +=1
        self.__xp -= self.__xp_to_next_level
        self.__xp_to_next_level = int(self.__xp_to_next_level * 1,5)
        self.__pv += 10
        self.__atk += 5
        self.__dfc += 5
        print(f"{self.__name} has been level up to level {self.__level}")
    
    def gain_experience(self, xp_earned):
        self.__xp += xp_earned
        if self.__xp >= self.__xp_to_next_level:
            self.level_up()