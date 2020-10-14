import numpy as np

def main():
	i=0 # declaring an integer
	n=10 # use any variable
	x=119.0 #floating points (decimals) easier than c++

	#numpy declares arrays and other functions (?)

	y = np.zeros(n,dtype=float) #declares 10 zeros in array
	            #zeros give the elements an initial value
	            #of zero
	for i in range(n): #i in range [0,n-1]
		y[i] =2.0 * float(i) +1 #sets y as 2i+1 (with decimals)

	for y_element in y:
		print(y_element)

	if __name__ == "__main__":
	           	main()           