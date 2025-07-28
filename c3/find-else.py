#for構文をフラグで分岐する場合
#食材の一覧
foodstuf = ["mango", "apple", "banana", "orange", "lemon", "grape"]

#マンゴーがないか確認する
for food in foodstuf:
    if food == "mango":
        print("マンゴーはあります")
        break
else:
    print("マンゴーはありません")

if "mango" in foodstuf:
    print("マンゴーはあります")
else:
    print("マンゴーはありません")