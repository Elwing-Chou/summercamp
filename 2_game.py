import random

my = int(input("0=剪刀 1=石頭 2=布:"))
com = random.randint(0, 2)
print("我出的", my)
print("電腦的", com)

# if-elif-else
# 你選的是電腦的下一個
if my == (com + 1) % 3:
    print("WIN")
# 電腦的是你的下一個
elif com == (my + 1) % 3:
    print("LOSE")
else:
    print("EVEN")