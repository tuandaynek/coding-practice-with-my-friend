a, b, c = map(int, input().split())
if a+b<c or a+c<b or b+c<a:
    print("NO");
else: print("YES")