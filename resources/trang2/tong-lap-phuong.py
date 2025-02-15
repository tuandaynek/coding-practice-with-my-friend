#cách 1 (for):

n = int(input())
sum = 0
for i in range(1, n+1):
    sum+=(i**3)
print(sum)

#cách 2 (while):
n = int(input())
sum = 0
i = 1
while i <=n:
    sum+=(i**3)
    i+=1
print(sum)
