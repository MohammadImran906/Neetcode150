# Q-1. Contains Duplicate
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



#Q-2. Valid Anagram
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


#Q-3. Two sum
# Brueforce approach. TC- O(n²) SC- O(1)
# def two_sum_1(arr, x):
#     n=len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]+arr[j]==x:
#                 indexes= i,j
#     return indexes     

# arr=[int(x) for x in input().split()]
# x=int(input())
# print(two_sum_1(arr,x))

#Optimal approach TC-> O(n) SC->O(1)
# def two_sum_2(arr, x):
#     n=len(arr)
#     start=0
#     for i in range(1,n):
#         if arr[start]+arr[i]==x:
#             index= start,i
#         start=start+1
#     return index

# arr=[int(x) for x in input().split()]
# x=int(input())
# print(two_sum_2(arr,x))


#Q-4. Group Anagram
#TC-> O(n.klogk)  SC-> (n.k)
# def group_anagrams(arr):
#     anagram_map = {}
    
#     for word in arr:
#         sorted_word = "".join(sorted(word))
        
#         if sorted_word not in anagram_map:
#             anagram_map[sorted_word] = []
            
#         anagram_map[sorted_word].append(word)
        
#     return list(anagram_map.values())

# arr = [x for x in input().split()]
# print(group_anagrams(arr))


# Q-5. Top K Frequent Elements
# TC-> O(nlogK)  SC-> O(n)
# from collections import Counter
# def top_k_most_frequent(arr,k):
#     frequency=Counter(arr)
#     sorted_frequency=(frequency.most_common(k))
#     return [item[0] for item in sorted_frequency]

# arr=[int(x) for x in input().split()]
# k=int(input())
# print(top_k_most_frequent(arr,k))


# optimal solution. TC->O(n)  SC->O(n)
# from collections import Counter
# def top_k_most_frequent(arr,k):
#     count=Counter(arr)
#     buckets=[[] for _ in range(len(arr) + 1 )]
    
#     for num,freq in count.items():
#         buckets[freq].append(num)
    
#     result=[]
#     for i in range(len(buckets)-1,0,-1):
#         for num in buckets[i]:
#             result.append(num)
#             if len(result)==k:
#                 return result

# arr=[int(x) for x in input().split()]
# k=int(input())
# print(top_k_most_frequent(arr,k))


#Q-6. Encode and Decode String
# TC-> O(n) SC-> O(1)
def encode(string):
    result=''
    for s in string:
        result += str(len(s)) + '#' + s 
    return result

def decode(s):
    res=[]
    i=0
    while i< len(s):
        j=i
        while s[j] != "#":
            j+=1

        length=int(s[i:j])

        word=s[j+1 : j + 1 + length]
        res.append(word)

        i= j+ 1 + length

    return res

string_list= [x for x in input().split()]
s=encode(string_list)
print(s)
y=decode(s)
print(y)