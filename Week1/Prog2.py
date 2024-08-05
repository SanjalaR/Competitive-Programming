'''
There is a photo-shoot going on at your school, and you are tasked to organize the photo-shoot. However, there is not much space in your campus for everyone to stand side by side for the group photo. You come up with the idea of making everyone stand in a queue and taking their photo from one side of the queue. There are n
 students in your class, and all are standing randomly in a queue for the photo. You are given the height of each of the student as an array of integers H
 where Hi
 is the height of the ith
 student in the queue from the left. Find out which side of the queue you should take the photo from so that everyone is visible.
 '''

def height(H):
  LH = sorted(H)
  RH = LH[::-1]
  if H==LH:
    return 'L'
  elif H==RH:
    return 'R'
  else:
    return 'N'
no_of_tc = int(input())
for i in range(no_of_tc):
  n = int(input())
  H = list(map(int, input().split()))
  print(height(H))
