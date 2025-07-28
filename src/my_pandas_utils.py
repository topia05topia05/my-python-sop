# ==============================================================================
#           my_pandas_utils.py - あなたの個人用データ分析ツールボックス
# ==============================================================================
# ここに、あなたが学び、作り上げた、再利用可能な「部品（関数）」を保管していくのよ。

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def load_data_from_csv(file_path: str) -> pd.DataFrame:
    """
    指定されたパスからCSVファイルを読み込み、データフレームとして返す。
    もしファイルが見つからなければ、エラーメッセージを出力する。
    """
    try:
        df = pd.read_csv(file_path)
        print(f"'{file_path}' の読み込みに成功しました。")
        return df
    except FileNotFoundError:
        print(f"エラー: ファイル '{file_path}' が見つかりませんでした。")
        return None # 何も返さない、という意味

def plot_sales_distribution(df: pd.DataFrame, column_name: str, title: str = "Sales Distribution"):
    """
    データフレームの指定された列のデータを棒グラフで表示します。
    """
    if df is not None and not df.empty:
        df[column_name].plot(kind='bar', title=title)
        plt.xlabel('Record Index')
        plt.ylabel('Amount')
        plt.show()
    else:
        print("データフレームが空か、存在しないため、グラフを描画できません。")

def calculate_profit_margin(df: pd.DataFrame, sales_column: str, profit_column: str) -> pd.DataFrame:
    """
    SalesとProfitの列から利益率を計算し、新しい列として追加する。
    売上が0またはnullの場合は、利益率を0として安全に扱う。
    """
    if df is None:
        print("データフレームが存在しないため、処理を中断します。")
        return None

    # 利益を売上で割る。もし売上が0なら、結果は無限大(inf)か、非数(NaN)になる可能性がある。
    profit_margin = df[profit_column] / df[sales_column]
    
    # NumPyの力を使って、発生したかもしれない無限大や非数を、安全な「0」に置き換える。
    # これこそが、エラーを未然に防ぐ、プロの防御的プログラミングよ。
    df['Profit_Margin'] = profit_margin.replace([np.inf, -np.inf], np.nan).fillna(0)
    
    return df