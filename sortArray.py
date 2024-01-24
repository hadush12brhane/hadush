def sortArray(arr):
    n=len(arr)
    for i in range(n):
        for j in range (0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[2,4,7,1,9,0]
sortArray(arr)
print('the sorted array')
for i in range(len(arr)):
    print(arr[i],end=" ")
