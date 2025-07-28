#国語の点数一覧
points = [80, 75, 90, 85, 70, 23, 12,]

#30点未満のデータだけ選んで赤点リストに追加
akaten = [p for p in points if p < 30]

print(akaten)