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



#Q-2. Longest Substring Without Repeating Characters
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



#Q-3. Longest Repeating Character Replacement
#TC-> O(n)  SC-> O(1)
# def characterReplacement(word,k):
#     count = {}
#     res = 0
#     l = 0
#     max_freq = 0

#     for r in range(len(word)):
#         count[word[r]] = 1 + count.get(word[r], 0)
#         max_freq = max(max_freq, count[word[r]])

#         while (r - l + 1) - max_freq > k:
#             count[word[l]] -= 1
#             l += 1

#         res = max(res, r - l + 1)

#     return res

# word= input()
# k=int(input())
# print(characterReplacement(word,k))



#Q-4. Permutation In String
# TC-> O(n) SC-> O(1)
# def check_permutation(s1,s2):
#     if len(s1)>len(s2):
#         return False
#     s1_count={}
#     s2_count={}
#     for i in range(len(s1)):
#         s1_count[s1[i]]= 1 + s1_count.get(s1[i],0)
#         s2_count[s2[i]]= 1 + s2_count.get(s2[i],0)
#     if s1_count==s2_count:
#         return True
#     l=0 
#     for r in range(len(s1), len(s2)):
#         s2_count[s2[r]]=1 + s2_count.get(s2[r],0)
#         s2_count[s2[l]] -= 1
        
#         if  s2_count[s2[l]]==0:
#             s2_count.pop(s2[l])
#         l+=1

#         if s1_count==s2_count:
#             return True
#     return False

# string1=input()
# string2=input()
# print(check_permutation(string1,string2))



#Q-5. Minimum Window Substring
#TC-> O(n)  SC-> O(1)
# def Minimum_Window_Substring(s,t):
#     if len(s)<len(t):
#         return""
        
#     t_count={}
#     for char in t:
#         t_count[char]=t_count.get(char,0)+1
        
#     required=len(t_count)
#     match=0
#     count_window={}
#     left=0
#     min_len=float('inf')
#     start_idx=0
    
#     for right in range(len(s)):
#         char_in=s[right]
#         if char_in in t_count:
#             count_window[char_in]=count_window.get(char_in,0)+1
#             if count_window[char_in]==t_count[char_in]:
#                 match+=1
                
#         while(required==match):
#             current_len=right-left+1
#             if current_len<min_len:
#                 min_len=current_len
#                 start_idx=left
                
#             char_out=s[left]
            
#             if char_out in t_count:
#                 if t_count[char_out]==count_window[char_out]:
#                     match-=1
#                 count_window[char_out]-=1
                
#             left+=1
            
#     if min_len==float('inf'):
#         return""
#     else:
#         return s[start_idx : start_idx + min_len]

# s=input()
# t=input()
# print(Minimum_Window_Substring(s,t))


#Q-6 