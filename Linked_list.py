#Creating and Printing Linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def display_list(self):
        curr=self.head
        while curr:
            print(curr.data, end="->")
            curr=curr.next
        print("None")

ll=LinkedList()

Node1=Node(10)
Node2=Node(20)
Node3=Node(30)

ll.head=Node1
ll.head.next=Node2
Node2.next=Node3

ll.display_list()