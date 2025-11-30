def binary_search(arr, index):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (low+high)//2
        guess = arr[mid]
        if(guess == index):
            return mid
        elif(guess > index):
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [34, 45, 67, 43, 23]
my_list.sort()
print(my_list)
print(binary_search(my_list, 45))