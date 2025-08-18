# bmi公式: weight(kg)/height(m)^2
# 絕對不要重複寫!!!!
# =: 名稱 = 值
# a. 5 == 3 + 2(相等?)
# b. x = 2(替換)
# 型態: 3(int)整數 3.1(float)小數 "ggkihj"(str) 字串
# 型態轉換: int() float() str()
# 名稱 = input("參數") 回傳答案(字串)
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (height / 100) ** 2
print("你的體重" + str(weight))
print("你的身高" + str(height))
print("bmi是" + str(bmi))

# 如果 否則(if else)
# 縮排: 強制排版(冒號/TAB)
# Elwing:
#   xxx
if bmi > 25:
    print("過重")
else:
    print("正常")






