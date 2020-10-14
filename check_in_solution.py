def main(): #defines a function called main
	i=0
	x=119.0
	for i in range(120): #this will loop i from 0 to 119
		if ( (i%2)==0 ): #if i is even...
			x+=3.0           #add 3 to it	
		else:            #if it's odd, subtract 5
			x -=5.0

		s = "The value of x = %3.2e" % x #defines s, 
		       # %3.2= sci. notation w/2 decimal places
		print(s)  #print this string and the value

if __name__ == '__main__': #if main exists, run it
	main()

		

		
		