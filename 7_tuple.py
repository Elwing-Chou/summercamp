# tuple: 簡化版的字典
# RGB: RED(0-255) GREEN BLUE
color = {
    "r":80,
    "g":200,
    "b":30
}
# 如果每次都要這樣表示顏色 也太累了
# tuple
color = (80, 200, 30)
print(color[0])
r, g, b = color
print(r, g, b)