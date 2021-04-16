import ProjectHelper.contacts_list
import ProjectHelper.sort_files
import ProjectHelper.mynote
from datetime import datetime

def log(action):

    current_time = datetime.strftime(datetime.now(), '%H:%M:%S')
    message = f'[{current_time}] {action}'
    print('_'*100)
    print(message)
    print('‾'*100)
    with open('logs.txt', 'a') as file:
        file.write(f'{message}\n')

def readme():
    print('''This is the helper with the functions:
1. Create and work with Contacts lists.
2. Create and work with the notes.
3. Sorting files in the folders.

You can choose your options in the console.
Thank you for using our Helper.''')
        
def main():
    
    log("Hello, I'm your personal helper. What can I do for you today?")
    while True:
        print('_'*100)
        user_input = input(f"1. Work with contacts list\n2. Work with notes\n3. Sort your folders\n4. Help\n5. Exit\n{'‾'*100}\n")

        if user_input in ('exit', '5'):
            log('Bye!')
            break
        elif user_input == '4':
            readme()
        elif user_input == '3':
            ProjectHelper.sort_files.main()
        elif user_input == '2':
            n = ProjectHelper.mynote.NoteList()
            while True:
                print('_'*100)
                user_input2 = input(f'What do you want to do with notes?\n1. Create new note\n2. Change note info\n\
3. View notes\n4. Delete note\n5. Find note by tag\n6. Find value in notes \n7. Save changes\n\
8. Back\n{"‾"*100}\n')
                if user_input2 == '1':
                    name = input('Enter the note name: ')
                    data = input('Enter your note: ')
                    tags = input('Enter your tags separated by " ": ')
                    new_note = ProjectHelper.mynote.Note(name, data, tags)
                    n.add_note(new_note)
                    log('Note has been created!')
                    
                elif user_input2 == '2':
                    n.print_notelist()
                    name_note_to_change = input('Choose the name of the note to change: ')
                    index_note = 0
                    index_flag = False
                    for note in n.data:
                        if note.name == name_note_to_change:
                            index_flag = True
                            break
                        index_note += 1
                    if not index_flag:
                        print('Note with this name does not exist')
                        continue
                        
                    while True:
                        print('_'*100)
                        user_input3 = input(f'What exactly do you want to change?\n1. Change name\n2. Change note\n\
3. Change tag\n4. Add tag\n5. Back\n{"‾"*100}\n')
                        if user_input3 == '1':
                            name_change = input('Enter new name: ')
                            n.data[index_note].change_name(name_change)
                        elif user_input3 == '2':
                            note_change = input('Enter new note: ')
                            n.data[index_note].change_data(note_change)
                        elif user_input3 == '3':
                            n.data[index_note].change_tag()
                        elif user_input3 == '4':
                            new_tag = input('Enter new tag: ')
                            n.data[index_note].add_tag(new_tag)
                        elif user_input3 == '5':
                            break
                        else:
                            print('Please choose correct option')
                            
                elif user_input2 == '3':
                    n.print_notelist()
                elif user_input2 == '4':
                    n.print_notelist()
                    name_del = input('Enter the name of the note to delete: ')
                    n.delete_note(name_del)
                elif user_input2 == '5':
                    tag_to_find = input('Enter the tag to find in the notes: ')
                    n.find_tags(tag_to_find)
                elif user_input2 == '6':
                    name_to_find = input('Enter the value to find in the notes: ')
                    n.find(name_to_find)    
                elif user_input2 == '7':
                    n.save_notelist()
                    log('Notes has been saved!')
                elif user_input2 == '8':
                    break
                else:
                    print('Please choose correct option')

        elif user_input == '1':
            active_list_flag = False
            while True:
                print('_'*100)
                user_input2 = input(f'What do you want to do with contacts list?\n1. Load contacts list\n2. Save contacts list\n3. New contacts list\n\
4. View contact list\n5. Create contact\n6. Change/delete name of contact\n7. Add/change/delete contact information\n8. Search value in contacts\n\
9. Find contacts with birthdays between two dates\n10. Back\n{"‾"*100}\n')
                
                if user_input2 == '1':
                    current_contact_list = ProjectHelper.contacts_list.ContactList()
                    current_contact_list.load()
                    active_list_flag = True

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
                    current_contact_list = ProjectHelper.contacts_list.ContactList(list_name)
                    active_list_flag = True
                    log('New contact list created!')

                elif user_input2 == '4':
                    if active_list_flag:
                        current_contact_list.print_contact_list()
                    else:
                        log('You are not working with contacts list now. Please load or create new one.')

                elif user_input2 == '5':
                    if active_list_flag:
                        new_contact = ProjectHelper.contacts_list.Record()
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
                        print('_'*100)    
                        add_or_change = input(f'What exactly do you want to do?\n1. Add new info\n2. Change/delete info\n3. Back\n{"‾"*100}\n')
                        if add_or_change == '1':
                            print('_'*100)
                            what_to_add = input(f'What exactly do you want to add?\n1. Phone\n2. Address\n3. Mail\n4. Birthday\n5. Back\n{"‾"*100}\n')
                            if what_to_add == '1':
                                current_contact_list[name_to_change].add_value('phone')
                            elif what_to_add == '2':
                                current_contact_list[name_to_change].add_value('address')
                            elif what_to_add == '3':
                                current_contact_list[name_to_change].add_value('mail')
                            elif what_to_add == '4':
                                if not current_contact_list[name_to_change]['birthday']:
                                    current_contact_list[name_to_change].add_birthday()
                                else:
                                    log('Birthday has been already added')
                            elif what_to_add =='5':
                                pass
                            else:
                                log('Please choose correct option.')
                        
                        elif add_or_change == '2':
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
                        current_contact_list.birthdays(days_from, days_to)
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
