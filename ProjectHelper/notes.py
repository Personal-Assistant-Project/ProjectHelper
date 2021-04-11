import os
import os.path


class NoteList:
    
    
    def add_note(self):
        user_inp_subj = input('Subject: ' )
        user_inp_text = input('Text: ')
        user_inp_dict = {user_inp_subj:user_inp_text}

        with open('note.txt', 'a') as note_add:
            for item in user_inp_dict.items():
                note_add.write('%s: %s \n' % (item[0], item[1]))
                print('Done')

                
    def find_teg(self):
        need_tegs = input('Enter teg you want to find: ')
        count = 0
        with open('note.txt', 'r') as find_note_tegs:
            find_note_tegs = find_note_tegs.readlines()
            for i in iter(find_note_tegs):
                if need_tegs in i:
                    print(i)
                    count += 1
            if count == 0:
                print('This teg is not in the notes')

                
    def change_notes(self):
        with open('note.txt', 'r+') as f:
            old_text = input('Enter text you want to change in the notes: ')
            new_text = input('Please enter new text: ')
            newline=[]
            
            for word in f.readlines():
                newline.append(word.replace(old_text, new_text))

        with open("note.txt","r+") as f:
            for line in newline:
                f.writelines(line)
                
    
    def sort_notes(self):        
        with open("note.txt", "r+") as f:
            lines = f.readlines()
            lines.sort()        
            f.seek(0)
            f.writelines(lines)

            
notelist = NoteList()
notelist.find_teg()
