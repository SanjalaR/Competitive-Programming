arr = list(map(int, input().split()))
eve = []
odd = []
for i in range(len(arr)):
    if i % 2 == 0:
        eve.append(arr[i])
    else:
        odd.append(arr[i])
eve.sort()
odd.sort()
arr2 = []
j, k = 0, 0
for i in range(len(arr)):
    if i % 2 == 0:
        arr2.append(eve[j])
        j += 1
    else:
        arr2.append(odd[k])
        k += 1
print(arr2)
sort_arr = sorted(arr)
if arr2 == sort_arr:
    print("Yes! Trouble sort works on this")
else:
    print("No!")
    for i in range(len(arr2)):
        if arr2[i] != sort_arr[i]:
            print("Index of first mismatch: ", i)
            break
