#あるクラスの国語の点数をリストに代入
points = [80, 75, 90, 85, 70]

#点数を合計する
sum_v = 0
for i in points:
    sum_v += i

print("合計点数: ", sum_v)

#点数を平均する
avg_v = sum_v / len(points)
print("平均点数: ", avg_v)

#点数を最大値と最小値を求める
max_v = max(points)
min_v = min(points)
print("最大点数: ", max_v)
print("最小点数: ", min_v)

#点数を昇順と降順に並び替える
points.sort()
print("昇順: ", points)
points.sort(reverse=True)
print("降順: ", points)

#点数をランダムに並び替える
import random
random.shuffle(points)
print("ランダム: ", points)
