#Q-1. Best Time to Buy And Sell Stock
#TC->O(n)   SC-> O(1) 
# def Buy_Sell(prices):
#     n=len(prices)
#     left=0
#     right=1
#     max_profit=0
#     while right<n:
#         if prices[left]<prices[right]:
#             current_profit=prices[right]-prices[left]
#             max_profit=max(current_profit,max_profit)
#         else:
#             left=right
        
#         right+=1
    
#     return max_profit


# prices=[int(x) for x in input().split()]
# print(Buy_Sell(prices))



#Longest Substring Without Repeating Characters
# Sliding window approach.TC->O(n²) Sc->O(n)
# def length_of_longest_substring(string):
#     start=0
#     next=0
#     new_word=""
#     max_length=0
#     while next<len(string):
#         if string[next] not in new_word:
#             new_word+=string[next]
#             next+=1
#             max_length=max(max_length,len(new_word))
#         else:
#             start=+1
#             new_word=new_word[start:next]
#     return max_length

# string=input()
# print(length_of_longest_substring(string))


#Optimal approach
# TC-> O(n)  SC-> O(m)
# def length_of_longest_substring(string):
#     empty_dict={}
#     left=0
#     result=0

#     for i in range(len(string)):
#         if string[i] in empty_dict:
#             left=max(empty_dict[string[i]] + 1, left)

#         empty_dict[string[i]]=i
#         result=max(result, i-left+1)

#     return result


# string=input()
# print(length_of_longest_substring(string))