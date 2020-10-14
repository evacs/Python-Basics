import numpy as np 

i = 10 #integer
print(type(i)) #print the data type defined by i

a_i = np.zeros(i,dtype=int) #array of integers with i elemenets?
print(type(a_i)) #will return ndarray
print(type(a_i[0])) #will return int64 (bits)



x = 119.0 #float, decimal
print(type(x))

y= 1.19e2 #sci note
print(type(y))

z = np.zeros(i,dtype=float) #array of floats
print(type(z))  #will return ndarray
print(type(z[0]))  #will return int64 (bits)