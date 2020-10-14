#strings
s = "I am a string."
print(type(s))

#Boolean- True/False
yes = True
print(type(yes))

no = False
print(type(no))

# List - ordered and UNchangeable
alpha_tuple = ("a", "b", "c") #initializing tuple
print(type(alpha_tuple))

try:
	alpha_tuple[2] = "d" #try to add d to end
except TypeError:
	print("Can't add elements to tuples!")
print(alpha_tuple)