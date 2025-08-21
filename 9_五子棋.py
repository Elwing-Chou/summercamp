import pygame as pg
#pygame初始化
pg.init()

#設定視窗
width, height = 800, 800
screen = pg.display.set_mode((width, height))
pg.display.set_caption("五子棋")

#建立畫布bg
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((199, 167, 82))
screen.blit(bg, (0,0))
pg.display.update()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()