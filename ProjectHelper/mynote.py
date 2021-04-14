from datetime import datetime
import csv


class Note:
    
    def __init__(self, name, data, tags, current_time = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')):
        self.name = name
        self.data = data
        self.tags = tags.split()
        self.current_time = current_time
        
    def add_tag(self, tag):
        self.tags.append(tag)

    def change_name(self, name):
        if not name:
            print('Note name cannot be empty')
        else:
            self.name = name
            self.current_time = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')
            
    def change_data(self, data):
        self.data = data
        self.current_time = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')        
    
    def change_tag(self):
        print(self.tags)
        user_input = input('Choose tag to change: ')
        if user_input in self.tags:
            user_input2 = input('Enter new tag: ')
            index_to_change = self.tags.index(user_input)
            self.tags[index_to_change] = user_input2
            self.current_time = datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S')        
            print('Tag successfully changed!')
            
    def print_note(self):
        print("|{:<20}|{:^15}|{:^25}|{}|".format(self.current_time,self.name, ' '.join(self.tags), self.data))
        print(' {:‾^105}'.format('')) 

class NoteList:
    
    def __init__(self):
        self.data = []
        self.load_notelist()
        
    def add_note(self, note):
        self.data.append(note)
        
    def delete_note(self, note_name):
        for note in self.data:
            if note.name == note_name:
                self.data.remove(note)
                break
        
    def find(self, search_value):
        find_flag = False    
        for i in self.data:
            if search_value in i.name or search_value in i.data:
                i.print_note()
                find_flag = True
        if not find_flag:
            print('Data was not founded in the notes ')
    
    def find_tags(self, search_value):
        find_flag = False
        for i in self.data:
            if search_value in i.tags:
                i.print_note()
                find_flag = True
                
        if not find_flag:
            print('Tag was not founded in the notes')
                
    def save_notelist(self):
        with open('notes.csv', 'w', newline='') as file:
            field_names = ['time', 'name', 'tags', 'note']
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            dict_to_write = {}
            for note in self.data:
                dict_to_write['time'] = note.current_time
                dict_to_write['name'] = note.name
                dict_to_write['tags'] = ' '.join(note.tags)
                dict_to_write['note'] = note.data
                writer.writerow(dict_to_write)
                
    def load_notelist(self):
        try:
            with open('notes.csv', 'r', newline = '') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    new_note = Note(row['name'], row['note'], row['tags'], row['time'])
                    self.data.append(new_note)
        except FileNotFoundError:
            self.data = []
                
    def print_notelist(self):
        print(' {:_^105}'.format(''))
        for note in self.data:
            note.print_note()
