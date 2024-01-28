#Oligotemp by Lance Dornan

#Write a program that returns the oligo melting temperature 
#given the number of As, Cs, Gs, and Ts in the oligo. Use these two methods.
#For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4
#For longer oligos, Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)
#Demonstrate that your program works by computing the Tm of several oligos of different sizes.

import math
def oligos(A, C, G, T)):
	oligo = (A + C + G + T)
	if oligo <= 13:
		tm = (A+T)*2 + (G + C)*4
	elif oligo > 13:
		tm = 64.9 + 41* (G + C -16.4)/ (A + C + G + T)
	return tm 
print(oligos(1, 3, 4, 5))
print(oligos(33, 44, 12, 6))