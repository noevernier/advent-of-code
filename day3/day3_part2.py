engine = []
with open('day3/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        engine.append(list(line))
explored = [[False for i in range(len(engine[j]))] for j in range(len(engine))]
result = 0
for i in range(len(engine)):
    for j in range(len(engine[i])):
        if engine[i][j] == "*":
            list_of_adjacent_numbers = []
            for l in range(-1, 2):
                for p in range(-1, 2):
                    if i+l >= 0 and i+l < len(engine) and j+p >= 0 and j+p < len(engine[i]) and engine[i+l][j+p].isnumeric() and not explored[i+l][j+p]:
                        g, h = j+p, j+p
                        while g < len(engine[i]) and engine[i+l][g].isnumeric():
                            explored[i+l][g] = True
                            g += 1
                        while h >= 0 and engine[i+l][h].isnumeric():
                            explored[i+l][h] = True
                            h -= 1
                        print(i, j, l, p, g, h)
                        list_of_adjacent_numbers.append(int(''.join(engine[i+l][h+1:g])))
            if len(list_of_adjacent_numbers) == 2:
                result += list_of_adjacent_numbers[0]*list_of_adjacent_numbers[1]
print(result)