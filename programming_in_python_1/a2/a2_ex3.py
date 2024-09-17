start = int(input('Start: '))
stop = int(input('Stop: '))
step = int(input('Step: '))

n_even = 0
sum_odd = 0
counter = 0

for i in range (start, stop, step):
    if counter < 5:
        print(f'Number in iteration {counter} = {i}')
        counter += 1
    if i%2==0:
        n_even += 1
    else:
        sum_odd += i

print(f'Even number count = {n_even}')
print(f'Sum of odd numbers = {sum_odd}')
    
    