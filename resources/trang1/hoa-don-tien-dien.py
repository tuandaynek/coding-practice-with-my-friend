x, a, b, c, d = map(int, input().split())
ans = 0

if 0 <= x <= 50:
    ans = ans + x*a
elif 51 <= x <= 100:
    ans = ans + 50*a + (x-50)*b
elif 101 <= x <= 150:
    ans = ans + 50*a + 50*b + (x-100)*c
else:
    ans = ans + 50*a + 50*b + 50*c + (x-150)*d

print(ans)