l=[1,2,3,4,7,4,90]

def fun(l):
    largest=l[0]
    for i in range(len(l)):
        if(l[i]>largest):
            largest=l[i]
    val=largest
    print(val)
    slargest=-1
    for i in range(len(l)):
        if(l[i]>slargest and val!=l[i]):
            slargest=l[i]
            print(slargest)
    print(slargest)
    return val,slargest


res=fun(l)
print(res)       