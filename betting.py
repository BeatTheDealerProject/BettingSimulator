"""
ベッティングシステムを調査するための簡易シミュレータ
任意の勝率、敗北率、引き分け率を設定しゲームを繰り返すことでベッティングシステムの優劣について検証する。
"""


import random
import numpy as np
import matplotlib.pyplot as plt


def main():
    # 勝ち、負け、引き分けの数をそれぞれ指定する
    winper = 44
    loseper = 48
    drawper = 8

    totalwin = 0
    totallose = 0
    totaldraw = 0

    # 初期で持っている金額
    money = 10000
    # 基礎となるベット数(1ユニットの額)を指定
    basebet =100

    # ゲームを行う回数を指定
    game_num = 5000

    # グラフへの出力
    left = np.zeros(game_num)
    height = np.zeros(game_num)

    for i in range(game_num):
        left[i] = i
        height[i] = money
        betmoney = betting(basebet)
        money -= betmoney
        game_result = random_response(winper, loseper, drawper)

        if game_result==1:
            totalwin += 1
        elif game_result==-1:
            totallose += 1
        else:
            totaldraw += 1

        money += money_manager(game_result, betmoney)
        if money <= 0:
            break

    print("win : " + str(totalwin) + "\nlose : " + str(totallose) + "\ndraw : "
          + str(totaldraw) + "\nmoney : " + str(money))
    plt.plot(left, height)
    plt.show()


# ベットする金額を決める関数

def betting(basebet):
    return basebet


# ランダムな結果を返す出漁
# 引数：winper = その時の勝率, loseper = その時の敗北率, drawper = その時の引き分け率
# 返り値: 1 = 勝ち, -1 = 負け, 0 = 引き分け

def random_response(winper, loseper, drawper):
    # すべての確率の合計
    prob_sum = winper + loseper + drawper
    # ランダムな数字を生成
    random_num = random.random()

    # 勝ちと負けの境界を定義
    win_border = winper / prob_sum
    lose_border = (winper + loseper) / prob_sum

    if random_num < win_border:
        return 1
    elif win_border < random_num < lose_border:
        return -1
    else:
        return 0


# 引数:gameresult = 勝敗, betmoney = 賭け金
# 返り値:勝敗に応じた利得

def money_manager(game_result, betmoney):
    if 1 == game_result:
        return betmoney * 2
    elif -1 == game_result:
        return 0
    else:
        return betmoney

if __name__ == "__main__":
    main()
