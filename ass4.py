class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def introduce(self):
        print(f"Welcome {self.name}, confirm you are {self.age} years old and are {self.gender}.")

#creating an instance of the person class
std = Person("Keith",12,"Male")
#calling the introduce method
std.introduce()
