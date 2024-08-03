'''
Find list of N integers bw 1 to N such that the cost of applying reversort to it is C
Min cost for reversort = n-1 := already sorted array
Max cost for reversort = n(n-1)/2 - 1
'''

def rec_revsort(n, c, m):
    # Construct an array from M to N which, when revsorted incurs a cost of c
    if n==1:
        return str(m)
    else:
        # Bounds for n-1
        if ((c-1)>=n-2 and (c-1)<=n*(n-1)/2-1):
            # place x at the beginning and recurse directly
            return str(m) + " " + rec_revsort(n-1, c-1, m+1)
        else:
            diff = int(c - n*(n-1)/2 + 1)
            y = rec_revsort(n-1, c-diff, m+1)
            arr = y.split()
            new_arr = [str(m)]
            new_arr.extend(arr)
            return " ".join(new_arr[:diff][::-1] + new_arr[diff:])



no_of_tc = int(input())
for i in range(no_of_tc):
    n, c = map(int, input().split())
    if c<n-1 or c>(n*(n+1)/2)-1:
        print("Impossible")
    else:
        a = rec_revsort(n, c, 1)
        print(a)