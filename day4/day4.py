import aoc_lube

RAW = aoc_lube.fetch(year=2023, day=4)

def part_one():
    result = 0
    for line in RAW.split('\n'):
        id_, set_ = line.split(':')
        winning_set, playing_set = set_.split('|')
        winning_set = list(map(int, winning_set.strip().split()))
        playing_set = list(map(int, playing_set.strip().split()))

        result_set = list(map(lambda x: x in winning_set, playing_set))
        num_of_wins = sum(result_set)
        if num_of_wins > 0:
            result += 2**(num_of_wins-1)
    return result

def part_two():
    current_state = [1] * len(RAW.split('\n'))
    for idx, line in enumerate(RAW.split('\n')):
        id_, set_ = line.split(':')
        winning_set, playing_set = set_.split('|')

        winning_set = list(map(int, winning_set.strip().split()))
        playing_set = list(map(int, playing_set.strip().split()))

        result_set = list(map(lambda x: x in winning_set, playing_set))
        num_of_wins = sum(result_set)

        for i in range(idx+1, idx+num_of_wins+1):
            current_state[i] += current_state[idx]
        
    return sum(current_state)

aoc_lube.submit(year=2023, day=4, part=1, solution=part_one)
aoc_lube.submit(year=2023, day=4, part=2, solution=part_two)