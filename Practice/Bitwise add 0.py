#https://www.hackerearth.com/problem/algorithm/day-5-1/
n = 6
run, Jatin = True, True
while run:
    if n == 1:
        break
    for i in range(n-1, 0, -1):
        run = False
        if not n & i:
            Jatin = False if Jatin else True
            n, run = n-i, True
            break
print('Pranshu'if Jatin else 'Jatin')