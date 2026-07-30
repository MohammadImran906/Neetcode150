#Q-1. Binary search
#TC-> O(logn) SC-> O(1)
# def binary_search(arr,k):
#     l=0
#     r=len(arr)-1
#     while l<=r:
#         mid=(l+r)//2
#         if arr[mid]==k:
#             return mid
#         elif arr[mid]<k:
#             l=mid+1
#         else:
#             r=mid-1
#     return False

# arr=[int(x) for x in input().split()]
# k=int(input())
# print(binary_search(arr,k))



#Q-2. Search a 2-D matrix
#Better approach(Row-by-Row Binary search). TC-> O(M log N) SC->O(1)
# def Search_2D_1(matrix,target):
#     for i in matrix:
#         l=0
#         r=len(matrix[0])-1
#         if i[0] <= target <=i[-1]:
#             while l<=r:
#                 mid=(l+r)//2
#                 if i[mid]==target:
#                     return True
#                 elif i[mid]<target:
#                     l=mid+1
#                 else:
#                     r=mid-1
#     return False


# Optimal Approach(Binary search) 
#Tc->O(log(m*n))  SC-> O(1)
def Search_2D_2(matrix,target):
    rows=len(matrix)
    cols=len(matrix[0])

    l=0
    r=(rows*cols)-1
    while l<=r:
        mid=(l+r)//2

        row=mid//cols
        col=mid%cols

        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            l=mid+1
        else:
            r=mid-1
    return False

n=int(input())
matrix=[]
for i in range(n):
    rows=[int(x) for x in input().split()]
    matrix.append(rows)
target=int(input())
print(Search_2D_2(matrix,target))