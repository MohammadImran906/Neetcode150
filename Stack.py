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



#Q-2. Min Stack two stack approach
#TC-> O(1)  SC-> O(n)
# class Minstack:
#     def __init__(self):
#         self.main_stack=[]
#         self.min_stack=[]
#     def push(self,val):
#         self.main_stack.append(val)
#         if len(self.min_stack)==0 or val <= self.min_stack[-1]:
#             self.min_stack.append(val)
#     def pop(self):
#         if self.main_stack[-1]==self.min_stack[-1]:
#             self.min_stack.pop()
#         self.main_stack.pop()
#     def top(self):
#         return self.main_stack[-1]
#     def getMin(self):
#         return self.min_stack[-1]

# obj=Minstack()
# obj.push(4)
# obj.push(9)
# obj.push(1)
# print(f" Min is {obj.getMin()} ")
# obj.pop()
# print(f" Top of stack is {obj.top()} ")