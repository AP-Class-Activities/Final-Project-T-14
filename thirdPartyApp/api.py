class Person:
    def __init__(self, username, fName, lName, email, password, phone, address):
        self.__username = username
        self.__first_name = fName
        self.__last_name = lName
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.__address = address

    @property
    def uName(self):
        return self.__username