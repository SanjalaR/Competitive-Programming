x1, y1 = list(map(int, input().split()))  # Origin
x2, y2 = list(map(int, input().split()))  # Destination
n = int(input())  # Length of weather forecast
S = input()  # Weather forecast

x, y = 0, 0
WL = [(0, 0)]

for s in S:
    if s == 'U':
        y += 1
    elif s == 'D':
        y -= 1
    elif s == 'R':
        x += 1
    elif s == 'L':
        x -= 1
    WL.append((x, y))

L, R = 0, 10 ** 15
done = False
while L != R:
    mid = (L + R) // 2
    Q, rem = divmod(mid, n)
    x3 = x1 + Q * x + WL[rem][0]
    y3 = y1 + Q * y + WL[rem][1]
    xoff = abs(x2 - x3)
    yoff = abs(y2 - y3)
    if (xoff + yoff) <= mid:
        R = mid
    else:
        L = mid + 1
    if L == 10 ** 15:
        print(-1)
        done = True
if not done:
    print(R)
