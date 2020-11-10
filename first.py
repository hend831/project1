x=int(input('enter num1 '))
y=int(input('rnter num2 '))
z=x^2+2*x*y+y^2
w=x^3+x^2+2*x*y+y^2+y^3
h=max(z,w)
t=min(z,w)
a=z+w
b=a/2
c=z-w
d=z*w
f=z%w
g=z/w
print('z= ',z,'w= ',w,'max of z,w is ',h,'min of z,w is ',t,'a= ',a,'b= ',b,'c= ',c,'d= ',d,'f= ',f,'g= ',g)
if z>0:
    print('z is positive')
else:
    print('z is negative')

total=0
for m in range(10): 
    print(m)
    total=total+m
print(total)

for n in range (0,20,2):
    print(n)
print('yes')

i=1
while i<10 :
    print(i)
    i=i+1
print('good')

X=[3,7,6,2]
Y=[6,9,0,3,2,4]
for j in X :
    Y.append(j)
print(Y)

X.pop()
print(X)

l=[5,8,9,7,3,1]
l.sort()
print(l)
