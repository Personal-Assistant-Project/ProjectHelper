import os
import shutil
import sys

GLOBAL_PATH = ''

# Folders to create
folders = ['archive', 'audio', 'documents', 'images', 'video', 'other']

# Extentions of known files
archive_ext = ['.7z', '.ace', '.arj', 'bz2', '.cab', '.cbr', '.d8t', '.deb', '.gz', '.gzip', '.gztar', '.jar',
               '.pak', '.php', '.pkg', '.rar', '.rpm', '.sh', '.sit', '.sitx', '.tar', '.tar-gz', '.tgz', '.xz', '.zip', '.zipx']
audio_ext = ['.aac', '.ac3', '.aif', '.aiff', '.amr', '.ape', '.asf', '.asx', '.au', '.aud', '.flac', '.iff', '.m3u', '.m3u8',
             '.m4a', '.m4b', '.m4p', '.m4r', '.mid', '.midi', '.mod', '.mp3', '.mpa', '.ogg', '.ra', '.ram', '.sib', '.wav', '.wm', '.wma']
docs_ext = ['.djvu', '.doc', '.docm', '.docx', '.dot', '.dotm', '.dotx', '.epub', '.fb2', '.ibooks', '.indd', '.key', '.mobi', '.mso', '.ods', '.odt',
            '.one', '.oxps', '.pages', '.pdf', '.pkg', '.pot', '.potm', '.potx', '.pps', '.ppsm', '.ppsx', '.ppt', '.pptm', '.pptx', '.ps', '.pub',
            '.rtf', '.sldm', '.vcard', '.vcf', '.txt', '.wpd', '.wps', '.xar', '.xlr', '.xls', '.xlsb', '.xlsm', '.xlsx', '.xlt', '.xltm', '.xltx', '.xps']
imgs_ext = ['.ai', '.bmp', '.cdd', '.cdr', '.dds', '.dng', '.eps', '.gbr', '.gif', '.iso', '.jpeg', '.jpg', '.kdc', '.mng', '.msp', '.pcx', '.pdd',
            'pdp', '.png', '.pot', '.ps', '.psb', '.psd', '.pspimage', '.raw', '.svg', '.tga', '.thm', '.tif', '.tiff', '.vsd', '.vst', '.wmf', '.xcf']
video_ext = ['.3g2', '.3gp', '.avi', '.f4v', '.flv', '.m4v', '.mkv', '.mod', '.mov', '.mp4', '.mpeg',
             '.mpg', '.mts', '.rm', '.rmvb', '.srt', '.swf', '.ts', '.vob', '.webm', '.wmv', '.yuv']

# Normalization of file names


def normalize(string):

    tr_map = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e', ord('є'): 'ye', ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'y',
              ord('і'): 'i', ord('ї'): 'yi', ord('й'): 'y', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r',
              ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'kh', ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'shch', ord('ы'): 'y',
              ord('ъ'): '', ord('ь'): '', ord('э'): 'e', ord('ю'): 'yu', ord('я'): 'ya', ord('ё'): 'yo', ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'G',
              ord('Д'): 'D', ord('Е'): 'E', ord('Є'): 'Ye', ord('Ж'): 'Zh', ord('З'): 'Z', ord('И'): 'Y', ord('І'): 'I', ord('Ї'): 'Yi', ord('Й'): 'Y', ord('К'): 'K',
              ord('Л'): 'L', ord('М'): 'M', ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P', ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T', ord('У'): 'U', ord('Ф'): 'F',
              ord('Х'): 'Kh', ord('Ц'): 'Ts', ord('Ч'): 'Ch', ord('Ш'): 'Sh', ord('Щ'): 'Shch', ord('Ы'): 'Y', ord('Ъ'): '', ord('Ь'): '', ord('Э'): 'E', ord('Ю'): 'Yu',
              ord('Я'): 'Ya', ord('Ё'): 'Yo'}

    normalized = []

    for c in string:
        if not c.isalpha() and not c.isdigit():
            c = '_'
            normalized.append(c)
        else:
            c = c.translate(tr_map)
            normalized.append(c)

    return ''.join(normalized)


# Folders creation
def create_folder(folders):
    for name in folders:
        directory = os.path.join(GLOBAL_PATH, name)
        try:
            os.stat(directory)
        except:
            os.mkdir(directory)


# Files move
def move_files(files_info):
    create_folder(folders)
    info = files_info.split(";")
    src = os.path.join(info[1], info[2]+info[3])
    destination = os.path.join(
        GLOBAL_PATH, info[0], normalize(info[2])+info[3])
    shutil.move(src, destination)
    try:
        os.rmdir(info[1])
    except OSError:
        pass


# Sort files in dirs
def sort_files(collection, path, nest_deep):
    for file in collection:
        name, ext = os.path.splitext(file)
        if ext.lower() in archive_ext:
            move_files(f'archive;{path};{name};{ext}')
        elif ext.lower() in audio_ext:
            move_files(f'audio;{path};{name};{ext}')
        elif ext.lower() in docs_ext:
            move_files(f'documents;{path};{name};{ext}')
        elif ext.lower() in imgs_ext:
            move_files(f'images;{path};{name};{ext}')
        elif ext.lower() in video_ext:
            move_files(f'video;{path};{name};{ext}')
        else:
            if os.path.isfile(os.path.join(path, file)):
                move_files(f'other;{path};{name};{ext}')


# Structures to find files
def grab_path(path, nest_deep=0):
    collection = []
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            grab_path(os.path.join(path, file), nest_deep + 1)
        else:
            collection.append(file)

    sort_files(collection, path, nest_deep)


def main():
    global GLOBAL_PATH
    while True:
        user_input = input('Do you want to sort current folder? (yes/no) ')
        if user_input.lower().strip() == 'yes':
            GLOBAL_PATH = os.getcwd()
            break
        elif user_input.lower().strip() == 'no':
            GLOBAL_PATH = input('Please enter the folder to do sorting: ')
            break
        else:
            print('Please choose correct option.')
    try:
        grab_path(GLOBAL_PATH)
        
        print('_{:_^155}'.format(''))

        print(f"Sorted directory:\t {GLOBAL_PATH}")
        print('_{:_^155}'.format(''))
        for i in folders:
            print("{:<10}|{:<144}".format(i.upper(), (' / '.join(
                os.listdir(os.path.join(GLOBAL_PATH, i))))))
        print('_{:_^155}'.format(''))
    except:
        print('Something went wrong... Your input is incorrect')


if __name__ == '__main__':
    main()
