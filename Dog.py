class Dog:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def barks(self):
    print(f"{self.name} barked at night")


  def plays(self):
    print(f"{self.name} played with a cat")

  def calAge(self):
    print(f"{self.name} is {self.age} years old")

mydog1 = Dog('Billie', 6)
mydog1.barks()
mydog1.calAge()