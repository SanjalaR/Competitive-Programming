'''
Imagine that you own a bookstore in downtown New York. Your shop sells a diverse range of books, of various popularity ranking. You sell New York best sellers as well as less popular titles. Each of these ranking are published at the end of each week by an autonomous organization. Lower ranking indicate more popular books, while higher ranking signify less popular ones.

One day you receive a large shipment of books. You realize that sorting these books in order of their popularity will boost sales and enhance the customer experience. However, the number of books n
 is really large for you to handle alone. To make this process of sorting you decide to hire workers. Money is no problem for you, so you can hire as many workers as needed.

Let's say you hire worker
 number of workers and you split the book shipment into book segments amongst the workers where each worker can get a different sized segment. Each of the workers, sort their books independently according to the popularity ranking.

What is the most number of workers you will hire such that at the end of the day, all your books are sorted by the popularity ranking?
'''

no_of_tc = int(input())

  
for i in range(no_of_tc):
  n = int(input())
  arr = list(map(int, input().split()))
  sa = sorted(arr)
  workers = 0
  curr_max = -1
  for i in range(n):
    if arr[i]>curr_max:
      curr_max = arr[i]
    if curr_max==sa[i]:
      workers+=1
      curr_max=-1
  print(workers)
