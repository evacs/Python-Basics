x = [0.0, 3.0, 5.0, 2.5, 3.7] #define an array
print(type(x))

x.pop(2) #removes 3rd element
print(x)

x.remove(2.5) #removes specified element
print(x)

x.append(1.2) #add element=1.2 at end
print(x)

y = x.copy() #make copy call it y
print(y)

print(y.count(0.0))#how many elements are 0.0

print(y.index(3.7)) #print the index with values

y.sort() #sort the list
print(y)

y.reverse() #reverse sort
print(y)

y.clear() #remove all elements
print(y)

