sub_duration = int(input('Please enter the duration of your subscription (in months): '))

if sub_duration <= 0:
    print('Invalid subscription duration')
    exit(0)
elif sub_duration < 6:
    monthly_price = 6.5
elif sub_duration > 6 and sub_duration < 12:
    monthly_price = 5.9
else:
    postal_code = int(input('Please enter your postal code: '))
    if postal_code < 1000 or  postal_code > 9999:
        print('Invalid postal code')
        exit(0)
    else:
        rest = (postal_code%1000 - postal_code%10)/1000
        monthly_price = (4 + rest)

print(f'The price per month is {monthly_price:.2f}')
print(f'The full price for {sub_duration} months is {(monthly_price*sub_duration):.2f}')
