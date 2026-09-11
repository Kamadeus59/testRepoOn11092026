import pygame as pg
pg.init()

screen = pg.display.set_mode((500,500))

x = 100
y = 100

def Render(screen,x,y):
    pg.draw.rect(screen, (255,255,255), (x,y,100,100))

def Update(events):
    global x,y
    keys = pg.key.get_pressed()
    if keys[pg.K_d]:
        x += 1
    if keys[pg.K_q]:
        x -= 1
    x = x%400
    if keys[pg.K_z]:
        y -= 1
    if keys[pg.K_s]:
        y += 1
    y = y%400



running = True
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
    screen.fill((0,0,0))

    Update(events)
    Render(screen,x,y)
    print(x)
    
    pg.display.flip()
pg.quit()