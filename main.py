from funciones import draw_world_empty, draw_out, draw_world, draw_player, move_player, collect_blocks, destroy_blocks, \
    build, print_blocks_sleep
from time import sleep

print("Minecraft 2D\n")

while input() != "init":
    continue

SPF = float(input("Seconds per frame (recommended SPF= 0.20): "))

camera_position = 1
pj = [11, 2]

draw_world_empty()
background = draw_world()
draw_out(background, pj, camera_position)
sleep(SPF)

draw_out(draw_player(background, pj), pj, camera_position)
sleep(SPF)

wood_block = 0
stone_block = 0

while True:
    load = input().split(",")
    for i in load:
        if " " in i:
            i = i.split(" ")
            if i[0] == "build":
                wood_block, stone_block, background = build(background, pj, wood_block, stone_block, i[1])
                camera_position = draw_out(draw_player(background, pj), pj, camera_position)
                print_blocks_sleep(wood_block, stone_block, SPF)
            else:
                for ii in range(int(i[0])):
                    pj = move_player(i[1], pj)
                    camera_position = draw_out(draw_player(background, pj), pj, camera_position)
                    print_blocks_sleep(wood_block,stone_block,SPF)
        else:
            if i == "top" or i == "up" or i == "down" or i == "left" or i == "right":
                pj = move_player(i, pj)
                camera_position = draw_out(draw_player(background, pj), pj, camera_position)
            elif i == "extract":
                wood_block, stone_block, background = collect_blocks(background, pj, wood_block, stone_block)
                camera_position = draw_out(draw_player(background, pj), pj, camera_position)
            elif i == "destroy":
                destroy_blocks(background, pj)
                camera_position = draw_out(draw_player(background, pj), pj, camera_position)
            print_blocks_sleep(wood_block,stone_block,SPF)