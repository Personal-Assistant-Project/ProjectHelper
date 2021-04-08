from collections import UserDict, UserString, UserList
from datetime import datetime

class ContactList(UserDict):
    
    def add_contact(self, record):
        self.data[record.name] = {}
        self.data[record.name]['address'] = record.address
        self.data[record.name]['phone'] = record.phone
        self.data[record.name]['mail'] = record.mail
        self.data[record.name]['birthday'] = record.birthday

class Birthday(UserString):
    
    @property
    def data(self):
        return self.__data
        
    @data.setter
    def data(self, new_value):

        try:
            self.year = int(new_value[6:])
            self.month = int(new_value[3:5])
            self.day = int(new_value[:2])
            self.date = datetime(self.year, self.month, self.day)
            self.__data = new_value
        except ValueError:
            self.__data = ''
            print('Birthday input is not correct. Should be in format: DD/MM/YYYY')

class Address(UserList):
    
    def __init__(self, value):
        self.data = [value]

class Mail(UserList):
    
    def __init__(self, value):
        self.data = [value]

class Phone(UserList):
    
    def __init__(self, value):
        self.data = [value]
    
class Record:
    
    def __init__(self, name, address = '', phone = '', mail = '', birthday = ''):
        self.name = name
        self.address = Address(address)
        self.phone = Phone(phone)
        self.mail = Mail(mail)
        self.birthday = Birthday(birthday)

    def add_phone(self, value):
        self.phone.data.append(value)
        
    def del_phone(self):
        self.phone.clear()


a = ContactList()

b = Record('Ivan', address = 'Mazepy 28', phone = '0936795412', mail = 'ivan75@gmail.com', birthday = '13/02/2000')

a.add_contact(b)
b.add_phone('0674712255')


print(a.data)
