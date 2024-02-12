class  Node:
    def __init__(self,data):
        self.data= data
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
        self.size=0
    def addAtHead_node(self,d):
        new_node=Node(d)
        new_node.next=self.head
        self.head=new_node
    def inserAt_the_end(self,d):
        new_node=Node(d)
        temp=self.head
        size=0
        while(temp.next):
            temp=temp.next
            size+=1
        temp.next=new_node
    """def updateAt(self,i,d):
        new_node=Node(d)
        temp=self.head
        couter=0
        if temp.next is not None:
            while(temp.next):
                if(couter==i):
                    temp.data=new_node
                    return new_node
                temp=temp.next
                couter+=1
            print(new_node)"""
            
        
    def delthead(self):
        if self.head==None:
            print('this is empty list')
        else:
            temp=self.head
            self.head=temp.next
            #temp=None
            #self.head=self.head.next
        
            
        
            
    def printList(self):
        temp=self.head
        if(temp!=None):
            while(temp!=None):
                print(temp.data ,end="->")
                temp=temp.next
            print()
        else:
            print("this is empty")
    def updqateAT(self,d,r):
    
        new_node=Node(d)
        temp=self.head
        """counter=0
        while temp.next:
            if (counter==r):
                temp.data=new_node
            temp=temp.next
            counter+=1"""
                
        for i in range(1,r-1):
            if(temp!=None):
                temp=temp.next
        if (temp!=None):
            temp.next=new_node
        temp=temp.next
            #return new_node
        
                
            

l=linkedList()
#l.updateAt(1,89)
l.addAtend_node(9)
l.addAtend_node(56)
l.addAtend_node(8)
l.addAtend_node(5)
l.addAtend_node(6)
l.printList()

#l.updqateAT(3,3)
"""l.addAtend_node(67)
l.addAtend_node(657)
l.updqateAT(4,80)
l.inserAt_the_end(4895)
l.printList()
l.delthead()
l.updqateAT(21,3)
l.updqateAT(3,3)"""
print('after delete')
l.delthead()
l.printList()

        
        
        
        