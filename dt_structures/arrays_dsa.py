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

print("-----Selection sort------")
n=len(my_array)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
       if my_array[j] < my_array[min_index]:
        min_index=j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
print("Sorted array",my_array)

print("-----Quicksort------")
def partition(array,low, high):
    pivot=array[high]

    i=low-1
    for j in range(low, high):
        if array[j] <=pivot:
            i +=1
            array[i],array[j]=array[j],array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)
        
print("----Linear search-----")
def linearSearch(arr,targetValue):
    for i in range(len(arr)):
        if arr[i] == targetValue:
            return i
    return -1

arr=[3, 7, 2, 9, 5]
targetValue=9

result=linearSearch(arr, targetValue)
if result != -1:
    print("Value",targetValue,"found at index", result)
else:
    print("Value",targetValue ,"not found")    


print("----binary search-----")
def binary_search(arr, targetValue):
    left=0
    right=len(arr)-1

    while left <= right:
        mid =(left+right) //2
        if arr[mid] == targetValue:
            return mid
        if arr[mid] < targetValue:
            left = mid + 1
        else:
            right = mid - 1
    return -1

myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15
result = binary_search(myArray, myTarget)
if result != -1:
    print("Value",myTarget,"found at index", result)
else:
    print("Target not found in array.")