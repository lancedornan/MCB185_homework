# Write a function that solves the quadratic formula (ax^2 + bx + c),
# returning the two X-intercepts. Demonstrate that it works by using the 
#formula multiple times within the program.


import math
def quadratic(a,c,b):
	x1= (-b + math.sqrt(b**2 + 4 * a * c)) / 2 * a
	x2= (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a
	assert(a > 0)
	return x1, x2
    

print(quadratic(1, 2, -3))
print(quadratic(2, 6, -9))