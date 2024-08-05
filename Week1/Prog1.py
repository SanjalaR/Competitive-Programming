'''
Eren is on a spree to conquer as many cities as possible in his journey of the rumbling. Each city is connected to one or more city in a directed or undirected way. Directed edges (a,b)
 mean he can go from city a
 to city b
, but not the other way around. Undirected edges mean both direction are viable for the path. After careful consideration, he has finalized a path from his starting city to the last destination city he wants to rumble. There are some cities in the path which can be pillaged multiple times, these are marked by self loops in the graph.
'''

def optpath(path):
  for i in path:
    if path.count(i)==2:
      return i
  return -1
no_of_tc = int(input())
for i in range(no_of_tc):
  inp = list(map(int, input().split()))
  n = inp[0]
  m = inp[1]
  path = [*map(int,input())]
  path.sort(reverse=True)
  print(optpath(path))
  
  
  
