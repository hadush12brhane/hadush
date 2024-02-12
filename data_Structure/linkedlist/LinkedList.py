class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    #adding at the end
    def push_back(self,newElement):
        newNode=Node(newElement)
        if(self.head==None):
            self.head=newNode
            return
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=newNode
            
            
            
       
    def push_At(self,newElement,postion):
        newNode=Node(newElement)
        if(postion < 1):
            print("the position must be > 1")
        elif(postion==1):
            newNode.next=self.head
            self.head=newNode
        else:
            temp=self.head
            for i in range(1,postion-1):
                if(temp!=None):
                    temp=temp.next
            if(temp!=None):
                newNode.next=temp.next
                temp.next=newNode
            else:
                print("the position is out of range")
                
                
        
               
            
            
            
    def printList(self):
        temp=self.head
        if(temp!=None):
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
                            
        else:
            print("this is empty")
            
            
myList=LinkedList()
myList.push_back(2)
myList.push_back(5)
myList.push_back(7)
myList.push_back(6)
myList.push_back(8)
myList.printList()
print("the updated list is")
myList.push_At(4,4)

myList.printList()

            
                
        