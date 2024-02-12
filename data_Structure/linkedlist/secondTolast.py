class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def findSecondlast(head):
    temp=head
    if (temp==None or temp.next==None):
        return -1
    while(temp!=None):
        if (temp.next.next==None):
            return temp.data
        temp=temp.next
def push(head,new_data):
    new_data=Node(new_data)
    new_data.next=head
    head=new_data
    return head
def printlist(self):
    temp=head 
    while(temp):
        print(temp.data,end=" ")
        temp=temp.next
if __name__=='__main__':
    head=None
    head=push(head,12)
    head=push(head,67)
    head=push(head,45)
    head=push(head,56)
    head=push(head,34)
    head=push(head,12)
print(printlist(head))
   # print('the second last')
print(findSecondlast(head))
    
    

