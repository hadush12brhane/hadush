class Node:
    def __init__(self,d,n=None,p=None):
        self.data=d
        self.next_node=n
        self.prev_node=p
    def __str__(self):
        return ('(' +str(self.data)+')')
class circularl:
    def __init__(self,r=None):
        self.root=r
        self.size =0
    def add(self,d):
        if self.size==0:
            self.root=Node(d)
            self.root.next_node=self.root
        else:
            new_node=Node(d,self.root.next_node)
            self.root.next_node=new_node
        self.size +=1
    def find(self,d):
        this_node=self.root
        while True:
            if this_node.data==d:
                return d
            elif this_node.next_node==self.root:
                return False
            this_node=this_node.next_node
    def remove(self,d):
        this_node=self.root
        prev_node=None
        while True:
            if this_node.data==d:
               if prev_node is not None:
                   prev_node.next_node=this_node.next_node
               else:
                   if this_node.next_node !=self.root:
                       while this_node.next_node !=self.root:
                           this_node=this_node.next_node
                       else:
                        this_node.next_node=self.root.next_node
                        self.root=self.root.next_node
                        self.size-=1
                   return True
            elif this_node.next_node==self.root:
                return False
            prev_node=this_node
            this_node=this_node.next_node
    def print_list(self):
        if self.root is None:
            return
        this_node=self.root
        print(this_node,end='=>')
        while this_node.next_node!=self.root:
            this_node=this_node.next_node
            print(this_node,end='=>')
        print()
c=circularl()
for i in [5,6,7,8,9,23,4,90]:
    c.add(i)
print("sizE="+str(c.size))
print(c.find(6))
my_node=c.root
print(my_node,end='=>')
for i in range(7):
    my_node=my_node.next_node
    print(my_node,end='=>')
print()
#c.print_list()
c.remove(5)
c.print_list()
print("size="+str(c.size))
c.remove(90)
c.print_list()
print("size="+str(c.size))
c.print_list()

