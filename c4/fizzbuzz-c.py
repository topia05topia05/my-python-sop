res = [
    "FizzBuzz" if i % 15 == 0 else "Fizz"
               if i % 3 == 0 else "buzz"
               if i % 5 == 0 else str(i)
    for i in range(1, 21)]

print(res)

#FizzBuzz

for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

from dataclasses import dataclass

@dataclass
class Rule:
    divisor: int
    word: str

rules = [
    Rule(divisor=3, word="Fizz"),
    Rule(divisor=5, word="Buzz"),
]

def advanced_fizzbuzz(number: int, rule_set: list[Rule]) -> str:
    # 現在の数値に適用された単語を格納する
    output = ""
    for rule in rule_set:
        if number % rule.divisor == 0:
            output += rule.word
    
    # もしどのルールにも一致しなければ、数値をそのまま返す
    return output or str(number)

# 実行
for i in range(1, 101):
    print(advanced_fizzbuzz(i, rules))