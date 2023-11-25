arr=[1,2,3,4,5,6,7]
k=3
temp=arr[0:k]
for i in range(k,len(arr)):
    arr[i-k]=arr[i]

for i in range(len(arr)-k,len(arr)):
    arr[i]=temp[i-(len(arr)-k)]
    
print(arr)
