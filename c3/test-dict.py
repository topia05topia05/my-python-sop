# 成績データを辞書型で定義
records = {
    "Taro": 80,
    "Hanako": 95,
    "Jiro": 70,
    "Sachiko": 90,
    "Kazuto": 50}
#合計を求める
sum_v = 0
for v in records.values():
    sum_v += v
print("合計点数: ", sum_v)
#平均点数を求める
avg_v = sum_v / len(records)
print("平均点数: ", avg_v)
#成績データの一覧と平均点数の差を表示
fmt = "|{0:<7}|{1:>4}|{2:<5}|"
print("| 名前 |点数, 差")
for name, v in sorted(records.items()):
    diff = v - avg_v
    print(fmt.format(name, v, diff))