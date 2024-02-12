"""x=40
while x:
    x=x-1
    if x % 2 !=0:continue
    print(x ,end=" ")
    """
"""while True:
    name= input('enter name')
    if name=='stop':break
    age= input('enter age')
    print(name,'=>',int(age)**2)"""
    
#check for prime or not
while True:
    
 y=input('enter a number ')
 t=int(y) //2
 while t >1:
    if int(y) % t==0:
        print(y, 'has fator',t)
        print('so it is composit')
        break
    t-=1
 else:
    print(y, 'is prime')
    
else:
    StopIteration


    
    
    
    
        
            
    