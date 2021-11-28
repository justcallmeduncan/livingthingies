class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Pet):
    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food
        
       
    

d = Dog("Tim",34,"meat")

# d.bark()
#print(d.name)
#d.name = "Tom"
print(d.name)
print(d.age)
print(d.food)