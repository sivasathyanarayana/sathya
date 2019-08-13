def alpha(n):
    s=ord(n)
    if(((s>=65)and(s<=90))or((s>=97)and(s<=122))):
       return "Alphabet"
    else:
       return "No"
n1=input()
print(alpha(n1))
