# 1) Get count of all set bits at odd positions (For 23 it’s 3).
# 2) Get count of all set bits at even positions (For 23 it’s 1).
# 3) If difference of above two counts is a multiple of 3 then number is also a multiple of 3.
ode, eve = 0, 0
n = str(110000001001011000111110001010110001111000101110100010001111111111101000001001010101011100100)
for i in range(len(n)):
    if i % 2 == 0 and n[i] == '1':
        eve += 1
    elif i % 2 != 0 and n[i] == '1':
        ode += 1
if abs((ode-eve) % 3 == 0):
    print(1)
else:
    print(0)