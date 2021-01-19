#おまじない
from tkinter import Tk, Button, X, Frame, GROOVE, W, E, Label, Entry, END

#ボタンを押したときに作動
def push():
    print(box1.get())

#おまじない　↓ここから本文
if __name__ == '__main__':
    # tkinter定義
    root = Tk()
    
    # ボタン1
    frame_1 = Frame(root, bd=4, relief=GROOVE) #ボタン1の定義
    frame_1.grid(row=0, column=0) #ボタン1の位置
    btn1 = Button(frame_1, text='1', command=push, font=("",20)) #ボタン1が押されたときの処理
    btn1.pack(fill=X) #ボタン1設置
    
    # ボタン2
    frame_2 = Frame(root, bd=4, relief=GROOVE) #ボタン2の定義
    frame_2.grid(row=1, column=1) #ボタン2の位置
    btn2 = Button(frame_2, text='2', command=push, font=("",20)) #ボタン2が押されたときの処理
    btn2.pack(fill=X) #ボタン2設置

    # ボタン2
    frame_3 = Frame(root, bd=4, relief=GROOVE) #ボタン2の定義
    frame_3.grid(row=2, column=2) #ボタン2の位置
    btn3 = Button(frame_3, text='3', command=push, font=("",20)) #ボタン2が押されたときの処理
    btn3.pack(fill=X) #ボタン2設置

    # 入力フォーム
    box1 = Entry(width=3) #入力フォームの定義
    box1.place(x=90, y=10) #入力フォームの位置
    
    # tkinter作動
    root.mainloop()