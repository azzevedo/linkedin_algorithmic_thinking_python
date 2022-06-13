doors = [False for i in range(1, 101)]

#1, #2, #3, #4, #5
c = 1
while c < 101:
    for i in range(c, 101, c):
        doors[i-1] = not doors[i-1]
    c += 1


print(doors)
