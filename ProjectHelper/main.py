import contacts_list
import sort_files
from datetime import datetime

def log(action):

    current_time = datetime.strftime(datetime.now(), '%H:%M:%S')
    message = f'[{current_time}] {action}'

    print(message)
    with open('logs.txt', 'a') as file:
        file.write(f'{message}\n')
        
def main():
    
    log("Hello, I'm your personal helper. What can I do for you today?")
    while True:
        user_input = input("1. Work with contacts list\n2. Work with notes\n3. Sort your folders\n4. Help\n5. Exit\n")
        if user_input in ('exit', '5'):
            log('Bye!')
            break
        elif user_input == '4':
            with open('.\README.md','r') as fh:
                all_file = fh.read()
                print(all_file)
        elif user_input == '3':
            sort_files.main()
        elif user_input == '2':
            pass
        elif user_input == '1':
            active_list_flag = False
            while True:
                user_input2 = input('What do you want to do with contacts list?\n1. Load contacts list\n2. Save contacts list\n3. New contacts list\n\
4. View contact list\n5. Create contact\n6. Change/delete name of contact\n7. Change/delete contact information\n8. Search value in contacts\n\
9. Find contacts with birthdays between two dates\n10. Back\n')

                if user_input2 == '1':
                    current_contact_list = contacts_list.ContactList()
                    current_contact_list.load()
                    active_list_flag = True
                    log('Contact list successfully loaded!')

                elif user_input2 == '2':
                    if active_list_flag:
                        current_contact_list.save_csv()
                        log('Contact list successfully saved!')
                    else:
                        log('You are not working with contacts list now. Please load or create new one.')

                elif user_input2 == '3':
                    if active_list_flag:
                        user_input3 = input('Do you want to save current contact list? (yes|no): ')
                        if user_input3 == 'yes':
                            current_contact_list.save_csv()
                            log('Contact list successfully saved!')

                    list_name = input('Enter contact list name: ')
                    current_contact_list = contacts_list.ContactList(list_name)
                    active_list_flag = True
                    log('New contact list created!')

                elif user_input2 == '4':
                    if active_list_flag:
                        current_contact_list.print_contact_list()
                    else:
                        log('You are not working with contacts list now. Please load or create new one.')

                elif user_input2 == '5':
                    if active_list_flag:
                        new_contact = contacts_list.Record()
                        if new_contact.name in current_contact_list.keys():
                            print('User name is occupied. Please try another name.')
                            continue
                        current_contact_list.add_contact(new_contact)
                        log('Contact successfully created!')
                    else:
                        log('You are not working with contacts list now. Please load or create new one.')

                elif user_input2 == '6':
                    if active_list_flag:
                        current_contact_list.change_name()
                    else:
                        log('You are not working with contacts list now. Please load or create new one.')

                elif user_input2 == '7':
                    if active_list_flag:
                        print(list(current_contact_list.keys()))
                        name_to_change = input('Choose the contact to change/delete: ')
                        if name_to_change not in current_contact_list.keys():
                            log('Name is not in contact list')
                            continue
                        current_contact_list[name_to_change].change_value()
                    else:
                        log('You are not working with contacts list now. Please load or create new one.')


                elif user_input2 == '8':
                    if active_list_flag:
                        find_value = input('Enter the value to find: ')
                        current_contact_list.find(find_value)
                    else:
                        log('You are not working with contacts list now. Please load or create new one.')

                elif user_input2 == '9':
                    if active_list_flag:
                        days_from = input('Enter the q-ty days from today to search from: ')
                        days_to = input('Enter the q-ty days from today to search to: ')
                        log(current_contact_list.birthdays(days_from, days_to))
                    else:
                        log('You are not working with contacts list now. Please load or create new one.')

                elif user_input2 == '10':
                    break

                else:
                    log('Please choose correct option.')
        else:
            log('Please choose correct option.')

if __name__ == '__main__':
    main()