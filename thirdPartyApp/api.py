class Person:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password 

    def id(self):
        pass
class customer(Person):
    def __init__(self,card,basket,username,id_customer,comments,history):
        self.card = card
        self.basket = basket
        self.username = username
        self.id_customer = id_customer
        self.history = history
        self.comments = comments

class new:
    def __init__(self, name):
        self.__name = name


class RMB:
    def __init__(self) -> None:
        pass