class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return (self.weight / self.age * 10)
    
    def fight(self, other_dog):
        self.other_dog = other_dog
    
        my_power = self.run_speed() * self.weight

        other_power = other_dog.run_speed() * other_dog.weight  

        if my_power > other_power:
                print(f"{my_dog.name} is the winner!")
        else:
                print(f"{my_dog.name} loose!")