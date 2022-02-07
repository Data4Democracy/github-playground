"""
Print Yanghui Triangle
1
11
121
1331
1 4 6 4 1
1 5 10 10 5 1
"""

def triangle():
    a=[1]
    while(len(a)<7):
        yield a
        i=0
        while(i<len(a)-1):
            a[i]=a[i]+a[i+1]
            i=i+1
        a.insert(0,1)
        a[-1]=1
        

for n in triangle():
    print(n)