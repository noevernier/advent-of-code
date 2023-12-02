color_dict = {
    'red': 0,
    'green': 1,
    'blue': 2
}
with open('day2/input.txt') as f:
    lines = f.readlines()
    total_power = 0
    for line in lines:
        current_game_limit = [0, 0, 0]
        power = 0
        possible = True
        line = line.strip()
        sets = line.split(':')[1].split(';')
        game_id = line.split(':')[0].split(' ')[1]
        
        for i in range(len(sets)):
            sets[i] = sets[i].strip().split(',')
            for j in range(len(sets[i])):
                sets[i][j] = sets[i][j].strip().split(' ')
                sets[i][j] = [int(sets[i][j][0]), sets[i][j][1]]
                current_game_limit[color_dict[sets[i][j][1]]] = max(current_game_limit[color_dict[sets[i][j][1]]], sets[i][j][0])
        total_power += current_game_limit[0]*current_game_limit[1]*current_game_limit[2]
    print(total_power)