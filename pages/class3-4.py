import random

a = random.randrange(1, 101)


while True:
    b = int(input("請輸入1~100的數字: "))
    if b == a:
        print("恭喜你，猜對了！")
        break
    elif b < a:
        print("再大一點！")
    else:
        print("再小一點！")
