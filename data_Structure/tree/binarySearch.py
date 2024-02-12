class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
        
    def insert(self,data):
        if self.key is None:
            self.key=data
            return 
        #if self.key==data:
            return
        if data<self.key:
            if self.lchild:
                self.lchild.insert(data) 
            else:
                self.lchild=BST(data)       
        else:
            if self.rchild:
                self.rchild.insert(data) 
            else:
                self.rchild=BST(data) 
    def search(self,data):
        if self.key==data:
            print("node found")
            return
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("no found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node not found")
    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def Inorder(self):
        if self.lchild:
            self.lchild.Inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.Inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")
    def delete(self,data):
        if self.key is  None:
            print("empty")
            return
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("the given data is not present")
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("not found the data")
            
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)
        return self
    def min_key(self):
        current =self
        while(current.lchild):
            current=current.lchild
        print("the min is",current.key)
    
    def max_key(self):
        current =self
        while(current.rchild):
            current=current.rchild
        print("the max is",current.key)

             
root=BST(-2)
list1=[2,5,6,8,4,0,1,3]
for i in list1:
    root.insert(i)
root.min_key()
root.max_key()
print("preorder")
root.delete(8)
root.preorder()
print()
print("inorder")
root.delete(3)
root.Inorder()
print()
root.delete(5)
print("postorder")
root.postorder()
print()
root.delete(2)


