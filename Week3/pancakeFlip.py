T = int(input())
for i in range(T):
    X = input().split()
    S = X[0]  # array of states
    K = int(X[1])  # size of flipper
    N = len(S)
    obs = [0 for _ in range(N)]
    ans = 0
    for j in range(N-K+1):
        state = S[j]
        obs[j] += obs[j-1]
        flipped = ans - obs[j]
        if (state=='+' and flipped%2!=0) or (state=='-' and flipped%2==0):
            ans+=1
            if j<N-K:
                obs[j+K] +=1
    for j in range(N-K+1, N):
        obs[j] += obs[j-1]
        flipped = ans - obs[j]
        state = S[j]
        if (state == '+' and flipped % 2 != 0) or (state == '-' and flipped % 2 == 0):
            ans = 'IMPOSSIBLE'
            break
    print(ans)