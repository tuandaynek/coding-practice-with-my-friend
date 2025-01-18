import math

a, b, c = map(float, input().split())
delta = (b**2)-4*a*c
if(delta == 0):
    x = -b/(2*a)
    print(f"{x:.2f}")
elif(delta > 0):
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    print(f"{(max(x1, x2)):.2f}\n{(min(x1, x2)):.2f}")
else:
    print(-1)