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

    def find_tegs(self):
        need_tegs = input('what tegs? ')
        with open('note.txt', 'r') as find_note_tegs:
            find_note_tegs = find_note_tegs.readlines()
            for i in iter(find_note_tegs):
                if need_tegs in i:
                    print(i)

    def change_note(self):

        with open('note.txt', 'r+') as f:
            old_text = input('what text you want change in note? ')
            new_text = input('for what text you want change in note? ')
            newline=[]
            
            for word in f.readlines():
                newline.append(word.replace(old_text, new_text))

        with open("note.txt","r+") as f:
            for line in newline:
                f.writelines(line)
                
    def sort_tegs(self):
        
        with open("note.txt", "r+") as f:
            lines = f.readlines()
            lines.sort()        
            f.seek(0)
            f.writelines(lines)

notelist = NoteList()
notelist.find_tegs()