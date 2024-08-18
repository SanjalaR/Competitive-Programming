T = int(input())
for i in range(T):
    N, M = list(map(int, input().strip().split()))
    req = []
    for i in range(M):
        r = tuple(map(int, input().strip().split()))
        req.append(r)
    req.sort(key = lambda x: x[1])
    ans = 0
    last = -1
    for r in req:
        if last > req[0]:
            continue
        else:
            last = req[1]
            ans += 1
    print(ans)