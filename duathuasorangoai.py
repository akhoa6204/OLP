n=int(input())
for i in range (1,int(n**0.5 +1)):
    if n%(i*i)==0:
        a=i
print(a)