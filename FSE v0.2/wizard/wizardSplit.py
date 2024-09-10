from pygame import *
thing,newSurface,c = image.load("NPC_188.png"),Surface((34, 142), SRCALPHA),0
newSurface.blit(thing, (0, 0))
for i in range(0, 142, int(142/3)):
    name = "skeleton_" + str(c) + ".png"
    image.save(newSurface.subsurface(0, i, 34, int(142/3)), name)
    c += 1