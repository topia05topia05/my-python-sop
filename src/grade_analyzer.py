"""
成績データを分析するための、便利な関数を集めたモジュール。
"""

def analyze_and_print_grades(records_dict):
    """
    成績データ（辞書型）を受け取り、分析結果をコンソールに出力する。

    Args:
        records_dict (dict): 生徒の名前をキー、点数を値とする辞書。
    """
    # このpassは「何もしない」という仮の命令。後で中身を埋めるわよ。
     # --- ここからが、JupyterLabで実験し、完成させたロジックよ ---
    
    # まず、データが空っぽじゃないか確認するのは、プロの作法よ
    if not records_dict:
        print("データが空です。処理を中断します。")
        return # データがなければ、ここで処理を終了する

    # 合計を計算
    sum_v = sum(records_dict.values())
    
    # 平均を計算
    avg_v = sum_v / len(records_dict)

    # 結果を美しく表示する
    print("-" * 30)
    print(f"| {'名前':<7} | {'点数':>4} | {'平均との差':>8} |")
    print("-" * 30)

    for name, v in sorted(records_dict.items()):
        diff = v - avg_v
        print(f"| {name:<7} | {v:>4} | {diff:>+8.2f} |")

    print("-" * 30)