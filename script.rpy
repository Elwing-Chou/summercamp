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
    return
