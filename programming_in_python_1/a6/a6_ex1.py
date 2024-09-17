import os

def file_statistics(path: str):
    f_name = os.path.basename(path)
    print(f'file_statistics(\'{f_name}\')')

    try:
        if not os.path.isfile(path):
            raise OSError
        if f_name.split('.')[-1] != 'txt':
            raise ValueError
        
        n_lines = 0
        n_words = 0
        n_chars = 0
        n_digits = 0
        with open(path, "r", encoding = "utf-8") as f:
            for line in f:
                n_lines+=1
                words = line.split()
                n_words += len(words)
                for char in line:
                    n_chars += 1
                    if char.isdigit():
                        n_digits += 1

        print(f'''--------------------       
Statistics of file {f_name}:
Number of lines: {n_lines}
Number of words: {n_words}
Number of characters: {n_chars}
Number of digits: {n_digits}
--------------------''')
        
    except OSError:
        print(f'OSError: Path {f_name} does not exist')
    except ValueError:
        print(f'ValueError: Path {f_name} is not a text file')
        