from colorama import Style, Back, Fore
from time import sleep

def draw_out(map_name, pj, cam_pos):
    print("\nMundo XYZ")
    cp = cam_pos  # posicion de la camara extremo 1
    cp2 = cam_pos + 29  # posicion de la camara extremo 2

    if cp2 - pj[1] <= 7:
        if 40 - pj[1] >= 7:
            cp = cp + 1
    elif pj[1] - cp <= 7:
        if pj[1] >= 7 and not (cp <= 1):
            cp = cp - 1

    for y in map_name:
        for x in y[cp:cp + 30]:
            if x == "V":
                print(Style.RESET_ALL + '   ', end="")
            elif x == "B":
                print(Back.BLACK + '   ', end="")
            elif x == "R":
                print(Back.RED + '   ', end="")
            elif x == "G":
                print(Back.GREEN + '   ', end="")
            elif x == "Y":
                print(Back.YELLOW + '   ', end="")
            elif x == "A":
                print(Back.BLUE + '   ', end="")
            elif x == "W":
                print(Back.WHITE + '   ', end="")
            elif x == "C":
                print(Back.CYAN + '   ', end="")
            elif x == "M":
                print(Back.MAGENTA + '   ', end="")
        print(Style.RESET_ALL)

    return cp


def draw_world_empty():
    map = []
    templist = []
    for i in range(1, 21, 1):
        for x in range(1, 31, 1):
            templist.append("V")
        map.append(templist)
        templist = []

    draw_out(map, [11, 2], 0)
    return map


