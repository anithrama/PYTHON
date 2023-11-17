class animal:
    def speak(self):
        print("Animal Speaking")
class Dog(animal):
    def bark(self):
        super().speak()
        print("Dog barking")

class Cat(animal):
    def meaw(self):
        super().speak()
        print("cat meawing")

class Cow(animal):
    def ambeee(self):
        super().speak()
        print("cow ambee")
dog=Dog()
cat=Cat()
cow=Cow()

dog.bark()
cat.meaw()
cow.ambeee()