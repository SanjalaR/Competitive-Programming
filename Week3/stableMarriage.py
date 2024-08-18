T = int(input())

def rank(v, person, N):
    return N-v.index(person)

for _ in range(T):
    N = int(input())
    women = []
    men = []
    for i in range(N):
        women.append(list(map(int, input().split()))[1:])
        women[i].reverse()
    for i in range(N):
        men.append(list(map(int, input().split()))[1:])
        men[i].reverse()
    print(women)
    print(men)


    WE, ME = [-1]*N, [-1]*N
    print(WE, ME)
    while(-1 in WE):
        for i in range(N):
            if ME[i]==-1:
                top = men[i][-1] - 1
                men[i].pop()
                if WE[top] == -1:
                    WE[top] = i
                    ME[i] = top
                else:
                    comp = WE[top]
                    if rank(women[top], i+1, N) < rank(women[top], comp+1, N):
                        WE[top] = i
                        ME[i] = top
                        ME[comp] = -1
    for i in range(N):
        print(i+1, ME[i]+1)
