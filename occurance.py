#Given 2 numbers N,K print the occurrences of K in N.
lis=input().split()
n=lis[0]
k=lis[1]
c=0
if((1<=int(n)<=100000)and(0<=int(k)<=9)):
  for i in n:
    if(i==k):
      c=c+1
	print(c)
else:
  print("Invalid Input")
