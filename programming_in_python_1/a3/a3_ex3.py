user_input = input('Enter comma-separated elements: ')
dictionary = dict()
words = user_input.split(',')

for word in words:
    ordinal_value = 0
    for char in word:
        ordinal_value += ord(char)
    
    if word in dictionary:
        assert ordinal_value == int(dictionary[word])

    dictionary[word] = f'{ordinal_value}'

pairs = list(dictionary.items())
for pair in pairs:
    pair = list(pair)
    pair[0] = f"'{pair[0]}'"

    joined_pairs = " -> ".join(pair)
    print(joined_pairs)