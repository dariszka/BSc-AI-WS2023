x = None
y = None

while True:
    x = input('Enter number or \'x\': ')
    if y == None:
        if x == 'x':
            print('Empty sequence')
            exit(0)
        else:
            y = input('Enter number or \'x\': ')
            if y == 'x':
                print('All numbers had the same digit in the ones place')
                exit(0)
            elif int(x)%10 != int(y)%10:
                print(f"{x} and {y} differ in the ones place")
                exit(0)
            else:
                continue
    
    if x == 'x':
        print('All numbers had the same digit in the ones place')
        exit(0)
    elif int(x)%10 != int(y)%10:
        print(f"{y} and {x} differ in the ones place")
        exit(0)

    y = input('Enter number or \'x\': ')
    if y == 'x':
        print('All numbers had the same digit in the ones place')
        exit(0)
    elif int(x)%10 != int(y)%10:
        print(f"{x} and {y} differ in the ones place")
        exit(0)
    
    
