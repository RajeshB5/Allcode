#https://practice.geeksforgeeks.org/problems/missing-number-in-array/0
for count in range(int(input())):
    m= int(input())
    a =sum(int(i) for i in input().split())
    print((m*(m+1))//2-a)