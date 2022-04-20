class Human():
     def __init__(self, name):
         self.name = name

     def welcome_message(self):
          print(f'Hello, {self.name}')

     def method(self):
          print(f'You are Homosapiens {name}.')

     @staticmethod
     def staticmethod():
        print('Its static method.')

name = input("Write your name: ")
obj_name = Human(name)
obj_name.method()
obj_name.staticmethod()
