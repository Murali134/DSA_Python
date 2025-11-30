'''def countDown(i):
    print(i)
    countDown(i-1)
    
countDown(3)'''

'''def countDown(i):
    print(i)
    if i <= 1: # This is Base Case
        return
    else:
        countDown(i-1) # This is Recursive Case
countDown(3)'''

'''
def a():
    b()

def b():
    c()

def c():
    print("Hi")

a()
'''

'''def fact(x):
    if x == 1:
        return 1
    else:
        return x*fact(x-1)
    
print(fact(4))'''

'''def greet(name):
    print("Hello", name)
    greet2(name)
    print("Goodbye", name)

def greet2(name):
    print("How are you,", name, "?")

greet("Maggie")'''

'''def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(3))'''


'''def countdown(n):
    while n>= 0:
        print(n)
        n = n-1
        
countdown(5)'''

'''def sum(arr):
    total  = 0
    for x in arr:
        #total = total + x
        total += x
    return total

print(sum([1, 2, 3, 5]))'''

# Recursive Binary Search for finding the index of the element.
def find_bs_index(arr, low, high, target):
    if low > high:
        return -1
    mid = (low+high) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return find_bs_index(arr, low, mid-1, target)
    else:
        return find_bs_index(arr, mid+1, high, target)
    
arr = [123, 23, 45, 213]
print(find_bs_index(arr, 0, len(arr)-1, 23))

# Recursion for sum
def sum_arr(list):
    if list == []:
        return 0
    return list[0] + sum_arr(list[1:])

print(sum_arr([1, 3, 4, 6]))

# Recursion for count
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print(count([1, 3, 4, 6]))

# Find the max element in the array using Recursion
def find_max(list):
    if len(list) == 1: # Base Case
        return list[0]
    sub_max = find_max(list[1:]) # Recursive Case
    if list[0] > sub_max:
        return list[0]
    else:
        return sub_max
    
print (find_max([1, 3, 4, 6]))

# Recursive Binary Search:

def bs_index(arr, low , high, target):
    # BaseCase1: There were no elements to search
    if low > high:
        return -1
    mid = (low+high) // 2
    # BaseCase2: Found the element
    if(arr[mid] == target):
        return mid
    # RecursiveCase: Search left half
    if(arr[mid] < target):
        return bs_index(arr, 0, mid-1, target)
    # RecursiveCase: Search right half
    else:
        return bs_index(arr, mid+1, high, target)
    
arr = [23, 43, 324, 213, 12]
print(bs_index(arr, 0, len(arr)-1, 213))



# Quicksort using Recursion

def quicksort(arr):
    # Base Case
    if len(arr) < 2:
        return arr
    # Recursive Case
    pivot = arr[0]
    less = []
    greater = []
    # Partition Step
    for value in arr[1:]:
        if value <= pivot:
            less.append(value)
        else:
            greater.append(value)
    # Divide & Conquer
    return quicksort(less) + [pivot] + quicksort(greater)
        

list = [12, 3, 12, 34, 2, 6]
print(quicksort(list))


#Iterative Quicksort With Median-of-Three Pivot
def quicksort_m3(arr):
    stack = [(0, len(arr)-1)]
    while stack:
        left, right = stack.pop()
        if left >= right: 
            continue

        mid = (left + right) // 2
        pivot = sorted((arr[left], arr[mid], arr[right]))[1]
        if pivot == arr[left]:
            index = left
        elif pivot == arr[mid]:
            index = mid
        else:
            index = right
        arr[index], arr[right] = arr[right], arr[index]

        i = left - 1
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        i += 1
        arr[i], arr[right] = arr[right], arr[i]

        stack.append((left, i-1))
        stack.append((i+1, right))
        
    return arr
    