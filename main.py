import pygame, time
from PyGM.master import *


pygame.display.init()
screen = pygame.display.set_mode((320, 240))
running = True
pygame.display.set_caption("PY-GM")
frame_id = 1

next_frame = time.time()


class GameTimer(Entity):
    def __init__(self, **kw):
        super(GameTimer, self).__init__(**kw)
        self.alarm = {"print_complete": 100, "end_game": 500}

    def print_complete(self):
        print "Completed!"

    def end_game(self):
        global running
        running = False
        print "game ended"

    def event_step(self):
        super(GameTimer, self).event_step()
        print self.alarm


class Tree(Entity):
    def __init__(self, **kw):
        super(Tree, self).__init__(**kw)

    def sayhi(self):
        print "hi"


NewGameRoom()
NewGameRoom.add_object(0, 0, GameTimer)
NewGameRoom.add_object(0, 0, Tree)
NewGameRoom.add_object(100, 0, Tree)
NewGameRoom.add_object(0, 0, Tree)
NewGameRoom.add_object(0, 0, Tree)

NewGameRoom.instance_destroy(NewGameRoom.type_nearest(100, 0, Tree))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    #make all objects in world preform step event
    NewGameRoom.room_step()


    pygame.display.flip()

