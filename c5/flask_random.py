import random
from flask import Flask

quotes = [
    "能ある鷹は爪を隠す", 
    "豚に真珠", 
    "二兎追う者は二兎を失う",
    "一石二鳥",
    "猫に小判",
    "七転八起",
    "十人十色",
    "百聞は一見に如かず"
]

app = Flask(__name__)

@app.route("/")
def index():
    num = random.randint(0, 7)
    mgs = quotes[num]
    html = f"""<html><meta charset="utf-8"><body>
    <div style="text-align: center; border: 1px solid ; padding: 2em">
    <h1><img src="https://emojipedia.org/wp-content/uploads/2017/04/dice-1.png" width="20" height="20"></h1><p>{mgs}</p></div>
    <a href="/">→ 更新する</a></body></html>"""
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)