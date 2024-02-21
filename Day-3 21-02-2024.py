#problem-1 
'''#approach=1
#find duplicate elements inarray
n=int(input())
a=list(map(int,(input().split())))[:n]
for i in range(n):
    if a[i] in a[i+1:]:
        print(a[i])
        break'''
'''#approach-2
n=int(input())
a=list(map(int,(input().split())))
a.sort()
for i in range(n):
    if a[i]==a[i+1]:
         print(a[i])
         break '''
'''#approach-3
n=int(input())
a=list(map(int,(input().split())))
for i in a:
     c=a.count(i)
     if c>1:
         print(i)
'''

#problem -2
'''#approach-1
n=int(input())
a=list(map(int,input().split()))[:n]
unique=[]
for i in range(n):
     if a.count(a[i])==1:
          if a[i] in unique:
               continue
          else:
               unique.append(a[i])
for i in unique:
     print(i,end=" ")
     break'''

'''#approach-2
n=int(input())
for i in a:
     if a.count(i)==1:
          print(i,end="")
          break'''

#problem=3
'''#approach-1
a=[3,2,1,2]
a.sort()
print(a)'''


#problem -4
#approach-1

'''n=int(input())
a=tuple(map(int,input().split()))
for i in range(n):
    if i//10:
        print("go to first team")
    else:
       print("go to second team")
    break'''
'''#approach-2
t=int(input())
a=tuple(map(int,input().split()))
for i in range(t):'''

'''#approach-3
t=int(input())
for j in range (t):
    n=int(input())
    factors = []
    for j in range (1,n+1):
        if n%j==0:
            factors.append(j)
    ef=[]
    of=[]
    for j in factors:
        if j%2==0:
            ef.append(j)
        else:
            of.append(j)
    if len(ef)==len(of):
        print(1)
    else:
        print(0)'''

#problem-5
#approach-1
'''n=int(input())
i=int(input())
for i in range(n):
    for j in range(1,i+1):
        x=int(input())
    if i>=x:
        print("a")
    else:
        print("b")
        break'''

    #app-2
'''t=int(input())
for i in range(t):
    n,x=map(int,input().spilt())
    a=list(map(int,input().split()))[:n]#freshness
    b=list(map(int,input().split()))[:n]#cost
    c=0
    for j in range(n):
        if a[j]>=x:
            c=c+b[j]
    print(c)'''

#priblem-6
#check where the number is prime or not(one and itself)
#approach-1
'''t=int(input())
for i in range(t):
    n=int(input())
    c=0
    for j in range(2,int(n/2+1)):
        if n%j==0:
            c=c+1
            print(" not prime")
            break
    if c==0:
        print("prime")'''
#approach-2,bruteforce approach
'''n=int(input())
fc=[]
for i in range(1,n+1):
    if n%i==0:
        '''
#problem-7 



#problem-8
#approach-1 (print all the even perfect numbers in a given range)
n=int(input())
for i in range(1,n+1):
    factors=[]
    if i%2==0:
        for j in range(1,i):
            if i%j==0:
                factors.append(j)
        if sum(factors)==i:
            print(i)
