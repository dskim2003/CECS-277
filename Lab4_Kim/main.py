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
    file = open('map.txt')
    map = []
    for row in file:
        items = row.strip().split(" ")
        list = []
        for item in items:
            list.append(int(item))
            map.append(list)
            print(map)
    return []
read_map()

def main():
    read_map
main()