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
    def __init__(self, id_customer, username, card, basket, history, comments):
        self.__id = id_customer
        self.__username = username
        self.__card = card
        self.__basket = basket
        self.__history = history
        self.__comments = comments
	def buy(self,stuff,price):
        	if self.card < price:
        		print('first charge your card')
        	else:
         		self.card-=price
         		history+=stuff
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

    def __str__(self):
        return self.__username + "( " + self.__first_name + " " + self.__last_name + " )"

# ================================================================
""" Seller Inheritance class """ # ===============================


class seller(User):
    def __init__(self, fName= "first name", lName= "last_name", phone, email, password,     id, address= "tehran", offer_list=[], income=0 , sell_counter=0, cost=0, suspension=False):
        super(seller, self).__init__(fName, lName, phone, email, password)
        self.__id= id
        self.__address= address
        self.__offer_list= offer_list
        self.__income= income
        self.__sell_counter= sell_counter
        self.__cost= cost
        self.__suspension= suspension
        
        
        def selling(self):
            return self.income += self.cost and self.sell_counter += 1
        
        
        
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
            seld.__address = value

        
        @property
        def offer_list(self):
            return self.__offer_list

        @offer_list.setter
        def offer_list(self, value):
            return self.__offer_list

        
        @property
        def income(self):
            return self.__income

        @income.setter
        def income(self, value):
            return self.__income

        
        @property
        def sell_counter(self):
            return self.__sell_counter

        @sell_counter.setter
        def sell_counter(self, value):
            if self.sell_counter < 0:
                print("sell_counter should be positive")
            else:
                return self.__sell_counter

        
        @property
        def cost(self):
            return self.__cost

        @cost.setter
        def cost(self, value):
            if self.cost < 0:
                print("cost should be positive")
            else:
                return self.__cost


        @property
        def suspension(self):
            return self.__suspension

        @suspension.setter
        def suspension(self, value):
            if self.suspension is True or False:
                return self.__self.suspension
            else:
                print("suspension should be True or False")
        

            
                
        def __str__(self):
            return "seller--> (%s)"%(super(seller,self).__str__())

# ================================================================
""" stuff Inheritance class """ # ================================






# =================================================================