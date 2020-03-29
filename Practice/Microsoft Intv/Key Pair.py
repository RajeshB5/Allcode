#https://practice.geeksforgeeks.org/problems/key-pair/0
for count in range(int(input())):
    find, f = int(input().split()[1]), 0
    inp = list(map(int, input().split()))
    for i in range(len(inp)-1):
        for j in range(i+1, len(inp)):
            if inp[i]+inp[j] == find:
                print("Yes")
                f = 1
                break
        else:
            continue
        break
    if f == 0:
        print("No")