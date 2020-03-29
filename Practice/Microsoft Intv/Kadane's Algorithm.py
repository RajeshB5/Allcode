#Contiguous sub-array with maximum sum
n = [-2, -3, 4, -1, 3]
max_sub_till_now = n[0]
max_val = 0
for i in n:
    max_val += i
    if max_sub_till_now < max_val:
        max_sub_till_now = max_val
    if max_val < 0:
        max_val = 0
print(max_sub_till_now)
