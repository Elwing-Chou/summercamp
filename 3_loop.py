# 單純執行十次的重複
i = 0
while i < 10:
    print(i, "hello")
    i = i + 1

# for...in走過
for j in range(10):
    print(j, "bye")

f = open("a.txt", "a")
# 以前思維: write(f, "abcd")
# 因為這個write只有檔案才能做(專屬功能): f.write("abcd")
f.write("acbad\n")
# close(f)
f.close()

total = 0
for i in range(100):
    user = input("請輸入分數 輸入exit結束")
    if user == "exit":
        break
    else:
        score = float(user)
        total = total + score
        f = open("score.txt", "a")
        avg = total / (i + 1)
        line = str(score) + "," + str(avg) + "\n"
        f.write(line)
        f.close()


