n = int(input())

f = []
for i in range(0, n+1):
    if(i==0): f.append(0)
    elif(i==1): f.append(1)
    else: f.append(f[i-1]+f[i-2])

print(f[n])
