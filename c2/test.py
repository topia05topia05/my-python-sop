# pandas DataFrameを作成し、'sales'列が100より大きい行を抽出する関数
def sales_over_100(df):
    return df[df['sales'] > 100]