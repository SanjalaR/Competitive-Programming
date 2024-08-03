def rightmost_left(t):
    return max([x[i] - (v[i] * t) for i in range(n)])


def leftmost_right(t):
    return min([x[i] + (v[i] * t) for i in range(n)])


def is_feasible(k):
    return rightmost_left(k) <= leftmost_right(k)


n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))
L, R = 0.0, 1e9
while R - L > 1e-6:
    mid = (L + R) / 2
    if is_feasible(mid):
        R = mid
    else:
        L = mid
print(mid)
