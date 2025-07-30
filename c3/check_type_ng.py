#型ヒントを指定してリストを定義（定義のエラー有り）
price_list : List[int]= [
    1000, 
    250,
     "#",#エラーになる
      3000 ]

print(price_list)