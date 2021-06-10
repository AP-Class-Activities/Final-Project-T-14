""" Main Class """ #===============================================================

class User:
    def __init__(self, fName, lName, phone, email, password):
        self.__first_name = fName
        self.__last_name = lName
        if len(phone) < 10:
            raise ValueError("Wrong number!")
        elif phone[0:3] != "+98":
            if phone[0] == "0":
                phone = "+98" + phone[1:]
            elif phone[0] != "0":
                phone = "+98" + phone
            else:
                raise ValueError("Wrong number!")
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
        if len(value) < 10:
            raise ValueError("Wrong number!")
        elif value[0:3] != "+98":
            if value[0] == "0":
                value = "+98" + value[1:]
            elif value[0] != "0":
                value = "+98" + value
        else:
            raise ValueError("Wrong number!")
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
        self.__distance = distance  # """ fasel anbar ta moshtari """

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
        if value < 0:
            ValueError("")
        else:
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

class seller(User):
    def __init__(self, id_seller, address, offer_list, income, sell_counter, cost, distance, suspension):
        self.__id = id_seller
        self.__address = address
        self.__offer_list = offer_list
        self.__income = income
        self.__sell_counter = sell_counter
        self.__cost = cost
        self.__distance = distance  # """ fasel foroshande ta anbar """
        self.__suspension = suspension
        
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
        
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def offer_list(self):
        return self.__offer_list

    @offer_list.setter
    def offer_list(self, value):
        self.__offer_list = value

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value):
        self.__income = value

    @property
    def sell_counter(self):
        return self.__sell_counter

    @sell_counter.setter
    def sell_counter(self, value):
        if value < 0:
            raise ValueError("sell_counter should be positive")
        else:
            self.__sell_counter = value
    
    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        if value < 0:
            print("cost should be positive")
        else:
            self.__cost = value

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
        self.__distance = value

    @property
    def suspension(self):
        return self.__suspension

    @suspension.setter
    def suspension(self, value):
        if value is not True or False:
            print("suspension should be True or False")
        else:
            self.__suspension = value
    
    def __str__(self):
        return "seller--> (%s)"%(super(seller,self).__str__())

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

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, value):
        self.__specification = value

# =================================================================

