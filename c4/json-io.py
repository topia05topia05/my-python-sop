import json

#辞書型のデータを定義する
data = {'name': 'Alice', 'age': 25, 'city': 'Tokyo'}

#JSONファイルに書き込む
filename = 'test.json'
with open(filename, 'w') as fp:
    json.dump(data, fp)

#JSONファイルから読み込む
with open(filename, 'r') as fp:
    j = json.load(fp)

print(j)    