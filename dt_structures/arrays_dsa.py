my_array=[10,9,4,6,8,12,3]
print(my_array[3])

minVal=my_array[0]
for i in my_array:
    if i < minVal:
        minVal=i
print("Lowest value is", minVal)        

#Bubble sort
print("-----Buble sort------")
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n=len(my_array) #length of the array

for i in range(n-1): #Controls how many times the inner loop must run
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1]=my_array[j+1], my_array[j]
print("Sorted array", my_array)  

n=len(my_array)
for i in range(n-1):
    swapped=False
    for j in range(n-i-1):
        if my_array[j]> my_array[j+1]:
            my_array[j], my_array[j+1]=my_array[j+1],my_array[j]
            swapped=True
    if not swapped:
        break                  
print("Sorted array", my_array)