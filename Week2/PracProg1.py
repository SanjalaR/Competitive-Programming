'''
You have to take a group photo of 2N people. The i-th person has height H[i] units.

You organize these people into two two rows consisting of N people each.

To ensure that everyone is seen properly, the j-th person of the back row must be at least X units taller than the j-th person of the front row for each j between 1 and N, inclusive.

Is this possible?
'''

no_of_tc = int(input())
for i in range(no_of_tc):
  inp = input().split()
  N = int(inp[0])
  X = int(inp[1])
  arr = list(map(int, input().split()))
  arr.sort()
  row1 = arr[:N]
  row2 = arr[N:]
  flag = True
  for i in range(N):
    if row2[i]-row1[i]<X:
      flag = False
  if flag:
    print("YES")
  else:
    print("NO")
