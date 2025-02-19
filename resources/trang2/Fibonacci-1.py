n = int(input())

def fibo(n):
    if(n==0): return 0
    if(n==1): return 1
    return fibo(n-1) + fibo(n-2)

f = []
for i in range(0, n+1):
    if(i==0): f.append(0)
    elif(i==1): f.append(1)
    else: f.append(f[i-1]+f[i-2])

print(f[n])
