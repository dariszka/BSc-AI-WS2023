n_lines = int(input('Enter number of lines: '))
if n_lines < 3:
    print('Invalid number of lines')
    exit(0)

horizontal_line = ''
vertical_row = ''
for i in range(n_lines):
    horizontal_line += '-'
    if i == 0 or i == (n_lines-1):
        vertical_row += '|'
    else:
        vertical_row += ' '

vertical_lines = (vertical_row + '\n')*(n_lines-2) 

print(horizontal_line)
print(vertical_lines, horizontal_line, sep='')