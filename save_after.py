#おまじない
from tkinter import Tk, Button, X, Frame, GROOVE, W, E, Label, Entry, END
import numpy as np
import os

#　保存フォルダの作成
def make_folder():
    # フォルダの名前
    path = "files/"
    # 上記のフォルダを作る
    os.mkdir(path)

#　入力フォームの保存
def save():
    # フォルダの名前（上記と同じ）
    path = "files/"
    # 入力フォームを読み込む
    a = box1.get()
    b = box2.get()
    # aとbを表にする
    result = []
    result.append(int(a))
    result.append(int(b))
    # aの保存
    np.savetxt(path + "file.csv", result, delimiter=",")

# 保存ファイルの読み込み
def load():
    path = "files/"
    # 保存ファイルを読み込む
    result = np.loadtxt(path + "file.csv", delimiter=",")
    # aを表示
    print("a:",result[0])
    print("b:",result[1])

#おまじない　↓ここから本文
if __name__ == '__main__':
    # tkinter定義
    root = Tk()
    
    # ボタン1
    frame_1 = Frame(root, bd=4, relief=GROOVE) #ボタン1の定義
    frame_1.grid(row=0, column=0) #ボタン1の位置
    btn1 = Button(frame_1, text='フォルダ作成', command=make_folder, font=("",20)) #ボタン1が押されたときの処理
    btn1.pack(fill=X) #ボタン1設置
    
    # ボタン2
    frame_2 = Frame(root, bd=4, relief=GROOVE) #ボタン2の定義
    frame_2.grid(row=1, column=1) #ボタン2の位置
    btn2 = Button(frame_2, text='保存', command=save, font=("",20)) #ボタン2が押されたときの処理
    btn2.pack(fill=X) #ボタン2設置

    # ボタン3
    frame_3 = Frame(root, bd=4, relief=GROOVE) #ボタン3の定義
    frame_3.grid(row=2, column=2) #ボタン3の位置
    btn3 = Button(frame_3, text='読み込み', command=load, font=("",20)) #ボタン3が押されたときの処理
    btn3.pack(fill=X) #ボタン3設置

    # 入力フォーム
    box1 = Entry(width=3) #入力フォームの定義
    box1.place(x=200, y=10) #入力フォームの位置
    
    box2 = Entry(width=3) #入力フォームの定義
    box2.place(x=250, y=10) #入力フォームの位置

    # tkinter作動
    root.mainloop()