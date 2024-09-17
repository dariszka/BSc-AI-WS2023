all = []
while True:
    elem = input('Enter element or \'x\' when done: ')
    if elem == 'x':
        print(f'all: {all}')
        unique = sorted(list(set(all)))
        print(f'unique (sorted): {unique}')
        exit(0)
    else:
        all.append(elem)
