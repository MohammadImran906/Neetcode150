#Q-1 Valid Parantheses
# Stack optimal approach.
# TC->O(n)  SC-> O(n)
# def Valid_parantheses(string):
#     stack=[]
#     for i in string:
#         if i=='(' or i=='{' or i=='[' or i=='<':
#             stack.append(i)

#         else:
#             if len(stack)==0:
#                 return False
#             if i==')' and stack[-1]=='(':
#                 stack.pop()
#             elif i=='}' and stack[-1] =='{':
#                 stack.pop()
#             elif i==']' and stack[-1] =='[':
#                 stack.pop()
#             elif i=='>' and stack[-1] =='<':
#                 stack.pop()
#             else:
#                 return False

#     if len(stack)==0:
#         return True
#     else:
#         return False

# string=input()
# print(Valid_parantheses(string))
