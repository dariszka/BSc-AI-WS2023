import os

def print_directory(dir_path: str, level:int=1):
    try:
        elems = sorted(os.listdir(dir_path))
        if level==1:
            print(f'path_to_the_directory_{os.path.basename(dir_path)}')
        if len(elems) != 0:
            for elem in elems:
                new_path = os.path.join(dir_path, elem)
                if os.path.isfile(new_path):
                    print(level*f'    '+ elem)
                elif os.path.isdir(new_path):
                    print(level*f'    '+ elem)
                    level+=1
                    print_directory(new_path,level)
                    level-=1
    except NotADirectoryError:
        print("dir_path is a file not a directory")
    except FileNotFoundError:
        print("dir_path is invalid")

#print_directory(dir_path) is the correct function call
#changing the level will change the indentation
#but also get rid of the first line 'path to directory ...'
dir_path = '/home/darina/Desktop/std/sem1/prog-py-I/lec5/d0'
print_directory(dir_path, 1)


