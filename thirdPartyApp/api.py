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