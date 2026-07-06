# Contains Duplicate
# def contains_duplicate_1(arr):  #TC-> O(n²)
#     n=len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]==arr[j]:
#                 return True
#     return False

# arr=[int(x) for x in input().split()]
# print(contains_duplicate_1(arr))

# def contains_duplicate_2(arr):   #TC-> O(n)
#     array=set()
#     for i in arr:
#         if i in array:
#             return True
#         array.add(i)
#     return False

# arr=[int(x) for x in input().split()]
# print(contains_duplicate_2(arr))



# Valid Anagram
# Btter approach. TC-> O(logn) SC->O(n)
# def valid_anagram_1(w1,w2):
#     if(len(w1) != len(w2)):
#         return False
#     return "".join(sorted(w1))=="".join(sorted(w2))

# w1=input()
# w2=input()
# print(valid_anagram_1(w1,w2))


# # Optimal approach-Using Hashing. TC->:O(n) SC->: O(1)
# from collections import Counter
# def valid_anagram_2(w1,w2):
#     if len(w1) != len(w2):
#         return False

#     if Counter(w1)==Counter(w2):
#         return True
#     return False

# w1=input()
# w2=input()
# print(valid_anagram_2(w1,w2))

#Another Approach
#TC-> O(n²) SC->O(N)
# def valid_anagram_3(w1,w2):
#     if len(w1) != len(w2):
#         return False 
    
#     word_list_2=list(w2)

#     for i in w1:
#         if i in word_list_2:
#             word_list_2.remove(i)
#         else:
#             return False
#     return True

# w1=input()
# w2=input()
# print(valid_anagram_3(w1,w2))