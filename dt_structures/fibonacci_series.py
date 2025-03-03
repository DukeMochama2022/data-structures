previous_1=0
previous_2=1

print(previous_1)
print(previous_2)

for fibo in range(20):
    new_fibonacci=previous_1+previous_2
    print(new_fibonacci)
    previous_2=previous_1
    previous_1=new_fibonacci

#solving using RecursionError
print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)    