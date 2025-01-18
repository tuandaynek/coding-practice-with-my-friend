import math #thư viện dùng để sử dụng để tìm căn của một số trong bài toán này

a, b, c = map(float, input().split())
delta = (b**2)-4*a*c
if(delta == 0):
    x = -b/(2*a)
    print(f"{x:.2f}") #làm tròn 2 chữ số sau dấu phẩy
elif(delta > 0):
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    print(f"{(max(x1, x2)):.2f}\n{(min(x1, x2)):.2f}")
else:
    print(-1)

"""
Các mấu chốt để giải được bài tập này::
- kiến thức về thư viện bên ngoài (import math)
- cách làm tròn số thập phân (x:.2f)
- nhập các số trên cùng 1 dòng (split())
- kiến thức xuống dòng (\n)
- kiến thức chèn một biến vào trong lệnh print (print(f"{}"))
"""