def draw_world():
    map_world = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        [1, "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V",
         "V", "V", "V", "V", "V", "V", "Y", "Y", "Y", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V"],
        [2, "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V",
         "V", "V", "V", "V", "V", "Y", "Y", "Y", "Y", "Y", "V", "V", "V", "V", "V", "V", "V", "V", "V"],
        [3, "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V",
         "G", "V", "V", "V", "V", "V", "Y", "Y", "Y", "V", "V", "V", "V", "V", "V", "G", "V", "V", "V"],
        [4, "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "G",
         "G", "G", "V", "V", "V", "Y", "V", "Y", "V", "Y", "V", "V", "V", "V", "G", "G", "G", "V", "V"],
        [5, "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "G", "G",
         "G", "G", "G", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "G", "G", "G", "G", "G", "V"],
        [6, "V", "V", "V", "V", "G", "V", "V", "V", "V", "V", "G", "V", "V", "V", "V", "V", "G", "V", "G", "G", "G",
         "G", "G", "G", "G", "V", "V", "V", "V", "V", "V", "V", "V", "G", "G", "G", "G", "G", "G", "G"],
        [7, "V", "V", "V", "G", "G", "G", "V", "V", "V", "G", "G", "G", "V", "V", "V", "G", "G", "G", "V", "V", "V",
         "R", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "R", "V", "V", "V"],
        [8, "V", "V", "G", "G", "G", "G", "G", "V", "G", "G", "G", "G", "G", "V", "G", "G", "G", "G", "G", "V", "V",
         "R", "V", "V", "G", "V", "V", "V", "G", "V", "V", "V", "V", "V", "V", "V", "R", "V", "G", "V"],
        [9, "V", "V", "V", "V", "R", "V", "V", "V", "V", "V", "R", "V", "V", "V", "V", "V", "R", "V", "V", "V", "V",
         "R", "V", "G", "G", "G", "V", "G", "G", "G", "V", "V", "V", "V", "V", "V", "R", "G", "G", "G"],
        [10, "V", "V", "V", "V", "R", "V", "V", "W", "V", "V", "R", "V", "V", "V", "V", "V", "R", "V", "V", "V", "V",
         "R", "V", "V", "R", "V", "V", "V", "R", "V", "V", "V", "V", "V", "V", "V", "R", "V", "R", "V"],
        [11, "V", "V", "V", "V", "R", "V", "W", "W", "W", "V", "R", "V", "V", "V", "V", "W", "R", "V", "V", "V", "V",
         "R", "V", "V", "R", "V", "V", "V", "R", "V", "V", "V", "V", "V", "V", "V", "R", "V", "R", "V"],
        [12, "V", "V", "V", "V", "R", "V", "W", "W", "W", "V", "R", "W", "V", "V", "W", "W", "R", "V", "V", "W", "V",
         "R", "V", "V", "R", "V", "V", "V", "R", "W", "V", "V", "V", "V", "W", "V", "R", "V", "R", "V"],
        [13, "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G",
         "G", "G", "G", "G", "A", "A", "A", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G"],
        [14, "B", "B", "B", "B", "W", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B",
         "B", "B", "B", "B", "A", "A", "A", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
        [15, "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B",
         "B", "W", "B", "W", "A", "A", "A", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
        [16, "B", "B", "B", "B", "B", "B", "W", "B", "B", "W", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B",
         "B", "W", "B", "B", "A", "A", "A", "B", "B", "B", "B", "B", "W", "B", "B", "W", "B", "B", "B"],
        [17, "B", "W", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B",
         "B", "W", "B", "B", "A", "A", "A", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
        [18, "B", "B", "B", "B", "W", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B",
         "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "W", "B", "B", "W"],
        [19, "B", "B", "B", "B", "B", "B", "W", "B", "B", "B", "B", "B", "B", "B", "W", "B", "B", "B", "B", "B", "B",
         "B", "B", "B", "B", "B", "B", "B", "W", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
        [20, "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B",
         "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"]]
    return map_world


def draw_player(map_name, pj):
    new_map = [[x for x in i] for i in map_name]
    y = pj[0]
    x = pj[1]
    new_map[y + 1][x] = "C"
    new_map[y][x] = "C"
    new_map[y - 1][x] = "C"
    new_map[y][x + 1] = "M"

    return new_map


def move_player(option, pj):
    if (pj[0] == 19 and option == "down") or (pj[0] == 2 and option == "up" or option == "top") or (pj[1] == 1 and option == "left") or (pj[1] == 39 and option == "right"):
        print(Fore.RED + "Invalid Operation", Style.RESET_ALL)

    elif option == "top" or option == "up":
        pj[0] = pj[0] - 1

    elif option == "down":
        pj[0] = pj[0] + 1

    elif option == "left":
        pj[1] = pj[1] - 1

    elif option == "right":
        pj[1] = pj[1] + 1

    return pj


def collect_blocks(background, pj, wood_block, stone_block):
    if background[pj[0]][pj[1] + 1] == "R":
        wood_block = wood_block + 1
        background[pj[0]][pj[1] + 1] = "V"
    elif background[pj[0]][pj[1] + 1] == "W":
        stone_block = stone_block + 1
        background[pj[0]][pj[1] + 1] = "V"

    return wood_block, stone_block, background


def destroy_blocks(background, pj):
    if background[pj[0]][pj[1] + 1] == "B":
        background[pj[0]][pj[1] + 1] = "V"
    elif background[pj[0]][pj[1] + 1] == "A":
        background[pj[0]][pj[1] + 1] = "V"
    elif background[pj[0]][pj[1] + 1] == "G":
        background[pj[0]][pj[1] + 1] = "V"
    elif background[pj[0]][pj[1] + 1] == "Y":
        background[pj[0]][pj[1] + 1] = "V"

    return background


def build(background, pj, wood_block, stone_block, intended_block):
    if background[pj[0]][pj[1] + 1] != "V" or (intended_block == "wood" and wood_block == 0) or (intended_block == "stone" and stone_block == 0):
        print(Fore.RED + "Invalid Operation", Style.RESET_ALL)

    else:
        if intended_block == "stone":
            background[pj[0]][pj[1] + 1] = "W"
            stone_block = stone_block - 1
        else:
            background[pj[0]][pj[1] + 1] = "R"
            wood_block = wood_block - 1
    return wood_block, stone_block, background


def print_blocks_sleep(wood_block,stone_block,SPF):
    print(Fore.BLACK + Back.LIGHTRED_EX + "wood blocks: ", wood_block, Style.RESET_ALL)
    print(Fore.BLACK + Back.LIGHTBLACK_EX + "stone blocks:", stone_block, Style.RESET_ALL, "\n")
    sleep(SPF)
