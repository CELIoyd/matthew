class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Dog. My name is {self.name}. I am {self.age} years old.") 

    def make_sound(self):
        print("Barrk")



cat1 = Cat("Zane", 9)
dog1 = Dog("Window", 8)


for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()

               
