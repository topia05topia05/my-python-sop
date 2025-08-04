# じゃんけんゲーム
import random

#手をリストで表現
hand = ["グー", "チョキ", "パー", "ゲーム終了"]

print("===じゃんけんを始めます。===")
while True:
    #コンピュータの手を決定
    com_hand = random.randint(0, 2)
    #ユーザーの手を入力
    for i, desc in enumerate(hand):
        print(i, ":", desc)
    you = int(input("出す手を数値で入力"))
    if you == 3: break
    if you < 0 or you > 2:
        print("0〜3の数字を入力してください")
        continue
    #手を表示
    print("---")
    print("自分の手:", hand[you])
    print("コンピュータの手:", hand[com_hand])
    input("---")
    #じゃんけんの勝敗を判定する
    j = (you - com_+ 3) % 3
    if j == 0:
        print("あいこ")
    elif j == 1:
        print("勝ち")
    else:
        print("負け")
        input("---")
