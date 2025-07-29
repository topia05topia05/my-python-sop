# src/grade_utils.py

def analyze_grades(records: dict):
    """
    生徒の成績データ（辞書）を受け取り、
    合計点、平均点、そして、各個人の、平均との差を、計算し、
    整形された、結果を、コンソールに、表示する。
    """
    # データが空の場合のエラー処理
    if not records:
        print("エラー：データが、空です。")
        return

    # --- ここからが、授業で習ったコードの、本質部分 ---
    # 1. 合計と平均を計算する
    total_score = sum(records.values())
    average_score = total_score / len(records)

    # 2. 計算結果と、詳細な一覧を表示する
    print(f"--- 成績分析結果 ---")
    print(f"合計点: {total_score}")
    print(f"平均点: {average_score:.1f}")
    print("-" * 35)
    print(f"| {'名前':<7} | {'点数':>4} | {'平均との差':>8} |")
    print("-" * 35)

    for name, score in sorted(records.items()):
        difference = score - average_score
        print(f"| {name:<7} | {score:>4} | {difference:>+8.1f} |")

    print("-" * 35)
