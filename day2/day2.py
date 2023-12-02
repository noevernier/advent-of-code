color_dict = {
    'red': 0,
    'green': 1,
    'blue': 2
}
with open('day2/input.txt') as f:
    lines = f.readlines()
    game_limit = [12, 13, 14]
    sum_of_id_possible_game = 0
    for line in lines:
        possible = True
        line = line.strip()
        sets = line.split(':')[1].split(';')
        game_id = line.split(':')[0].split(' ')[1]

        for i in range(len(sets)):
            sets[i] = sets[i].strip().split(',')
            for j in range(len(sets[i])):
                sets[i][j] = sets[i][j].strip().split(' ')
                sets[i][j] = [int(sets[i][j][0]), sets[i][j][1]]
                if sets[i][j][0] > game_limit[color_dict[sets[i][j][1]]]:
                    possible = False
        if possible:
            sum_of_id_possible_game += int(game_id)

    print(sum_of_id_possible_game)