x= int(input())
a=str(x)
l=len(a)
s=0
for i in a:
    s+=int(i)**l
if s==x:
    print(x,' is an amstrong number')
else:
    print('no')
    

