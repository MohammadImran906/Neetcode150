#Creating and Printing Linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def display_list(self):
#         curr=self.head
#         while curr:
#             print(curr.data, end="->")
#             curr=curr.next
#         print("None")

# ll=LinkedList()

# Node1=Node(10)
# Node2=Node(20)
# Node3=Node(30)

# ll.head=Node1
# ll.head.next=Node2
# Node2.next=Node3

# ll.display_list()



#Q-1. Reverse Linked List
#TC-> O(n)  SC->O(1)
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def reverse_list(head):
#     prev=None
#     curr=head
#     while curr:
#         nxt=curr.next
#         curr.next=prev
#         prev=curr
#         curr=nxt
#     return prev

# def print_list(head):
#     temp=head
#     while temp:
#         print(temp.data,end="->")
#         temp=temp.next
#     print("None")

# Node1=Node(10)
# Node2=Node(20)
# Node3=Node(30)

# head=Node1
# head.next=Node2
# Node2.next=Node3

# print_list(head)
# reverse=reverse_list(head)
# print_list(reverse)


#Q-2. Merge Two Sorted Lists
#TC-> O(n+m)  SC-> O(1)
# class ListNode:
#     def __init__(self,val):
#         self.val=val
#         self.next=None

# def mergelist(list1,list2):
#     dummy=ListNode(0)
#     tail=dummy
#     while list1 and list2:
#         if list1.val<=list2.val:
#             tail.next=list1
#             list1=list1.next
#         else:
#             tail.next=list2
#             list2=list2.next
#         tail=tail.next
#     tail.next=list1 if list1 else list2
#     return dummy.next

# def creating_list(arr):
#     head=ListNode(int(arr[0]))
#     curr=head
#     for val in arr[1:]:
#         curr.next=ListNode(int(val))
#         curr=curr.next
#     return head

# def printingList(head):
#     curr=head
#     while curr:
#         print(curr.val,end="->")
#         curr=curr.next
#     print("None")

# L1_input=[1,3,8]
# L2_input=[4,7,10,11]

# l1=creating_list(L1_input)
# l2=creating_list(L2_input)

# merge=mergelist(l1,l2)
# printingList(merge)



#Q-3. Linked List Cycle
#TC->O(n)  SC-> O(1)
# class ListNode:
#     def __init__(self,val):
#         self.val=val
#         self.next=None

# def hascycle(head):
#     slow, fast=head, head
#     while fast and fast.next:
#         slow=slow.next
#         fast=fast.next.next

#         if slow==fast:
#             return True
#     return False

# def creating_list(arr,pos):
#     if not arr:
#         return None
#     head=ListNode(arr[0])
#     curr=head
#     for val in arr[1:]:
#         curr.next=ListNode(val)
#         curr=curr.next

#     if pos!=-1:
#         target=head
#         for i in range(pos):
#             target=target.next
#             curr.next=target
#     return head

# head=creating_list([1,2,3,4], pos=-1)
# print(hascycle(head))


#Q-4. Copy List With Random Pointer
#TC->O(n)  SC->O(1)
# class Node:
#     def __init__(self, val):
#         self.val=val
#         self.next=None
#         self.random=None

# def copyRandomList(head):
#     if not head:
#         return None

#     curr=head
#     while curr:
#         newNode=Node(curr.val)
#         newNode.next=curr.next
#         curr.next=newNode
#         curr=newNode.next

#     curr=head
#     while curr:
#         if curr.random:
#             curr.next.random=curr.random.next
#         curr=curr.next.next

#     curr=head
#     copy_head=curr.next
#     copy_curr=copy_head
#     while curr:
#         curr.next=curr.next.next
#         curr=curr.next
#         if copy_curr.next:
#             copy_curr.next=copy_curr.next.next
#             copy_curr=copy_curr.next

#     return copy_head

# def creatingList(data):
#     if not data:
#         return None

#     nodes=[Node(val) for val, _ in data]
#     for i in range(len(data)):
#         if i < len(data)-1:
#             nodes[i].next=nodes[i+1]

#         random_idx=data[i][1]
#         if random_idx is not None:
#             nodes[i].random=nodes[random_idx]
#     return nodes[0]

# def Print_list(head):
#     curr=head
#     while curr:
#         random_val=curr.random.val if curr.random else None
#         print(f"[Val: {curr.val} R: {random_val}]", end="->")
#         curr=curr.next

#     print("None")

# data=[[7,None],[13,0],[11,4],[10,2],[1,0]]

# Original=creatingList(data)
# Print_list(Original)

# Clone_list=copyRandomList(Original)
# Print_list(Clone_list)



#Q-5. Find the duplicate number
#TC-> o(n)  SC-> O(1)
#We have to give atleast N+1 inputs, N being the max of array
# def isduplicate(nums):
#     slow=nums[0]
#     fast=nums[0]
#     while True:
#         slow=nums[slow]
#         fast=nums[nums[fast]]
#         if slow == fast:
#             break

#     slow=nums[0]
#     while slow!=fast:
#         slow=nums[slow]
#         fast=nums[fast]
#     return slow

# nums=[int(x) for x in input().split()]
# print(isduplicate(nums))


#Q-5. LRU Cache
#TC->O(1)  SC-> O(n)
# from collections import OrderedDict
# class LRUCache:
#     def __init__(self,capacity):
#         self.cache=OrderedDict()
#         self.capacity=capacity

#     def get(self, key):
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]

