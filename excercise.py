"""def fuctorCountTwo(data):
    count=0
    while data%2==0:
        data=data/2
        count+=1
    return count

well=int(input("enter the number "))
result=fuctorCountTwo(well)
print(result)
arr = [1, 2, 3, 4,5,6,7]
arr1 = [None]*7
for i in range(0, 7):
    arr1[6 - i] = arr[i]
for j in range(0, 7):
    print(arr1[j],end=" ")"""
"""n = int(input("size of array:"))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i}: ")))
arr1 = [0] * n
for i in range(0, n):
    arr1[n - i - 1] = arr[i]
for j in range(0, n):
    print(arr1[j],end=" ")"""
    
def reverse(num: int)->int:
    reversea=0
    ma=0
    temp=0
    mi=9
    while(num!=0):
        reversea=reversea*10+num%10
        temp=num%10
        num//=10
        if ma<temp:
            ma=temp 
        else:
            if temp<mi:
                mi=temp
        
    print(f"the difference of max and min is :",+(ma-mi))
    print(f"the max from the input number is :",+ma,+mi)
    return reversea

#well=int(input("enter a number:"))
print(f"the reversed number is",+reverse(436579))
"""def reverse_integer(num: int) -> int:
    reversed_num = 0
    while num != 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10
    return reversed_num
num=12345
print(reverse_integer(12345))"""