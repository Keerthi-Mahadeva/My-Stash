class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name,level = 5):
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10
        
    def opponent(self):
        return (self.weak, self.strong)

    def __str__(self):
        self.update()

        obj_blueprint = \
        """

        Class Variables:
        Pokemon Type={pok_type}
        Pokemon Attack  ={pok_attack}    
        Pokemon Defense ={pok_defense}    
        Pokemon Health  ={pok_health}   

        Instance Variables:
        Pokemon Name={pok_name}
        Pokemon Level  ={pok_level}    
        Pokemon Weak Against ={pok_weak}    
        Pokemon Strong Against  ={pok_strong}

        Boosts:
        Health Boost = {health_boost}
        Attack Boost = {attack_boost}
        Defense Boost = {defense_boost}
        Evolve = {evolve}

        """.format(pok_type=self.p_type, pok_attack=self.attack, pok_defense=self.defense, pok_health=self.health, \
            pok_name=self.name, pok_level=self.level, pok_weak=self.weak, pok_strong=self.strong, \
            health_boost=self.health_boost, attack_boost=self.attack_boost, defense_boost=self.defense_boost, evolve=self.evolve)

        return obj_blueprint
        #return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def __init__(self, name,level = 5):
        super().__init__(name, level)
        self.weak = "Fire"
        self.strong = "Water"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def __init__(self, name,level = 5):
        super().__init__(name, level)
        self.weak = "Dark"
        self.strong = "Psychic"

    def update(self):
        super().update()
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3

class Fire_Pokemon(Pokemon):
    p_type = "Fire"

    def __init__(self, name,level = 5):
        super().__init__(name, level)
        self.weak = "Water"
        self.strong = "Grass"

    def update(self):
        super().update()
        

class Flying_Pokemon(Pokemon):
    p_type = "Flying"

    def __init__(self, name,level = 5):
        super().__init__(name, level)
        self.weak = "Electric"
        self.strong = "Fighting"

    def update(self):
        super().update()


Normal = Pokemon("Pikachu")
Grass = Grass_Pokemon("Chikarita")
Ghost = Ghost_Pokemon("Gengar")
Fire = Fire_Pokemon("Magneto")
Flying = Flying_Pokemon("Pigi")

# print(Normal)
# print(Grass)
# print(Ghost)
# print(Fire)
# print(Flying)

print(Grass.opponent())
print(Ghost.opponent())
print(Fire.opponent())
print(Flying.opponent())