engine = []
with open('day3/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        engine.append(list(line))
result = 0
for i in range(len(engine)):
    j = 0
    while j < len(engine[i]):
        has_symbol = False
        if engine[i][j].isnumeric():
            k = j
            while k < len(engine[i]) and engine[i][k].isnumeric():
                for l in range(-1, 2):
                    for p in range(-1, 2):
                        if i+l >= 0 and i+l < len(engine) and k+p >= 0 and k+p < len(engine[i]) and not engine[i+l][k+p].isnumeric() and not engine[i+l][k+p] == '.':
                            has_symbol = True
                k += 1
        if has_symbol:
            result += int(''.join(engine[i][j:k]))
            j = k
        else:
            j += 1
            
print(result)