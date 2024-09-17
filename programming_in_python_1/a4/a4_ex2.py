def clip(*values, min_=0, max_=1) -> list:
    lst = []
    for value in values:
        if value < min_:
            lst.append(min_)
        elif value > max_:
            lst.append(max_)
        else:
            lst.append(value)

    return lst
