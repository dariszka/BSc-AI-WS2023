def gen_fibonacci(upper_bound):
    try:
        if not isinstance(upper_bound, int) and not isinstance(upper_bound, float):
            raise TypeError('TypeError: Upper bound needs to be either integer or float.')
        if upper_bound < 0:
            raise ValueError('ValueError: Upper bound needs to be at least zero.')
        
        f0, f1 = 0, 1
        while f0 <= upper_bound:
            yield f0
            f0, f1 = f1, f0 + f1
    except (ValueError, TypeError) as ex:
        print(ex)
        exit(0) #added this because when called without it, the function yields an empty list after the error message


