total_calibration = 0
with open('day1/input.txt') as f:
    lines = f.readlines()

    for line in lines:
        i, j = 0, len(line)-1
        while ord(line[i]) not in range(49, 58):
            i += 1
        while ord(line[j]) not in range(49, 58):
            j -= 1
        total_calibration += 10*int(line[i]) + int(line[j])
print(total_calibration)
