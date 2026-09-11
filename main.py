import pygame as pg
pg.init()

screen = pg.display.set_mode((500,500))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((0,0,0))
    pg.draw.rect(screen, (255,255,255), (100,100,100,100))
    pg.display.flip()
pg.quit()