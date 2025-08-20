import random

low, high = 1, 100
ans = random.randint(low, high)

count = 0
while True:
    try:
        print("請輸入", low, "-", high)
        n = int(input(":"))
        if low <= n <= high:
            count = count + 1
            if n > ans:
                print("too big")
                high = n
            elif n < ans:
                print("too small")
                low = n
            else:
                print("Congratulations, you win!", count, "次")
                break
    except ValueError:
        print("別亂輸入了")