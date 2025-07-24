
new_list = [1,2,3,4,5,6,7,8,9,10]

# Accessing an array by Index
print(new_list[3])

# Searching for a value in an array
for n in new_list:
  if n == 1:
    print (True)
    break

if 3 in new_list: print(True)

#Inserting a value into an existing array

new_list[3] = 12 #Adds a value to the defined index and shifts all other items in the array
print(new_list)

new_list.append(14) #Adds only one value to the last part of the array
print(new_list)

new_list.extend([20, 21, 22]) #Inserts a full array
print(new_list)

#Deletion operation in an array
new_list.remove(8) #Removes Item by value
print(new_list)

new_list.pop(3) #Removes Item by index
