n, x, k = map(int, input().split())
conLai = x - (n*k)
chiaDeu = conLai // n
du = conLai % n
lessSticker = n - du
if du==0: lessSticker = du

print(chiaDeu, lessSticker)
