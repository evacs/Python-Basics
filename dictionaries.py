
example_dict = {

     #keys       values
	"class"  :  "Astr 119",
	"prof"   : "Brant",
	"Awesomeness"  : 10
}
print(type(example_dict))

#get value via key

course = example_dict["class"]
print(course)

#change value with associated key
example_dict["Awesomeness"] += 1 
		#increase by one
print(example_dict) #print dictionary

#to print element by element:
for x in example_dict.keys():
	print(x,example_dict[x])