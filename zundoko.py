import random

ZUNDOKO = "ズンズンズンズンドコ"
KIYOSHI = "KIYOSHI"

list = []

while ''.join(list[-5:]) != ZUNDOKO:
    list.append(random.choice(["ズン", "ドコ"]))
    print(list[-1])
print(''.join(list[-5:]))
print(KIYOSHI)