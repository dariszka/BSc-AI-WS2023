def sort(elements: list, ascending: bool = True):
    if ascending == True:
        for i in range(1, len(elements)):
            j = i - 1

            while j >= 0 and elements[i] < elements[j]:
                elements[j], elements[i] = elements[i], elements[j]
                i = j 
                j -= 1
    else:
        for i in range(1, len(elements)):
            j = i - 1

            while j >= 0 and elements[i] > elements[j]:
                elements[j], elements[i] = elements[i], elements[j]
                i = j 
                j -= 1
