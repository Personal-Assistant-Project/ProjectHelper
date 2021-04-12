from collections import UserDict, UserString, UserList
from datetime import datetime, timedelta
from re import fullmatch
import csv
import copy

class ContactList(UserDict):

    def __init__(self, name='new_contact_list'):
        self.name = name
        self.data = {}

    def add_contact(self, record):
        self.data[record.name] = record

    #find value in ContactList
    def find(self, find_value):

        finded_names = ''
        
        for key, value in self.data.items():
            if find_value in key:
                finded_names += f'{key}: {self.data[key]}\n'
                continue
            
            search_values = value['address'] + value['phone'] + value['mail'] + [value['birthday']]

            for i in search_values:
                if find_value in i:
                    finded_names += f'{key}: {self.data[key]}\n'
                    break
                
        if not finded_names:
            print(f'No value {find_value} found')
        else:
            print(finded_names)

    #change name in ContactList
    def change_name(self):
        while True:
            user_input = input('Please enter name to rename: ')
            if user_input not in self.data.keys():
                user_input2 = input('Entered name is not in the contact book.\n1. Try again\n2.return to previous menu?\n')
                if user_input2 == '1':
                    continue
                else:
                    break
            else:
                new_input = input('Enter new name or leave empty to delete contact: ')
                self.data[new_input] = self.data.pop(user_input)
                if new_input:
                    self.data[new_input].name = new_input
                break

            
       
    #calculate contacts with birthdays from days_from to days_to
    def birthdays(self, days_from, days_to):

        try:
            days_from = int(days_from)
            days_to = int(days_to)
        except:
            return f'Input is not correct. Days should be integer'
    
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

    #save contact list
    def save_csv(self):
        user_input = self.name
        with open(f'{user_input}.csv', 'w', newline='') as file:
            field_names = ['name', 'phone', 'address', 'mail', 'birthday']
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            for key,value in self.data.items():
                dict_to_write = copy.deepcopy(value)
                dict_to_write['name'] = key
                dict_to_write['phone'] = '&'.join(dict_to_write['phone'])
                dict_to_write['phone'] = dict_to_write['phone'].replace("'",'')
                dict_to_write['address'] = '&'.join(dict_to_write['address'])
                dict_to_write['address'] = dict_to_write['address'].replace("'",'')
                dict_to_write['mail'] = '&'.join(dict_to_write['mail'])
                dict_to_write['mail'] = dict_to_write['mail'].replace("'",'')
                writer.writerow(dict_to_write)

    def load(self):
        user_input = input('Enter the name of your Contact List: ')
        self.name = user_input
        with open(f'{user_input}.csv', newline='') as file:
            reader = csv.DictReader(file)     
            for row in reader:
                key = row.pop('name')
                loaded_record = Record(name = key, phone = row['phone'].split('&'), address = row['address'].split('&'), mail = row['mail'].split('&'), birthday = Birthday(row['birthday']))
                self.data[key] = loaded_record

    def print_contact_list(self):
        print(f'Contact list: {self.name}')
        print(' {:_^105}'.format(''))
        counter = 0
        
        for i in self.data:
            print("|{:<10}|{:^27}|{:^27}|{:^27}|{:>10}|".format(i[:10],('/ '.join(self.data[i]['phone']))[:27],('/ '.join(self.data[i]['address']))[:27],('/ '.join(self.data[i]['mail']))[:27],self.data[i]['birthday'].data))
            counter += 1
            if not counter % 10:
                print(' {:‾^105}'.format(''))
                input('Press any key to continue')
                print(' {:_^105}'.format(''))
                
        print(' {:‾^105}'.format('')) 

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
            if new_value:
                print(f'Birthday input is not correct. Should be in format: DD.MM.YYYY')
    
class Record(UserDict):
    
    #creating Record dict with all values
    def __init__(self, name = '', phone = '', address = '', mail = '', birthday = 'no_data'):
        self.data = {}
        if not name:
            self.add_name()
        else:
            self.name = name

        if not phone:
            self.add_value('phone')
        else:
            self.data['phone'] = phone

        if not address:
            self.add_value('address')
        else:
            self.data['address'] = address

        if not mail:
            self.add_value('mail')
        else:
            self.data['mail'] = mail

        if birthday == 'no_data':
            self.add_birthday()
        else:
            self.data['birthday'] = birthday
        
    #adding name attribute to the Record
    def add_name(self):
        user_input = input('Enter contact name please: ')
        self.name = user_input
            
    
    #adding phone, mail and address to the Record
    def add_value(self, value):
        while True:
           
            user_input = input(f"Enter the {value} please (If you don't want to enter {value}, leave empty): ")
                    
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

            if not user_input:
                add_more = 'no'
            else:
                add_more = input(f'Do you want to enter another {value}? (yes|no): ')
                
            if add_more == 'yes':
                continue
            else:
                break
    
    #phone check
    def __phone_check(self, phone):

        PHONE_CHECK = '[+]?380(93|67|63|50|95|66|97|68|73|96|98|99)\d{7}'

        if fullmatch(PHONE_CHECK, phone) or not phone:
            return True
        else:
            print('Phone number is not correct. Should start from +380 or 380, have correct operator number and 12 digits')
            return False
    
    #mail check
    def __mail_check(self, mail):

        MAIL_CHECK = '[a-zA-Z0-9_]{2,15}[@][a-z]{1,10}\.[a-z]{2,4}'

        if fullmatch(MAIL_CHECK, mail) or not mail:
            return True
        else:
            print('Mail is not correct.')
            return False
    
    #birthday adding
    def add_birthday(self):
        while True:
           
            user_input = input('Enter the birthday please in format "DD.MM.YYYY"(If you do not want to enter birthday, leave empty): ')
            self.data['birthday'] = Birthday(user_input)
            
            if self.data['birthday'] or not user_input:
                break
    
    #change any value in Record except name
    def change_value(self):
        
        CORRECT_INPUT = ('1', 'phone', '2', 'address', '3', 'mail', '4', 'birthday','5','back')

        while True:
            user_input = input("What value do you want to change/delete?\n1. Phone\n2. Address\n3. Mail\n4. Birthday\n5. Back\n")

            if user_input  not in CORRECT_INPUT:
                print('Please choose correct option from the list: ')
                continue
            elif user_input in ('5', 'back'):
                break
            elif user_input in ('4', 'birthday'):
                self.add_birthday()
                break
            else:

                if user_input in ('1', 'phone'):
                    value = 'phone'
                elif user_input in ('2','address'):
                    value = 'address'
                else:
                    value = 'mail'

                print(self.data[value])

                user_input = input(f'Choose the number of {value} to change/delete. If you want to delete all values, type "clear": ')

                if user_input == 'clear':
                    self.data[value].clear()
                    break

                data_input = input(f'Enter the correct {value} or leave empty if you want to delete {value}: ')

                if value == 'phone':
                    if not self.__phone_check(data_input):
                        continue
            
                if value == 'mail':
                    if not self.__mail_check(data_input):
                        continue
                if data_input:
                    self.data[value][int(user_input)-1] = data_input
                else:
                    self.data[value].pop(int(user_input)-1)
                break
