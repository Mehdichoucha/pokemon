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
            ("water", "fire"): 2,
            ("ground", "fire"): 2,
            ("electric", "plant"): 0.5,
            ("plant", "electric"): 2,
            # Add more type interactions as needed
        }

        multiple = type_advantages.get((self.__type_pokemon, defense.get_type_pokemon()), 1)
        damage = self.__atk * multiple - defense.get_dfc()
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
