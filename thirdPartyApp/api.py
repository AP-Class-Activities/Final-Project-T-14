""" Main Class """ #===============================================================

class User:
    def __init__(self, fName, lName, phone, email, password):
        self.__first_name = fName
        self.__last_name = lName
        self.__phone_numer = phone
        self.__email = email
        self.__password = password

    @property
    def fName(self):
        return self.__first_name

    @fName.setter
    def fName(self,value): 
        self.__first_name = value

    @property
    def lName(self):
        return self.__last_name

    @lName.setter
    def lName(self, value):
        self.__last_name = value

    @property
    def phone(self):
        return self.__phone_numer

    @phone.setter
    def phone(self, value):
        self.__phone_numer = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    def __str__(self) -> str:
        return self.__first_name + " " + self.__last_name


# ======================================================================
""" Customer Inheritance class """ # ===================================

class customer(User):
    def __init__(self, id_customer, username, card, basket, history, distance):
        self.__id = id_customer
        self.__username = username
        self.__card = card
        self.__basket = basket
        self.__history = history
        self.__distance = distance

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def uname(self):
        return self.__username
    
    @uname.setter
    def uname(self, value):
        self.__username = value

    @property
    def card(self):
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value

    @property
    def basket(self):
        return self.__basket

    @basket.setter
    def basket(self, value):
        self.__basket = value

    @property
    def history(self):
        return self.__history

    @history.setter
    def history(self, value):
        self.__history = value

    @property
    def comments(self):
        return self.__comments
    
    @comments.setter
    def comments(self, value):
        self.__comments = value

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
        self.__distance = value

    def __str__(self):
        return self.__username + "( " + self.__first_name + " " + self.__last_name + " )"

# ================================================================
""" Seller Inheritance class """ # ===============================






# ================================================================
""" stuff Inheritance class """ # ================================

class stuff:
    def __init__(self, stuff_id, s_id, name, price, specification):
        self.__stuff_id = stuff_id
        self.__s_id = s_id
        self.__name = name
        self.__price = price
        self.__specification = specification

    @property
    def stuffId(self):
        return self.__stuff_id

    @stuffId.setter
    def stuffId(self, value):
        self.__stuff_id = value

    @property
    def sellerId(self):
        return self.__s_id

    @sellerId.setter
    def sellerId(self, value):
        self.__s_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value




# =================================================================

