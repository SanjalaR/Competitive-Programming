from fractions import Fraction

def findMean(prefixSum, n, k, median):
    total = prefixSum[median+1] - prefixSum[median-k] + prefixSum[n] - prefixSum[n-k]
    return Fraction(total, (2*k+1))

n = int(input())
nums = sorted(list(map(int, input().split())))
bestSkew, bestK, bestMedian = 0,0,0

prefSum = [0]
for i in range(n):
    prefSum.append(prefSum[-1]+nums[i])

for median in range(1, n-1):
    rangeK = min(median, n-median+1)
    L, R = 0, rangeK
    mid = (L+R)//2
    while R>L:
        a = nums[n-mid-1]
        b = nums[median-mid-1]
        if (2*mid+1)*(a+b) <= 2*(prefSum[median+1] - prefSum[median-mid] + prefSum[n] - prefSum[n-mid]):
            R = mid
        else:
            L = mid+1
        mid = (L+R)//2
    bestMean = findMean(prefSum, n, L, median)
    if bestMean - nums[median] > bestSkew:
        bestSkew = bestMean - nums[median]
        bestMedian = median
        bestK = L

print(2*bestK+1)
for i in range(bestK):
    print(nums[n-1-i], end=' ')
for i in range(bestK+1):
    print(nums[bestMedian-i], end=' ')