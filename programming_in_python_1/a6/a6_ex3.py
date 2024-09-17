import os

def merge_csv_files(
        *paths: str, 
        delimiter = ';', 
        only_shared_columns=False):

    headers = []
    data = []

    for path in paths:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        f_header = lines[0].strip().split(delimiter)
        f_data = [line.strip().split(delimiter) for line in lines[1:]]

        headers.append(f_header)
        data.append(f_data)

        #to make sure it's the same dir as the csv files, it's under the assumption they're all in the same one
        #else it will save it in the same file as the last one 
        file_name = os.path.basename(path)
        abs_path = os.path.abspath(path)
        abs_path = abs_path.split(file_name)[0]

    if only_shared_columns:
        columns = headers[0]
        for header in headers[1:]:
            columns = [column for column in columns if column in header]
    else:
        columns = headers[0]
        columns = []
        for header in headers:
            columns += [column for column in header if column not in columns]
   
    matrix = []
    for f_data, header in zip(data, headers):
        for row in f_data:
            new_row = []
            for column in columns:
                if column in header:
                    column_index = header.index(column)
                    new_row.append(row[column_index])
                else:
                    new_row.append('NaN')
            matrix.append(new_row)

   
    with open(abs_path + 'merged.csv', 'w') as f:
        f.write(delimiter.join(columns) + '\n')
        for row in matrix:
            f.write(delimiter.join(row) + '\n')
