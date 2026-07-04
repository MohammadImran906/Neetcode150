# Contains Duplicate
def contains_duplicate(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                return True
    return False

arr=[int(x) for x in input().split()]
print(contains_duplicate(arr))