#cách 1 (for):

n = int(input())
count=0
odd = 0
even = 0

for i in range(1, n+1):
    print(i, end=" ")
    count+=1
    if count%10==0: print("")
    if i%2==0 : even+=i
    else: odd+=i

print(f"\n{even}\n{odd}")

#cách 2 (while):

n = int(input())
count=0
odd=0
even=0
i=1
while i <= n:
    print(i, end=" ")
    count+=1
    if count%10==0: print("")
    if i%2==0: even+=i
    else: odd+=i
    i+=1

print(f"\n{even}\n{odd}")
