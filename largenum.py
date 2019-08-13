def largest(n):
    max=n[0]
    #print(n)
    for i in range(len(n)):
        if(n[i]>max):
            max=n[i]
    return max
n1=input().split()
lis=list(map(int,n1))
print(largest(lis))
