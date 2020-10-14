#dealing with unexpected results
#great for writing complex programs

try:
	print (a) #throw an exception
except:
	print("a is not defined")

	#a is not defined, instead of crashing program,
	#we can ask it to tell us what the problem is

try: 
	print(a)
except NameError: #if this is the error...
	print("a still isn't defined") 
except:   #if not...
	print("Something else is wrong")


print(a) #this will not work and will
         #BREAK the program

