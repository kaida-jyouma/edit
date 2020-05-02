# フロアフィールド頑張ってみる。
import math as mt
import matplotlib.pyplot as plt
import time as tm

def print2djoin(listname): # テキスト表示
    da = [""]
    for d1 in listname:
        for d2 in d1:
            da.append(d2)
        da.append("\n")
    print(" ".join(list(map(str, da))))
    return

def md(x, y): # ドアまでの距離を求める
    tx1 = abs(1 - x) # 上ドアまでの距離(x)
    tx2 = abs(6 - x) # 下ドアまでの距離(x)
    ty = abs(11 - y) # ドアまでの距離(y)
    return(float(str(min([mt.sqrt(tx1**2 + ty**2), mt.sqrt(tx2**2 + ty**2)]))[:7]))





# 距離リスト作成
dis = [[0 for c in range(12)] for d in range(7)]
for i in range(7):
    for j in range(12):
        dis[i][j] = md(i, j)

# 教室作成
cll = [
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0]
]

# ランダム方向抽選用
chz = [[[] for c in range(12)] for d in range(7)]

ckr = False

while True:
    if not ckr:
        break
    # else:
        

# print(type(dis[-2][-3]))
