a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))

sum_a_b_d = a+b+d
product_all = a*b*c*d
sum_a_b_x_sum_c_d = (a+b)*(c+d)
a_by_d_int = a//d
a_by_d_reg = a/d
modulo_a_by_b = a%b
c_power_minus_a = c**(-a)
square_root_b = b**(1/2)
complex_eq = b/3 * (b**(a + d/2) - 1) + c

print(f"Sum of a, b and d: {sum_a_b_d}")
print(f"Product of all numbers: {product_all}")
print(f"The sum of a and b times the sum of c and d: {sum_a_b_x_sum_c_d}")
print(f"a divided by d (int): {a_by_d_int}")
print(f"a divided by d (float): {a_by_d_reg} ")
print(f"Remainder of a divided by b: {modulo_a_by_b}")
print(f"c to the power of -a: {c_power_minus_a}")
print(f"b to the power of 1/2 (square root): {square_root_b}")
print(f"Complex equation: {complex_eq}")
