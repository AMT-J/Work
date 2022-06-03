import random
N=100
a=[random.randint(1,N) for i in range(N)]
print(a)
for i in range(N):
    for j in range(N-1,i,-1):
        if a[j-1]>a[j]:
            a[j-1],a[j]=a[j],a[j-1]
print(a)
random.shuffle(a)
for i in range(N):
    for j in range(0,N-i-1):
        if a[j+1]<a[j]:
            a[j+1],a[j]=a[j],a[j+1]
print(a)