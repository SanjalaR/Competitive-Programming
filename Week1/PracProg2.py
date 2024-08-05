'''
At a party, there are n cups of gulab jamun arranged in a circle. A fly is sitting in one of the cups at the moment.

After minute number k, the fly jumps over k - 1 cups (clockwise) and lands and the next one. For example, after the first minute the fly ends up at the neighboring cup, and after that at the third cup from the start.

You should answer: will the fly visit all the cups or not?

We assume that fly is jumping forever.
'''
import math
def fly(n):
  for k in range(2, n+1):
    if n%k==0 and n//k<=k:
      return('NO')
  return('YES')
n = int(input())
if n==1:
  print('YES', end='')
else:
  print(fly(n), end='')

    
  
