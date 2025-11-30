def linear_search(arr, index):
    for i in range(len(arr)):
        if(arr[i] == index):
            return i
    return None

my_list = [34, 45, 67, 43, 23]
print(linear_search(my_list, 23))