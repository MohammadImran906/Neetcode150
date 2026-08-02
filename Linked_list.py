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
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def reverse_list(head):
    prev=None
    curr=head
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev

def print_list(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print("None")

Node1=Node(10)
Node2=Node(20)
Node3=Node(30)

head=Node1
head.next=Node2
Node2.next=Node3

print_list(head)
reverse=reverse_list(head)
print_list(reverse)

