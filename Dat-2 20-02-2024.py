'''def myfun(x):
    x[0]=20
lst=[10,11,12,13,14,15]
myfun(lst)
print(lst)'''
'''#sugarcane juice wpwr approach 1
def profit(n):
    t=n*50
    b=t*0.2
    m=t*0.2
    r=t*0.3
    return (int(t-b-m-r))
for i in range(int(input())):
    n=(int(input()))
    print(profit(n))

# approach_2 
t=int(input())
while t>0:'''

'''#approach 4
t=int(input())
def profit(n):
    x=int((n*50)-((0.7)*n*50))
    return x
def test(t):
    if t>0:
        n=int(input())
        print(profit(n))
    else:
        return
    test(t-1)
test(t)'''

'''#watching movie at 2x app 1
def movie(x,y):
    total=((x-y)+(y/2))
    print(int(total))
x,y=map(int,input().split())
movie(x,y)'''
'''# approach 2
x,y=map(int,input().split())
print((x-y)+(y//2))'''
'''#approach-3
x,y=map(int,input().split())
def movie(x,y):
    total=(x-y//2)
    print(total)
movie(x,y)'''

'''#W lucky four approach-1 without using functions
t=int(input())
for i in range(t):
    n=int(input())
    c=0
    while n>0:
        if n%10==4:
            c=c+1
            n=n//10
        print(c) 
# approch 2,1 recursive 
def test(n):
    if t==0:
        return '''
'''#x-compute N!approach-1,for loop
n=int(input())
for i in range(1,n+1):
    r=r*i
print(r)'''
'''#approach-2 
n=int(input())
r=1
while n>0:
    r=r*n
    n=n-1
print(r)'''

'''# append three logic
123/1000
0.123+3
3.123*1000
3.123*10+3
31233'''
'''# append three 
for i in range(int(input())):
    n=int(input())
if n>0:
    n=((n*10)+3)
print(n)'''
# approach-2
n=int(input())
def temp(n):
    r=n
    c=0
    while r>0:
        c+=1
        r=r//10
    n=(3*pow(10,c))+n
    n=n*10+3
    return n
print(temp(n))