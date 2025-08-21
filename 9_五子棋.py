import pygame as pg
#pygame初始化
pg.init()

#設定視窗
width, height = 600, 600
# 產生視窗
screen = pg.display.set_mode((width, height))
# 設定遊戲標題
pg.display.set_caption("五子棋")

# 建立畫布bg
bg = pg.Surface(screen.get_size())
# 把畫布填滿某個顏色
bg.fill((199, 167, 82))
# 把某個圖層貼到上一層
screen.blit(bg, (0,0))
# 對畫面進行更新(才會真的秀出來)
pg.display.update()

# 建立一個永不結束的迴圈(遊戲才不會結束)
running = True
while running:
    # 收取你的遊戲任何事件(滑鼠點擊/鍵盤按鈕...)
    for event in pg.event.get():
        # 如果收到的事件是按x
        if event.type == pg.QUIT:
            # 迴圈就會變成while False
            running = False
# 結束遊戲
pg.quit()