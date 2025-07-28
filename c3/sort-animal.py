#（動物、最高時速）のリスト（各要素はタプルで作成）
animal_list = [("猫", 30), ("犬", 20), ("鳥", 50), ("魚", 10)]

#最高時速を降順にソート
faster_list = sorted(animal_list, key=lambda ani : ani[0], reverse=True)

#結果を出力
for i in faster_list:
    print(i)