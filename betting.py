'''
袋の中に-1、0、1と書かれた3種類のボールが一定の割合で複数個入っているとする。
袋から1つのボールを取り出した時、1が出ることにベットする、という状況を想定している。
書かれた数字はそのまま倍率になっている。-1を引くとベット分没収されるし、1を引くとベット分得られる。0は変動なし。
0を入れる意味はあまり無い気もするけどとりあえず入れた。
'''


import random

global ballList
ballList = []

def main():

    #勝ち、負け、引き分けの数をそれぞれ指定する
    wper = 44
    lper = 48
    dper = 8

    #初期で持っている金額
    nowMoney = 10000
    #基礎となるベット数を指定
    basebet =100

    makelist(wper,lper,dper) #最初はリスト生成
    resetnum = len(ballList) / 2 #リスト再生成の目安。今回はボールの数が半分の時。
    for i in range(100): #今回は100回のゲーム
        print("battle : "+str(i))
        bet = betting(basebet)
        print("bet : "+str(bet))
        print("win : lose = " + str(ballList.count(1)) + ":" + str(ballList.count(-1)))
        nowMoney +=result(battle())*bet #勝った時1倍、負けた時-1倍、引き分けで0倍のベット。

        if len(ballList) == resetnum: #リストの長さが規定回数以下になった時にリストを生成しなおす
            makelist(wper,lper,dper)

        print("now money : "+str(nowMoney))
        print("")


#勝敗を-1、0、1で出力し、リストからその要素を消去する関数
def battle():
    num = random.choice(ballList)
    """
    これはボールを減少させる用。今は未使用
    ballList.remove(num)
    """
    return num

#勝敗をprintで表示するだけ。いずれ何かに使うかもと思いとりあえず作った。
def result(battle):
    print(battle)
    if battle == -1:
        print("負け")
    elif battle == 1:
        print("勝ち")
    else:
        print("引き分け")
    return battle

#ベットする金額を決める関数。
def betting(basebet):
    #basebet=100 #基礎ベットを決める

    #割合に応じてどのくらい賭けるか決める。今は（当たりの数-外れの数）/ボール全体*基礎ベット
    '''
    恐らく考えるべきはこのcountをどのくらい上下させるかである。
    今は仮に「（当たりの数-外れの数）/ボール全体*基礎ベット」を入れているが適当である。
    '''
    count = int((ballList.count(1) - ballList.count(-1)) / len(ballList) * basebet)
    return basebet + count

#ボールリストを作成する関数
def makelist(w,l,d):
    ballList.clear() #初期化
    for i in range(w):
        ballList.extend([1])
    for i in range(l):
        ballList.extend([-1])
    for i in range(d):
        ballList.extend([0])
    #ballList.sort()

if __name__ == "__main__":
    main()
