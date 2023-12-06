import aoc_lube
import math
RAW = aoc_lube.fetch(year=2023, day=6)

def part_one():
    times, distances = RAW.split('\n')
    times = list(map(int, times.split(":")[1].split()))
    distances = list(map(int, distances.split(":")[1].split()))

    result = 1
    for t, d in zip(times, distances):
        x_1, x_2 = (t + math.sqrt(t**2 - 4*d))/2, (t - math.sqrt(t**2 - 4*d))/2
        n = math.floor(x_1) - math.floor(x_2)
        if x_1 == math.floor(x_1) or x_2 == math.floor(x_2):
            n -= 1
        result *= n
    return result

def part_two():
    times, distances = RAW.split('\n')
    t = int(times.split(":")[1].replace(" ", ""))
    d = int(distances.split(":")[1].replace(" ", ""))
    x_1, x_2 = (t + math.sqrt(t**2 - 4*d))/2, (t - math.sqrt(t**2 - 4*d))/2
    n = math.floor(x_1) - math.floor(x_2)
    if x_1 == math.floor(x_1) or x_2 == math.floor(x_2):
        n -= 1
    return n

aoc_lube.submit(year=2023, day=6, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=6, part=2, solution=part_two)