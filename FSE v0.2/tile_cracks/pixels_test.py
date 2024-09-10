from pygame import *
dirt_blocks = image.load("TileCracks.png")
c = 0
for y in range(0, 72, 18):
    for x in range(0, 108, 18):
        image.save(dirt_blocks.subsurface((x, y, 16, 16)), "tile_crack_%i.png" %(c))
        c += 1
