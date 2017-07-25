"""
Write a function power that accepts two arguments, a and b and
calculates a raised to the power b.

Example

power(2, 3) => 8

"""

def power(a,b):
    if a == 0 and b == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return (a * power(a,b-1))

def power_iter(a,b):
	count, result = 0, 1
	while count < b:
		result = result * a

print power(0,90)
print power(3,0)
print power(10,0)
print power(3,0)
print power(100000,5)
