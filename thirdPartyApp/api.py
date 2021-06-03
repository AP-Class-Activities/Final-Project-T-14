class Person:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def id(self):
        pass
class customer(Person):
    def __init__(self,card,basket,username):
        self.card = card
        self.basket = basket



class new:
    def __init__(self, name):
        self.__name = name