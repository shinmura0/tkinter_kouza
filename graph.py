#おまじない
from tkinter import Tk, Button, X, Frame, GROOVE, W, E, Label, Entry, END
import numpy as np
import os
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
             
# プロットする関数
def graph(data):
    # 大きさ(6,3)のグラフを生成する
    fig = plt.Figure(figsize=(6,3))
    ax1 = fig.add_subplot(111)
    
    # もらったデータをプロットする。
    ax1.plot(data)

    # グラフの描画
    canvas = FigureCanvasTkAgg(fig, frame_3)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0)

    return fig    

#　入力フォームの保存
def plot():
    # 入力フォームを読み込む
    a = box1.get()
    b = box2.get()
    c = box3.get()
    # 表形式に変換
    result = []
    result.append(int(a))
    result.append(int(b))
    result.append(int(c))
    # 描画関数にデータを渡す
    graph(result)

#おまじない　↓ここから本文
if __name__ == '__main__':
    # tkinter定義
    root = Tk()
    
    # ボタン1
    frame_1 = Frame(root, bd=4, relief=GROOVE) #ボタン1の定義
    frame_1.grid(row=0, column=0) #ボタン1の位置
    btn1 = Button(frame_1, text='描画', command=plot, font=("",20)) #ボタン1が押されたときの処理
    btn1.pack(fill=X) #ボタン1設置
    
    # グラフ
    frame_3 = Frame(root, bd=4, relief=GROOVE) #ボタン1の定義
    frame_3.grid(row=1, column=0)
    canvas = FigureCanvasTkAgg(graph([]), frame_3)

    # 入力フォーム
    box1 = Entry(width=3) #入力フォームの定義
    box1.place(x=20, y=5) #入力フォームの位置
    
    box2 = Entry(width=3) #入力フォームの定義
    box2.place(x=50, y=5) #入力フォームの位置

    box3 = Entry(width=3) #入力フォームの定義
    box3.place(x=80, y=5) #入力フォームの位置

    # tkinter作動
    root.mainloop()