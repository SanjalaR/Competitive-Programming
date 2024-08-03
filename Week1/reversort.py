'''
Algo:
Reversort(L):
    for i := 1 to length(L)-1:
        j := position with min value in L bw i and length(L) (incl)
        Reverse(L[1...j])
        cost+=(j-i+1)
Max cost: Reverse the array at every step := L+(L-1)+(L-2)+....+2
'''


def reversort(L):
    cost = 0
    for i in range(len(L)-1):
        j = L.index(min(L[i:]))
        L[i:j+1] = reversed(L[i:j+1])
        cost += (j - i + 1)
    print(L)
    print(cost)


no_of_tc = int(input())
for i in range(no_of_tc):
    n = int(input())
    L = list(map(int, input().split()))
    reversort(L)
