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


#Q-3. Evaluate Reverse Polish Notation
#TC-> O(n) SC-> O(n)
# def evalRPN(tokens):
#     stack=[]
#     for i in tokens:
#         if i=='+':
#             stack.append(stack.pop() + stack.pop())
#         elif i=='-':
#             stack.append(stack.pop() - stack.pop())
#         elif i=='*':
#             stack.append(stack.pop() * stack.pop())
#         elif i=='/':
#             stack.append(int(stack.pop() / stack.pop()))
#         else:
#             stack.append(int(i))
#     return stack[0]

# tokens=input().split()
# print(evalRPN(tokens))



#Q-4. Daily Tempature 
#TC->O(n) SC->O(n)
# def daily_temp(temp):
#     n=len(temp)
#     res=[0]*n
#     stack=[]
#     for i in range(n):
#         current_temp=temp[i]
#         while stack and current_temp>temp[stack[-1]]:
#             prev_index=stack.pop()
#             res[prev_index]=i-prev_index
#         stack.append(i)
#     return res

# temp=[int(x) for x in input().split()]
# print(daily_temp(temp))



#Q-5. Car fleet. TC-> O(n) SC-> O(n)
# def car_fleet(target,pos,spd):
#     cars=sorted(zip(pos,spd), reverse=True)
#     stack=[]
#     for pos,spd in cars:
#         time=(target-pos)/spd
#         stack.append(time)

#         if len(stack)>=2 and stack[-1]<=stack[-2]:
#             stack.pop()
#     return len(stack)

# target=int(input())
# position=[int(x) for x in input().split()]
# speed=[int(y) for y in input().split()]
# print(car_fleet(target,position,speed))


#Q-6. Largest rectangle in histogram
#TC->O(n) SC->O(n)
# def lar_rect_in_hist(heights):
#     max_area=0
#     stack=[]
#     for i,h in enumerate(heights):
#         start=i
#         while stack and stack[-1][1] > h:
#             index,height=stack.pop()
#             max_area=max(max_area, height* (i-index))
#             start=index
#         stack.append((start,h))
#     for i,h in stack:
#         max_area=max(max_area,h*(len(heights)-i))
#     return max_area

# heights=[int(x) for x in input().split()]
# print(lar_rect_in_hist(heights))