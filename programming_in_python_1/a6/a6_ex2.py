import os

def chunks(path: str, size: int, mode='r'):
    try:
        if not os.path.isfile(path):
            raise ValueError
        if size < 1:
            raise ValueError
        
        with open(path, mode) as f:
            while chars := f.read(size):
                yield(chars)

    except ValueError:
        #this is just so I can print a different message for the same error
        if not os.path.isfile(path):
            print('Error: path is not file')
        elif size < 1:
            print('Error: chunk size smaller than 1') 

# for i, c in enumerate(chunks("ex2_example.txt", 25, mode="rb")):
#     print(f"Chunk {i} = {c}")