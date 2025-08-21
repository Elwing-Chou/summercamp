import pygame as pg
#pygame初始化
pg.init()

#設定視窗
width, height = 640, 640
# 產生視窗
screen = pg.display.set_mode((width, height))
# 設定遊戲標題
pg.display.set_caption("五子棋")

# 建立畫布bg
bg = pg.Surface(screen.get_size())
# 把畫布填滿某個顏色
bg.fill((199, 167, 82))

# 把棋盤的直線畫出來(直線與直線間隔40)
# pygame.draw.line(畫布, 顏色, (x坐標1, y坐標1), (x坐標2, y坐標2), 線寬)
# 棋盤跟最左最右空隙45
for i in range(15):
    pg.draw.line(bg, (75, 75, 75), (40, 40+40*i), (600, 40+40*i), 2)
for i in range(15):
    pg.draw.line(bg, (75, 75, 75), (40+40*i, 40), (40+40*i, 600), 2)

# 把某個圖層貼到上一層
screen.blit(bg, (0,0))
# 對畫面進行更新(才會真的秀出來)
pg.display.update()

# 建立一個永不結束的迴圈(遊戲才不會結束)
# 第幾回合
game_round = 0
running = True
while running:
    # 收取你的遊戲任何事件(滑鼠點擊/鍵盤按鈕...)
    for event in pg.event.get():
        # 偵測滑鼠點擊以後放掉的動作
        if event.type == pg.MOUSEBUTTONUP:
            # 因為每一個都是40, 我只要計算點擊的座標落在(1.5)(1.6)(1.2)
            # 得到x, y座標
            x, y = pg.mouse.get_pos()
            # 找最近的一格 1.5->2 1.2->1 1.6->2
            x_inter, y_inter = round(x / 40), round(y / 40)
            # 如果落在0格, 16格都不做事
            if 0 < x_inter <= 15 and 0 < y_inter <= 15:
                # pygame.draw.circle(畫布, 顏色, (圓心x坐標, 圓心y坐標), 半徑, 線寬)
                # 線寬=0, 實心
                if game_round % 2 == 0:
                    color = (50, 50, 50)
                else:
                    color = (200, 200, 200)
                pg.draw.circle(bg, color, (x_inter*40, y_inter*40), 20, 0)
                # 把某個圖層貼到上一層
                screen.blit(bg, (0, 0))
                # 對畫面進行更新(才會真的秀出來)
                pg.display.update()
                # 每下一子就回合+1
                game_round = game_round + 1

        # 如果收到的事件是按x
        if event.type == pg.QUIT:
            # 迴圈就會變成while False
            running = False
# 結束遊戲
pg.quit()