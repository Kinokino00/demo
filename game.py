"""
- 猜數字遊戲
1. 要任意產生亂數(1-50)
2. 要讓使用者可以猜數字
3. 偵測是否猜對
4. 可以多次猜測

"""

import random

low, high = 1, 50
x = random.randint(low, high)
print(x)

for i in range(5):
    y = eval(input(f"請輸入一個數字{low}~{high}: "))
    if y == x:
        print("恭喜猜對")
        break
    else:
        if y > x:
            print("猜低一點~")
        else:
            print("猜高一點~")
        print("猜錯了!")
if y != x:
    print(f"答案為:{x}")
