line1 = '=================================================='
line2 = '--------------------------------------------------'

print(line1)
print('PC Parts Store - Order')
print(line1)

n_cables = int(input('Number of cables: '))
n_monitors = int(input('Number of monitors: '))
n_keyboards = int(input('Number of keyboards: '))

cost_cables = n_cables*9.9
cost_monitors = n_monitors*249.99
cost_keyboards = n_keyboards*27.5
total = cost_cables + cost_monitors + cost_keyboards

print(f"{n_cables:3} cables (9.90 EUR each) = {cost_cables:.2f} EUR")
print(f"{n_monitors:3} monitors (249.99 EUR each) = {cost_monitors:.2f} EUR")
print(f"{n_keyboards:3} keyboards (27.50 EUR each) = {cost_keyboards:.2f} EUR")

print(line2)
print(f"Total: {total:.2f} EUR")
print(line1)

