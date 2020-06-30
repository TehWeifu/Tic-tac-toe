# write your code here
def game_state(array):
    o_count = 0
    x_count = 0
    other_char_count = 0
    winner = []

    if array[0] == array[1] and array[0] == array[2]:
        if array[0] == "X" or array[0] == "O":
            winner.append("{} wins".format(array[0]))
    if array[3] == array[4] and array[3] == array[5]:
        if array[3] == "X" or array[3] == "O":
            winner.append("{} wins".format(array[3]))
    if array[6] == array[7] and array[6] == array[8]:
        if array[6] == "X" or array[6] == "O":
            winner.append("{} wins".format(array[6]))

    if array[0] == array[3] and array[0] == array[6]:
        if array[0] == "X" or array[0] == "O":
            winner.append("{} wins".format(array[0]))
    if array[1] == array[4] and array[1] == array[7]:
        if array[1] == "X" or array[1] == "O":
            winner.append("{} wins".format(array[1]))
    if array[2] == array[5] and array[2] == array[8]:
        if array[2] == "X" or array[2] == "O":
            winner.append("{} wins".format(array[2]))

    if array[0] == array[4] and array[0] == array[8]:
        if array[0] == "X" or array[0] == "O":
            winner.append("{} wins".format(array[0]))
    if array[2] == array[4] and array[2] == array[6]:
        if array[2] == "X" or array[2] == "O":
            winner.append("{} wins".format(array[2]))

    for char in array:
        if char == "X":
            x_count += 1
        elif char == "O":
            o_count += 1
        else:
            other_char_count += 1

    if x_count + 1 < o_count or o_count + 1 < x_count:
        return "Impossible"

    if len(winner) == 0:
        if x_count + o_count == 9:
            return "Draw"
        else:
            return "Game not finished"
    elif len(winner) == 1:
        return winner[0]
    else:
        return "Impossible"


def transform_coordinates(x, y):
    i = 3 - y
    j = x - 1
    return i * 3 + j


last_player = 'O'
choice = "         "
array_of_chars = list(choice)

print("---------")
print("| {} {} {} |".format(array_of_chars[0], array_of_chars[1], array_of_chars[2]))
print("| {} {} {} |".format(array_of_chars[3], array_of_chars[4], array_of_chars[5]))
print("| {} {} {} |".format(array_of_chars[6], array_of_chars[7], array_of_chars[8]))
print("---------")

while game_state(array_of_chars) == "Game not finished":

    user_input = input("Enter the coordinates: ")
    user_input = user_input.split()


    while user_input[0].isnumeric() == False or user_input[1].isnumeric() == False:
        print("You should enter numbers!")
        user_input = input("Enter the coordinates: ")
        user_input = user_input.split()

    x_point = int(user_input[0])
    y_point = int(user_input[1])

    while x_point < 1 or x_point > 3 or y_point < 1 or y_point > 3:
        print("Coordinates should be from 1 to 3!")
        user_input = input("Enter the coordinates: ").split()
        x_point = int(user_input[0])
        y_point = int(user_input[1])

    coord = transform_coordinates(x_point, y_point)

    while array_of_chars[coord] == 'X' or array_of_chars[coord] == 'O':
        print("This cell is occupied! Choose another one!")
        user_input = input("Enter the coordinates: ").split()
        x_point = int(user_input[0])
        y_point = int(user_input[1])
        coord = transform_coordinates(x_point, y_point)

    if last_player == 'O':
        array_of_chars[coord] = 'X'
        last_player = 'X'
    else:
        array_of_chars[coord] = 'O'
        last_player = 'O'

    print("---------")
    print("| {} {} {} |".format(array_of_chars[0], array_of_chars[1], array_of_chars[2]))
    print("| {} {} {} |".format(array_of_chars[3], array_of_chars[4], array_of_chars[5]))
    print("| {} {} {} |".format(array_of_chars[6], array_of_chars[7], array_of_chars[8]))
    print("---------")

print(game_state(array_of_chars))
