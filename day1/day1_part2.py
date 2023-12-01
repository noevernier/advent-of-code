total_calibration = 0
spelled_numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five':5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

with open('day1/input_part2.txt') as f:
    lines = f.readlines()

    for line in lines:

        left_buffer = []
        right_buffer = []

        left_number = 0
        right_number = 0

        find_left = False
        find_right = False

        k, l = 0, len(line)-1

        while not find_left:

            left_buffer =  left_buffer + [line[k]]

            if ord(line[k]) in range(49, 58):
                left_number = int(line[k])
                find_left = True
            else:
                for number in spelled_numbers.keys():
                    if number in ''.join(left_buffer):
                        left_number = spelled_numbers[number]
                        find_left = True
            k+=1

        while not find_right:   
            right_buffer = [line[l]] + right_buffer

            if ord(line[l]) in range(49, 58):
                right_number = int(line[l])
                find_right = True
            else:
                for number in spelled_numbers.keys():
                    print(right_buffer)
                    if number in ''.join(right_buffer):
                        print(number)
                        right_number = spelled_numbers[number]
                        find_right = True
            l -= 1
        print(line)
        print("left : ", left_number, "   right : ", right_number)  
        total_calibration += 10*left_number + right_number
print(total_calibration)
