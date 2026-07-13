#Q-1. Valid Palindrome
#TC-> O(n) SC->O(1)
# def valid_palindrome(word):
#     n=len(word)
#     left=0
#     right=n-1

#     while left<right:
#         if word[left] != word[right]:
#             return False
#         left +=1
#         right-=1

#     return True

# word=input()
# if valid_palindrome(word):
#     print("Valid")
# else:
#     print("Invalid")



#Q-2. Two Sum II Input Array Is Sorted
# def two_sum(arr,x):
#     n=len(arr)
#     start=0
#     end=n-1
#     while start<end:
#         current_sum=arr[start] + arr[end]

#         if current_sum==x:
#             return start, end
#         elif current_sum< x:
#             start+=1
#         else:
#             end-=1
#     return []

# arr=[int(x) for x in input().split()]
# x=int(input())
# print(two_sum(arr,x))



#Q-3. 3 Sum
# TC-> O(n²), Aux.SC->O(1), Internal SC->O(n)
# def three_sum(arr):
#     arr.sort()
#     n=len(arr)
#     result=[]
#     for i in range(n):

#         if i > 0 and arr[i] == arr[i - 1]:
#             continue

#         start=i+1
#         end=n-1

#         while start<end:
#             current_sum=arr[i] + arr[start]+ arr[end]
#             if current_sum==0:
#                 result.append([arr[i],arr[start],arr[end]])
#                 start+=1
#                 end-=1

#                 while start<end and arr[start]==arr[start-1]:
#                     start+=1
#                 while start<end and arr[end]==arr[end+1]:
#                     end-=1
#             elif current_sum<0:
#                 start+=1
#             else:
#                 end-=1
#     return result

# arr=[int(x) for x in input().split()]
# print(three_sum(arr))



#Q-4. Container With Most Water
#TC-> O(n) SC-> O(1)
# def container_with_most_water(arr):
#     n=len(arr)
#     result=0
#     start=0
#     end=n-1
#     while start<end:
#         width=end-start
#         water_content= min(arr[start],arr[end]) * width
#         result= max(water_content,result)

#         if arr[start]<arr[end]:
#             start+=1
#         else:
#             end-=1
#     return result

# arr=[int(x) for x in input().split()]
# print(container_with_most_water(arr))



#Q-5. Trapping Rain Water
#TC-> O(n) SC->O(1)
def trapping_rain_water(arr):
    n=len(arr)
    total_water=0
    start=0
    end=n-1
    left_max=arr[start]
    right_max=arr[end]
    if not arr or n<3:
        return 0
    while start<end:
        if left_max<right_max:
            start=start+1
            if arr[start]<left_max:
                total_water += left_max-arr[start]
            else:
                left_max=arr[start]
        else:
            end-=1
            if arr[end]<right_max:
                total_water+=right_max-arr[end]
            else:
                right_max=arr[end]
    return total_water

arr=[int(x) for x in input().split()]
print(trapping_rain_water(arr))