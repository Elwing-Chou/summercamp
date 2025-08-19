# 遊戲腳本位於此檔案。

# 宣告該遊戲使用的角色。 color 參數
# 為角色的名稱著色。

define e = Character("艾琳", who_color="#eb4034")
define player = Character("[player_name]")

# 遊戲從這裡開始。

label start:

    # scene bg room
    show alice normal
    e "請問你的名字是?"
    $ player_name = renpy.input("請輸入名字", length=8)
    e "喔 你叫做 [player_name] 嗎?"
    menu:
        "是":
            e "好喔"
        "否":
            jump start

# !!!
default win = 0
default lose = 0
default even = 0
label game:
    $ t = ["剪刀", "石頭", "布"]
    e "來玩個剪刀石頭布吧!"
    menu:
        "剪刀":
            $ my = 0
        "石頭":
            $ my = 1
        "布":
            $ my = 2
    $ com = renpy.random.randint(0, 2)
    e "你出 [t[my]] 我出 [t[com]]"
    if my == (com + 1) % 3:
        e "你贏了"
        $ win = win + 1
    elif com == (my + 1) % 3:
        e "你輸了"
        $ lose = lose + 1
    else:
        e "平手"
        $ even = even + 1

    # !!!!
    if win == 3:
        jump final
    elif lose == 3:
        jump final
    else:
        jump game


label final:
    e "贏:[win] 輸:[lose] 平手:[even]"
    return








