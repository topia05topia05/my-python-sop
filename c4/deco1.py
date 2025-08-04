#デコレーターの関数を定義
def show_func_name(func):
    def wrapper(*args, **kwargs):
        print("--- start:" + func.__name__ )
        res = func(*args, **kwargs)
        print("--- end:" + func.__name__ )
        return res
    return wrapper

#デコレーターを使う
@show_func_name
def kakugen():
    print("能ある鷹は爪を隠す")
    print("鷹の爪は人間を獲る")

@show_func_name
def kakugen2():
    print("2能ある鷹は爪を隠す")
    print("2鷹の爪は人間を獲る")

#実行
kakugen()
kakugen2()