import pygame as pg
pg.init()

screen = pg.display.set_mode((500,500))

x = 100
y = 100

def Render(screen):
    pg.draw.rect(screen, (255,255,255), (x,y,100,100))

def Update(coo):
    coo[0] += 1
    coo[0] = min(max(0, coo[0]),300)

def isOkay():
    pass

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((0,0,0))
    Update([x])
    Render(screen)
    
    pg.display.flip()
pg.quit()