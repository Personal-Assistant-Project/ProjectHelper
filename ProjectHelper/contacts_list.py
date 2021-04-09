from collections import UserDict, UserString, UserList
from datetime import datetime, timedelta

class ContactList(UserDict):
    
    def add_contact(self, record):
        self.data[record.name] = record.data
        
    #calculate contacts with birthdays from days_from to days_to
    def birthdays(self, days_from, days_to):
    
        if not(isinstance(days_from, int) and isinstance(days_to, int)) or days_from < 0 or days_to < 0 or days_to < days_from:
            return f'Input is not correct. Days should be integer and days from should be less then days to'
    
        date_now = datetime.now()
        delta_from = timedelta(days = days_from)
        delta_to = timedelta(days = days_to)
        
        #dates from - to in datetime
        date_from = date_now + delta_from
        date_to = date_now + delta_to
        
        finded_contacts = f'Finded contacts with birthdays in range:\n'
        for key, value in self.data.items():
            
            #find correct birthday date between from and to
            if date_from.month < value['birthday'].month:
                birthday_date = value['birthday'].date.replace(year = date_now.year)
            elif date_from.month == value['birthday'].month:
                if date_from.day <= value['birthday'].day:
                    birthday_date = value['birthday'].date.replace(year = date_now.year)
                else:
                    birthday_date = value['birthday'].date.replace(year = date_now.year + 1)
            else:
                birthday_date = value['birthday'].date.replace(year = date_now.year + 1)
                
            if date_from < birthday_date < date_to:
                finded_contacts += f'{key}: {self.data[key]}\n'
                
        return finded_contacts

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
            print(f'Birthday input is not correct. Should be in format: DD.MM.YYYY')
    
class Record(UserDict):
    
    #creating Record dict with all values
    def __init__(self):
        self.data = {}
        self.add_name()
        self.add_value('address')
        self.add_value('phone')
        self.add_value('mail')
        self.add_birthday()
        
    #adding name attribute to the Record
    def add_name(self):
        user_input = input('Enter your name please: ')
        self.name = user_input
            
    
    #adding phone, mail and address to the Record
    def add_value(self, value):
        while True:
           
            user_input = input(f'Enter the {value} please: ')
                    
            if value == 'phone':
                if not self.__phone_check(user_input):
                    continue
            
            if value == 'mail':
                if not self.__mail_check(user_input):
                    continue
            
            if value not in self.data.keys():
                self[value] = [user_input]
            else:
                self[value].append(user_input)

            add_more = input(f'Do you want to enter another {value}? ')
            if add_more == 'yes':
                continue
            else:
                break
    
    #phone check
    def __phone_check(self, phone):
        if (phone[:3] == '380' and len(phone) == 12) or not phone:
            return True
        else:
            print('Phone number is not correct. Should start from 380 and have 12 digits')
            return False
    
    #mail check
    def __mail_check(self, mail):
        #if mail[:3] == '380' and len(mail) == 12:
        return True
        #else:
        #    print('Mail is not correct.')
        #    return False
    
    #birthday adding
    def add_birthday(self):
        while True:
           
            user_input = input('Enter the birthday please in format "DD.MM.YYYY": ')
            self.data['birthday'] = Birthday(user_input)
            
            if self.data['birthday'] or not user_input:
                break
    
    
a = ContactList()

b = Record()

a.add_contact(b)
#a.add_contact(c)


print(a)
