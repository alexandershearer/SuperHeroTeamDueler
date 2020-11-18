class Dog:
    def __init__(self, name):
        self.name = name
        print("dog initialized!")

#Creates a dog object
my_dog = Dog("Rex")
print(my_dog)
print(my_dog.name)