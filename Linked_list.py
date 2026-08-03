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

