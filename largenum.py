def largest(n):
    max=0
    #print(n)
    for i in range(len(n)-1):
        if(n[i]>n[i+1]):
            max=n[i]
        else:
            max=n[i+1]
    return max
n1=input().split()
lis=list(map(int,n1))
print(largest(lis))
