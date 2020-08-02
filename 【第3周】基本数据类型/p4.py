str=input()
t=''
for c in str:
    if 'a'<=c<='z':
        c=chr(ord('a')+(ord(c)-ord('a')+3)%26)      
    elif  'A'<=c<='Z':
        c=chr(ord('A')+(ord(c)-ord('Z')+3)%26)           
    t=t+c
print(t)