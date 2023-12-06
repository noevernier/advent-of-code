import aoc_lube

RAW = aoc_lube.fetch(year=2023, day=5)

def part_one():
    i = 0
    parts = RAW.split('\n\n')
    _, seeds = parts[0].split(':')
    seeds = list(map(int, seeds.split()))
    for part in parts[1:]:
        map_ = {}
        i+=1
        _, part = part.split(':')
        done = [False] * len(seeds)
        for line in part.strip().split('\n'):
            dest_start, source_start, range_ = list(map(int, line.split()))
            for idx, seed in enumerate(seeds):
                if seed >= source_start and seed < source_start + range_ and not done[idx]:
                    seeds[idx] = dest_start + (seed - source_start)
                    done[idx] = True
    return min(seeds)

def part_two():
    i = 0
    parts = RAW.split('\n\n')
    _, seeds_ = parts[0].split(':')
    seeds_ = list(map(int, seeds_.split()))
    seeds = []
    for i in range(0, len(seeds_)-1, 2):
        for j in range(seeds_[i+1]):
            seeds.append(seeds_[i] + i)
    print(seeds)
    # for part in parts[1:]:
    #     map_ = {}
    #     i+=1
    #     _, part = part.split(':')
    #     done = [False] * len(seeds)
    #     for line in part.strip().split('\n'):
    #         dest_start, source_start, range_ = list(map(int, line.split()))
    #         for idx, seed in enumerate(seeds):
    #             if seed >= source_start and seed < source_start + range_ and not done[idx]:
    #                 seeds[idx] = dest_start + (seed - source_start)
    #                 done[idx] = True
    # return min(seeds)
            

#aoc_lube.submit(year=2023, day=5, part=1, solution=part_one)
part_two()