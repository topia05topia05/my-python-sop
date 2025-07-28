#印税を計算する関数
def calc_royalty(price,sales,per):
    rate = per / 100
    ro = int(price * sales * rate)
    return ro

#ユーザーから情報を入力してもらう
i = input("価格を入力してください:")
price = int(i)

i = input("発行部数は？:")
sales = int(i)

i = input("印税率を入力してください:")
prr = float(i)

#結果を表示する
v = calc_royalty(price,sales,prr)
print("印税は",v,"円です。")