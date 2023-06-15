class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.firstName = first_name
        self.lastName = last_name
        self.treats = treats
        self.petFood = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.sound()
        return self 

class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        self.noise = noise
    
    def sleep(self):
        self.energy += 25
        print(f"Feeding {self.name}!")
    
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} just ate")
    
    def play(self):
        self.health += 5
        print(f"{self.name} played!")
    
    def sound(self):
        print(self.noise)

pet1 = Pet("Izzy", "dog", "sit", "woof")

ninja1 = Ninja("Matt","Abbott", "peanutbutter", "chimken", pet1)

ninja1.bathe()


