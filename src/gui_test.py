#赤と青の線を交互に100本引く

#グラフィックスライブラリをインポートする
from tkinter import *
#画面の初期化
w = Canvas(Tk(), width=400, height=400)
w.pack()
#赤線を引く
for i in range(100):
    w.create_line(0, i*2, 400, i*2, fill="red")
#青線を引く
for i in range(100):
    w.create_line(0, i*2+1, 400, i*2+1, fill="blue")

mainloop()