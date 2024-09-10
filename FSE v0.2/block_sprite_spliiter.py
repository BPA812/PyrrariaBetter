from pygame import *
dirt_blocks,c = image.load("Tiles_6.png"),0
for y in range(0, 270, 18):
    for x in range(0, 288, 18):
        image.save(dirt_blocks.subsurface((x, y, 16, 16)), "ironore/ironore_block_%i.png" %(c))
        c += 1