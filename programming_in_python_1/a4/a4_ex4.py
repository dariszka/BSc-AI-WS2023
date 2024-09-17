def round_(number, ndigits:int = None):
    splits = str(number).split('.')
    whole = int(splits[0])
    rest = splits[1]
    rest_list = [int(num) for num in rest]
    n = 0

    if ndigits is None:
        if rest_list[0] >= 5:
            whole +=1
        n = whole
    else:
        if len(rest_list) == ndigits or len(rest_list) <= ndigits:
            n = str(whole) + '.' + rest
            n = float(n)
        else:
            stop = rest_list[:ndigits]
            
            if len(stop) == 0: # ndigits == 0 case
                if rest_list[ndigits] >= 5:
                    whole += 1
                n = float(whole)
            elif rest_list[ndigits] >= 5: 
                stop[-1] += 1

            rest = ''.join(str(num) for num in (stop))
            n = str(whole) + '.' + rest
            n = float(n)
        
    return n