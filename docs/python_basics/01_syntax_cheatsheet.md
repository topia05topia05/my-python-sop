---

```markdown
# Python 構文チートシート

---

## 基本出力

### 画面表示
```python title="print()"
print("表示したい内容")
```

### f-string (文字列と変数の合体)
```python title="f-string"
name = "パートナー"
print(f"ようこそ, {name}!")
```

---
## 条件分岐: if-else

!!! note "条件分岐の、本質"
    プログラムの流れを、「もし〇〇なら、Aの道へ。そうでなければ、Bの道へ」と、分岐させるための、命令。

### 基本形
```python
score = 85
if score >= 80:
    print("合格！")
else:
    print("不合格...")
```

### 複数条件 (elif)
```python
score = 75
if score >= 80:
    print("優")
elif score >= 60:
    print("良")
else:
    print("可")
```

### ネスト（入れ子）
```python
attendance_rate = 0.9
if score >= 60:
    print("点数は合格...")
    if attendance_rate >= 0.8:
        print("出席率もクリア！最終的に、合格です。")
    else:
        print("しかし、出席率が足りません。不合格。")
else:
    print("点数が足りません。不合格。")
```

---
## 論理演算子

| 演算子 | 意味 | 使用例 |
|:---:|:---|:---|
| `and` | **かつ** (両方がTrueの時だけ、True) | `if score >= 80 and attendance_rate >= 0.8:` |
| `or` | **または** (どちらか一方がTrueなら、True) | `if day == "Saturday" or day == "Sunday":` |
| `not` | **ではない** (True/Falseを、反転させる) | `if not is_submitted:` |

---
## データ構造

### リスト (list) - 順番のある、データの集まり
```python title="リストの、基本操作"
# 作成
my_list = ["apple", "banana", "cherry"]
print(f"最初のリスト: {my_list}")

# 取り出し (0番目から数える)
first_item = my_list
print(f"最初の要素: {first_item}")

# 末尾に、追加
my_list.append("orange")
print(f"追加後のリスト: {my_list}")

# 書き換え
my_list = "grape"
print(f"書き換え後のリスト: {my_list}")

# 削除
del my_list
print(f"削除後のリスト: {my_list}")

# 長さの取得
list_length = len(my_list)
print(f"現在の、長さ: {list_length}")
```

### 辞書 (dict) - 名前付きの、データの集まり
```python title="辞書の、基本操作"
# 作成
my_dict = {"name": "月雲アリア", "age": 23}
print(f"最初の辞書: {my_dict}")

# 取り出し (キーを指定)
name = my_dict["name"]
print(f"名前: {name}")

# 追加 / 書き換え
my_dict["speciality"] = "Quantum Machine Learning"
print(f"追加後の辞書: {my_dict}")
```

---
## 繰り返し処理: for ループ
```python title="リストの、全件処理"
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    # `fruit`という、一時的な変数に、リストの要素が、一つずつ、入ってくる
    print(f"I love {fruit}!")```

---
## ファイル I/O (入出力)

!!! warning "ファイルの、書き込み(`"w"`)は、上書きよ！"
    もし、すでに、同名のファイルが存在した場合、その中身は、**完全に、消えてしまう**。注意しなさい。

### 書き込み (Write)
```python title="data.txtへの、書き込み"
my_data = "これが、私の、最初の、ファイル記録よ。"

# "w" は write モードの指定
with open("data.txt", "w", encoding="utf-8") as f:
    f.write(my_data)
```

### 読み込み (Read)
```python title="data.txtからの、読み込み"
# "r" は read モードの指定
with open("data.txt", "r", encoding="utf-8") as f:
    read_data = f.read()

print(f"ファイルから読み込んだ内容: {read_data}")
```
```

---