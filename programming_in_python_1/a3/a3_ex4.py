user_input = input('Enter comma-separated elements: ')
elements = user_input.split(',')
numbers = []
non_numbers = []
numbers_dictionary = dict()

for element in elements:
    if element.isdecimal():
        element = int(element)
        numbers.append(element)
        if element in numbers_dictionary:
            numbers_dictionary[element] += 1
        else:
            numbers_dictionary[element] = 1
    else:
        non_numbers.append(element)

print(f"""integers: {numbers}
counts: {numbers_dictionary}
rest: {non_numbers}""")
