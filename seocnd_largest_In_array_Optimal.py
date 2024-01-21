arr=[1,2,4,7,7,5]
largest=arr[0]
slarge=-1
for i in range(2,len(arr)):
    if(arr[i]==largest):
        pass

    elif(arr[i]>largest):
        temp=largest
        largest=arr[i]
        slarge=temp
    elif(arr[i]<largest and arr[i]>slarge):
        slarge=arr[i]
print(largest,slarge)
import sys
print(sys.maxsize)
            
