import contacts_list
import sort_files


def main():

    print("Hello, I'm your personal helper. What can I do for you today?")
    while True:
        user_input = input("1. Work with contacts list\n2. Work with notes\n3. Sort your folders\n4. Help\n5. Exit\n")
        if user_input in ('exit', '5'):
            print('Bye!')
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
            while True:
                user_input2 = input('What do you want to do with contacts list?\n1. Load contacts list\n2. Save contacts list\n3. New contacts list\n\
4. View contact list\n5. Create contact\n6. Change/delete name of contact\n7. Change/delete contact information\n8. Search value in contacts\n\
9. Find contacts with birthdays between two dates\n10. Back\n')

                if user_input2 == '1':
                    current_contact_list = contacts_list.ContactList()
                    current_contact_list.load()
                    current_contact_list.print_contact_list()

                elif user_input2 == '2':
                    if current_contact_list:
                        current_contact_list.save_csv()
                        print('Contact list successfully saved!')
                    else:
                        print('You are not working with contacts list now. Please load or create new one.')

                elif user_input2 == '3':
                    list_name = input('Enter contact list name: ')
                    current_contact_list = contacts_list.ContactList(list_name)
                    print('New contact list created!')

                elif user_input2 == '4':
                    if current_contact_list.name:
                        current_contact_list.print_contact_list()
                    else:
                        print('You are not working with contacts list now. Please load or create new one.')

                elif user_input2 == '5':
                    if current_contact_list.name:
                        new_contact = contacts_list.Record()
                        if new_contact.name in current_contact_list.keys():
                            print('User name is occupied. Please try another name.')
                            continue
                        current_contact_list.add_contact(new_contact)
                        print('Contact successfully created!')
                    else:
                        print('You are not working with contacts list now. Please load or create new one.')

                elif user_input2 == '6':
                    current_contact_list.change_name()

                elif user_input2 == '7':
                    print(list(current_contact_list.keys()))
                    name_to_change = input('Choose the contact to change/delete: ')
                    if name_to_change not in current_contact_list.keys():
                        print('Name is not in contact list')
                        continue
                    current_contact_list[name_to_change].change_value()

                elif user_input2 == '8':
                    if current_contact_list.name:
                        find_value = input('Enter the value to find: ')
                        current_contact_list.find(find_value)
                    else:
                        print('You are not working with contacts list now. Please load or create new one.')

                elif user_input2 == '9':
                    if current_contact_list.name:
                        days_from = input('Enter the q-ty days from today to search from: ')
                        days_to = input('Enter the q-ty days from today to search to: ')
                        print(current_contact_list.birthdays(days_from, days_to))
                    else:
                        print('You are not working with contacts list now. Please load or create new one.')

                elif user_input2 == '10':
                    break

                else:
                    print('Please choose correct option.')

if __name__ == '__main__':
    main()