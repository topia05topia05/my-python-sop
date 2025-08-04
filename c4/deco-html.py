#デコレータを定義
def wrap_html(tag):
    def wrapper(func):
        def inner(*args, **kwargs):
            s = "<html>"
            s += func(*args, **kwargs)
            s += "</html>"
            return s
        return inner
    return wrapper

def wrap_body(func):
    def wrapper(*args, **kwargs):
        s = "<body>"
        s += func(*args, **kwargs)
        s += "</body>"
        return s
    return wrapper

#デコレータを使ってみる
@wrap_html("html")
@wrap_body
def show_html(text):
    return text

print(show_html("デコレータのテスト"))