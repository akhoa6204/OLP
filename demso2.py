n=int(input())
A=map(int,input().split())
am = 0
duong = 0
for i in A:
    if i<0:
        am+=1
    elif i>0:
        duong+=1
print (am,duong)