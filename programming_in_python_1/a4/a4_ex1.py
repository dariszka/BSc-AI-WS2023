def split_list(lst: list, num_sublists: int) -> list:
    if num_sublists == 0:
        return lst
    else:
        split_list = []
        for _ in range(num_sublists):
            split_list.append([])

        for i, elem in enumerate(lst):
            split_list[i % num_sublists].append(elem)

    return split_list
