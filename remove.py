class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add(self,d):
        new_node=Node(d)
        if(self.head==None):
            self.head=new_node
            return
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_node
            return
    
    
    def pop_At(self,postion):
        newNodeTd=Node(postion)
        if(postion < 1):
            print("the position must be > 1")
        elif(postion==1 and self.head!=None):
            newNodeTd=self.head
            self.head=self.head.next
            newNodeTd=None
        else:
            temp=self.head
            for i in range(1,postion-1):
                if(temp!=None):
                    temp=temp.next
            if(temp!=None and temp.next!=None):
                newNodeTd=temp.next
                temp.next=temp.next.next 
                temp=newNodeTd
            else:
                print("the list in the given position alredy null")
            
    def delete_last_node(self):
        if self.head is None:
           return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

        
    def printList(self):
        temp=self.head
        if(temp!=None):
            while(temp!=None):
                print(temp.data ,end="->")
                temp=temp.next
            print()
        else:
            print("this is empty")
            
            
myList=LinkedList()
myList.add(41)
myList.add(78)
myList.add(4)
myList.add(7)
myList.add(45)
myList.add(67)
myList.printList()

"""myList.push_At(2)
myList.push_back(5)
myList.push_back(4)
myList.push_back(6)
myList.push_back(8)
myList.printList()"""
print("the updated list is")
myList.pop_At(4)
myList.delete_last_node()
myList.printList()
