x=int(input('Enter the length of the series:'))
a=0
b=1
print(a, b, end=' ')
for i in range(x):
    z=a+b
    print(z,end=' ')
    a=b
    b=z
    
    
