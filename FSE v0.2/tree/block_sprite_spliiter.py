from pygame import *
sprite,xsprit,ysprite,c = image.load("Tree_Tops.png"),3,1,0
for y in range(0, sprite.get_height(), int(sprite.get_height() / ysprite)):
    for x in range(0, sprite.get_width(), int(sprite.get_width() / xsprite)):
        image.save(sprite.subsurface((x, y, sprite.get_width() / xsprite - 2, sprite.get_height() / ysprite - 2)), "tree_branch_%i.png" %(c))
        c += 1
