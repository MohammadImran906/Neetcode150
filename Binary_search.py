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