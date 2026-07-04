# def contains_duplicate_1(arr):  #TC-> O(n²)
# Contains Duplicate
#     n=len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]==arr[j]:
#                 return True
#     return False

# arr=[int(x) for x in input().split()]
# print(contains_duplicate_1(arr))

def contains_duplicate_2(arr):   #TC-> O(n)
    array=set()
    for i in arr:
        if i in array:
            return True
        array.add(i)
    return False

arr=[int(x) for x in input().split()]
print(contains_duplicate_2(arr))