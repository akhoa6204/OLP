a=str(input())
b=str(input())
D1=[0]*26
D2=[0]*26
dem=0
for i in a : 
    i=ord(i)-97
    D1[i]+=1
for i in b : 
    i=ord(i)-97
    D2[i]+=1
for i in range (26):
    if min(D1[i],D2[i])==0:
        dem+=max(D1[i],D2[i])
print(dem)
    