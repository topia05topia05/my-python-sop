#辞書型のデータ（果実名と価格）を変数に代入
fruits = {"apple": 100, "banana": 200, "orange": 300}

#辞書型のデータ一覧を表示
for mame, price in fruits.items():
    #画面に出力
    s = "{0}は {1}円です。".format(mame, price)
    print(s)