#https://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/1
inp, item, count = [6, 5, 4, 5, 3, 4], [], []
for i in inp:
    if i not in item:
        item.append(i)
        count.append(inp.count(i))
for j in range(len(count)):
    for i in range(len(count)-1):
        if (count[i] == count[i+1] and item[i] > item[i+1]) or count[i] < count[i+1]:
            count[i+1], count[i] = count[i], count[i+1]
            item[i+1], item[i] = item[i], item[i+1]

for i in range(len(count)):
    print(str(item[i])*count[i], end='')
