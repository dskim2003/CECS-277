# Name: David Kim
# Date: 09/19/2024
# Desc: creates a game where user must collect treasure and avoid traps

def read_map():
    """
    Reads in map.txt and stores in list
    Args:

    Returns:
        filled list
    """
    file = open("map.txt")
    map = []
    for row in file:
        list = []
        for item in row:
            if item != ' ' and item != '\n':
                list.append(item)
        map.append(list)
    return map

def display_map(map, player):
    """
    displays map in matrix format, shows player's position
    Args:
        map: map list
        player: player coordinates
    Returns:

    """
    y_pos = 0
    for row in map:
        x_pos = 0
        for letter in row:
            if x_pos == player[1] and y_pos == player[0]:
                print('P', end=" ")
                x_pos += 1
                continue
            print(letter, end=" ")
            x_pos += 1
        print("\n")
        y_pos += 1
            

def move_player(player, dir, upper_bound):
    """
    updates player's location within map
    Args:
        player: location of player stored in list
        dir: direction of movement
        upper_bound: bounds of map
    Returns:
    """
    if dir.lower() == 'w' and player[0] != 0:
        player[0] -= 1
    elif dir.lower() == 'a' and player[1] != 0:
        player[1] -= 1
    elif dir.lower() == 's' and player[0] < upper_bound:
        player[0] += 1
    elif dir.lower() == 'd' and player[1] < upper_bound:
        player[1] += 1
    else:
        print("You cannot move that direction.")
    
def count_treasures_traps(map, player, upper_bound):
    T = 0
    X = 0
    for y in range(3):
        for x in range(3):
            if map[player[0] - 1 + y][player[1] - 1 + x] == 'T':
                T += 1
            if map[player[0] - 1 + y][player[1] - 1 + x] == 'X':
                X += 1

    return T, X
def main():
    treasure_count = 0
    map_hidden = read_map()
    map_display = []
    for i in range(7):
        list = []
        for j in range(7):
            list.append('.')
        map_display.append(list)
    user_location = [0,0]
    print("Treasure Hunt!")
    print("Find the 7 treasures without getting caught in a trap. Look around to spot nearby traps and treasures.")
    display_map(map_display, user_location)
    while True:
        user_input = input("Enter Direction (WASD or L to look around or Q to quit\n")
        if user_input.lower() == 'w' or user_input.lower() == 'a' or user_input.lower() == 's' or user_input.lower() == 'd':
            move_player(user_location, user_input, 6)
            if map_hidden[user_location[0]][user_location[1]] == 'T':
                treasure_count += 1
                map_hidden[user_location[0]][user_location[1]] = '.'
                map_display[user_location[0]][user_location[1]] = 'T'
                print("You found treasure!")
                print("There are " + str(7-treasure_count) + " treasures remaining.")
            if map_hidden[user_location[0]][user_location[1]] == 'X':
                print("You were caught in a trap!")
                print("You found " + str(treasure_count) + " treasure(s).")
                display_map(map_display, user_location)
                break
        elif user_input.lower() == 'q':
            break
        elif user_input.lower() == 'l':
            treasure, traps = count_treasures_traps(map_hidden, user_location, 6)
            print("You detect " + str(treasure) + " treasures nearby.")
            print("You detect " + str(traps) + " traps nearby.")
        else:
            print("Invalid input.")
        display_map(map_display, user_location)

        if treasure_count == 7:
            print("You Win!")
            break
    print("Game Over!")
main()