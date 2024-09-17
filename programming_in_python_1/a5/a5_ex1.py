def sub_summarize(nested: list, sub_sums: list) -> int:
    current_sum = 0
    for elem in nested:
        if isinstance(elem, int):
            current_sum += elem
        else:
            sub_sum = sub_summarize(elem, sub_sums)
            current_sum += sub_sum

    sub_sums.append(current_sum)
    return current_sum

nested = [1, 2, 3, [4, [5, 6], 7], 8, [9, 10]]

sub_sums = []

print(sub_summarize(nested, sub_sums)) #-> 55
print(sub_sums)

#sub_sums -> [11, 22, 19, 55]
