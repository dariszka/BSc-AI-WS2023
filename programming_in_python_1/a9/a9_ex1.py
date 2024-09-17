import re 
import os

try:
    f_name = input('Enter file name: ')

    if not os.path.isfile(f_name):
        raise ValueError(f"'{f_name}'is not a file")
    
    enc = input("Enter character encoding or press ENTER for default (utf-8): ")
    if enc == '':
        enc = 'utf-8'
except ValueError as e:
    print(e)
    exit(0)

pattern = input("Enter pattern or press ENTER to exit: ")
while pattern != '':
    with open(f_name, "r", encoding=enc) as f:
        text = f.read()
        match_list = re.findall(pattern, text)
        print(f"{pattern}: {match_list}")
    pattern = input("Enter pattern or press ENTER to exit: ")