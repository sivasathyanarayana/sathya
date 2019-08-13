def vowel(n):
    s=ord(n)
    t="AEIOU"
    if((s>=65)and(s<=90)):
        if(n in t):
            return "vowel"
        else:
            return "consonant"
    else:
        return "invalid"
n1=input().upper()
print(vowel(n1))
