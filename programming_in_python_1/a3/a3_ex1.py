n_rows = int(input('Number of rows: '))
n_columns = int(input('Number of cols: '))

header_list = [f' {i}' for i in range(n_columns)]
header = '  ' 
for i in header_list: 
    header += i
print(header)

line = '  ' + '--'*n_columns      
print(line)


matrix = [[0] * n_columns for i in range(n_rows)]
for i, row in enumerate(matrix): 
    for j, element in enumerate(row):
        if i == j:
            matrix[i][j] = 1
        
    row_str = ''
    for element in row:
        row_str += ' ' + str(element)
    print(f'{i}|' + row_str)