#     def put(self,key,value):
#         if key in self.cache:
#             self.cache.move_to_end(key)

#         self.cache[key]=value

#         if len(self.cache)>self.capacity:
#             self.cache.popitem(last=False)

# obj=LRUCache(2)
# obj.put(1,10)
# obj.put(2,20)
# print(obj.get(1))
# obj.put(3,30)
# print(obj.get(2))
# print(obj.get(3))


#Q-6. Merge K sorted lists
#TC-> O(nlogk)  SC->O(k)
# class ListNode:
#     def __init__(self,val):
#         self.val=val
#         self.next=None

# class Solution:
#     def mergeKlists(self,lists):
#         if not lists or len(lists)==0:
#             return None
#         while len(lists)>1:
#             merged_list=[]
#             for i in range(0, len(lists),2):
#                 l1=lists[i]
#                 l2=lists[i+1] if i+1<len(lists) else None

#                 merged_list.append(self.merge2list(l1,l2))

#             lists=merged_list
#         return lists[0]

#     def merge2list(self,list1,list2):
#         dummy=ListNode(0)
#         tail=dummy
#         while list1 and list2:
#             if list1.val<=list2.val:
#                 tail.next=list1
#                 list1=list1.next
#             else:
#                 tail.next=list2
#                 list2=list2.next
#             tail=tail.next
#         tail.next=list1 if list1 else list2
#         return dummy.next

# def creating_list(arr):
#     head=ListNode(int(arr[0]))
#     curr=head
#     for val in arr[1:]:
#         curr.next=ListNode(int(val))
#         curr=curr.next
#     return head

# def printingList(head):
#     curr=head
#     while curr:
#         print(curr.val,end="->")
#         curr=curr.next
#     print("None")


# l1=creating_list([1,2,4,6])
# l2=creating_list([3,4,7,9])
# l3=creating_list([6,7,8,9])
# l4=creating_list([2,3,7,8])

# obj=Solution()

# res=obj.mergeKlists([l1,l2,l3,l4])
# printingList(res)



#Q-7. Reordered List
# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.next=None

# class Solution:
#     def reorderedList(self,head):
#         if not head or not head.next:
#             return None
        
#         slow=head
#         fast=head
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next

#         prev=None
#         curr=slow.next
#         slow.next=None

#         while curr:
#             nxt=curr.next
#             curr.next=prev
#             prev=curr
#             curr=nxt

#         first=head
#         second=prev
#         while second:
#             temp1=first.next
#             temp2=second.next

#             first.next=second
#             second.next=temp1

#             first=temp1
#             second=temp2


# def creatingList(arr):
#     dummy=Node(0)
#     curr=dummy
#     for val in arr:
#         curr.next=Node(val)
#         curr=curr.next
#     return dummy.next

# def printList(head):
#     curr=head
#     while curr:
#         print(curr.val,end="->")
#         curr=curr.next
#     print("None")

# arr=creatingList([1,2,3,4,5])

# obj=Solution()
# obj.reorderedList(arr)
# printList(arr)



#Q-8. Remove Nth Node From End of List.
# TC-> O(n)  SC-> O(1)
# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=next

# class Solution:
#     def removeNthFromEnd(self,head,n):
#         dummy=ListNode(0,head)
#         slow=dummy
#         fast=dummy
#         for _ in range(n+1):
#             fast=fast.next

#         while fast:
#             slow=slow.next
#             fast=fast.next

#         slow.next=slow.next.next

#         return dummy.next

# def creatList(arr):
#     if not arr:
#         return None
#     head=ListNode(arr[0])
#     curr=head
#     for val in arr[1:]:
#         curr.next=ListNode(val)
#         curr=curr.next
#     return head

# def display_list(head):
#     curr=head
#     while curr:
#         print(curr.val, end="->")
#         curr=curr.next
#     print("None")


# arr=[1,4,2,3,7,8,9]
# n=int(input())
# l1=creatList(arr)
# display_list(l1)
# obj=Solution()
# modified_list=obj.removeNthFromEnd(l1,n)
# display_list(modified_list)


#Q-9. Add Two numbers
# TC-> O(max(n,m))  SC-> O(max(n,m))
# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=next

# class Solution:
#     def AddTwoNumbers(self,l1,l2):
#         dummy=ListNode(0)
#         curr=dummy
#         carry=0
#         while l1 or l2 or carry:
#             val1=l1.val if l1 else None
#             val2=l2.val if l2 else None

#             total=val1+val2+carry
#             carry=total//10
#             new_digit=total%10

#             curr.next=ListNode(new_digit)
#             curr=curr.next

#             l1=l1.next if l1 else None
#             l2=l2.next if l2 else None
#         return dummy.next

# def creatList(arr):
#     if not arr:
#         return None
#     head = ListNode(arr[0])
#     curr = head
#     for val in arr[1:]:
#         curr.next = ListNode(val)
#         curr = curr.next
#     return head

# def display_list(head):
#     curr = head
#     while curr:
#         print(curr.val, end="->")
#         curr = curr.next
#     print("None")

# arr1 = [2, 4, 3]
# arr2 = [5, 6, 4]

# l1=creatList(arr1)
# l2=creatList(arr2)

# print("List 1:")
# display_list(l1)
# print("List 2:")
# display_list(l2)

# obj=Solution()
# result=obj.AddTwoNumbers(l1,l2)
# print("List after adding:")
# display_list(result)
