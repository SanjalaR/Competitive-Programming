'''
There are N boxes. The i-th box a[i] packets of Maggi. So, by picking up the i-th box, you grab a[i] packets of Maggi.

There are Q queries regarding these boxes. For the j-th query you have to answer what is the minimum number of boxes you need to pick up to own at least x[j] packs of Maggi, or print -1 if it's not possible to obtain such a quantity.

In other words, you should print the minimum possible K such that after picking K boxes, you have at least x[j] packets of Maggi. Note that one box can be chosen once only, and queries are independent of each other (you can use the same box for different queries).
'''
no_of_tc = int(input())
for i in range(no_of_tc):
  inp = input().split()
  N = int(inp[0])
  Q = int(inp[1])
  packets = list(map(int, input().split()))
  packets.sort(reverse=True)
  for i in range(Q):
    j = int(input())
    summ = 0
    count = 0
    while summ<j and count<len(packets):
      summ+=packets[count]
      count+=1
    if summ<j:
      print(-1)
    else:
      print(count)
                                  
