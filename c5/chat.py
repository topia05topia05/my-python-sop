import os, time, json
from flask import Flask, request, redirect
from markupsafe import Markup

#チャットログの保存ファイル
SAVE_FILE = os.path.join(os.path.dirname(__file__), 'chat.log.json')

#Flaskのインスタンスを作る
app = Flask(__name__)

#チャットログファイルを作成する
if not os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)

#ルートにアクセスしたとき
@app.route('/')
def index():

    #チャットログを読んでHTMLを生成
    logs = ""
    for c in reversed(read_chat_log()):
        name , body = Markup(c['name']), Markup(c['body'])
        logs += f"<div class='box'><span class='name'>{name}</span>: "
        logs += f"{body} >(span class='date'>{c['date']}</span></div>"
    #CSSの定義
    css = """
        h1 { background-color: #eef; color: black; padding: 1em; }
        .blue {background-color: #eef;}
        .box {border-bottom: 1px solid gray; padding: 1em; }
        .name { font-weight: bold; color: blue; background-color: #ff3; }
        .date { font-size: 0.8em; color: gray; }"""
    #フォームの定義
    form = """
        <form method="post" action="/write">
            名前: <input type="text" name="name" value"" maxlength="8">
            内容: <input type="text" name="body" value"" maxlength="30">
            <input type="submit" value="発言">
            """ 
    #HTMLにチャットログを埋め込んで表示
    return f"""
        <html><meta charset="utf-8"><style>{css}</style><body>
            <h1>チャット</h1>
            <div class="box-blue">{form}</div>
            <div>{logs}</div>
        </body></html>
    """
# /writeにアクセスした時の処理
@app.route("/write", methods=["POST"])
def write():

    name = request.form.get('name')
    body = request.form.get('body')
     
    if name is None or name == "" or body == "":
        return redirect("/")
    
    try:
        chats = read_chat_log()
        chats.append({'name': name, 'body': body, 'date': time.strftime('%Y-%m-%d %H:%M:%S')})
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(chats, f)
    except Exception as e:
        print("チャットの書き込みに失敗しました", e)
    return redirect("/")

def read_chat_log():
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("チャットの読み込みに失敗しました", e)
        return []
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)