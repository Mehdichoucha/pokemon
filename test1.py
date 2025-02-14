class Pokemon:
    def __init__(self, name, pv, niv, atk, dfc, type_pokemon):
        self.__name = name
        self.__pv = pv
        self.__niv = niv
        self.__atk = atk
        self.__dfc = dfc
        self.__type_pokemon = type_pokemon
#
    # Getter methods
    def get_name(self):
        return self.__name

    def get_pv(self):
        return self.__pv

    def get_atk(self):
        return self.__atk

    def get_dfc(self):
        return self.__dfc

    def get_niv(self):
        return self.__niv

    def get_type_pokemon(self):
        return self.__type_pokemon

    # Setter methods
    def set_atk(self, atk):
        self.__atk = atk

    def set_dfc(self, dfc):
        self.__dfc = dfc

    def set_niv(self, niv):
        self.__niv = niv

    # Method to receive damage
    def receive_damage(self, damage):
        self.__pv -= damage
        if self.__pv < 0:
            self.__pv = 0

    # Method to calculate damage
    def calculate_demage(self, defense):
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
