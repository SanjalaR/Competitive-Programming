'''
You work at a popular thrift shop in Los Angeles where people donate various clothing items for the goodwill of the community. One day, you receive a large shipment of donations with multiple boxes. Each box contains different number of clothing items. Your job at the store, is to sort through these boxes and display them before your shift ends that day.

You have n
 hours left on your shift to end from the time you start sorting through these boxes. When you start sorting through one box and displaying them, should you finish your work before that hour ends, you take a coffee break until the next hour to break open the next box of clothing.

Given the donations
 array which logs the number of clothing items in each box, find a minimum rate of sorting k
 (in number of clothing items per hour) to sort all the items and display them before your shift ends.
'''
import math
no_of_tc = int(input())
for i in range(no_of_tc):
  inp = input().split()
  n = int(inp[0])
  l = int(inp[1])
  arr = list(map(int, input().split()))
  L, R = 1, max(arr)
  while L<R:
    mid = (L+R)//2
    hrs = 0
    flag = True
    for i in arr:
      hrs+=math.ceil(i/mid)
      if hrs>n:
        flag = False
        break
    if flag:
      R = mid
    else:
      L = mid+1
  print(L)
