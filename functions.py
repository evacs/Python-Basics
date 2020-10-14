import numpy as np
import sys

def expo(x): #define a function that returns a value
	return np.exp(x) #returns e to the x


def show_expo(n): #def subroutine that doesn't return value
	for i in range(n):
		print(expo(float(i))) #calls expo function

def main():

	n = 10 #n is 0-9
	#check for command line argument
	if(len(sys.argv)>1):
		n = int(sys.arg[1])

	show_expo(n) #calls above subroutine 

if __name__ == "__main__":
	main()