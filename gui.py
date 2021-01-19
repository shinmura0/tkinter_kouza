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
    btn1 = Button(frame_1, text='出力', command=push, font=("",20)) #ボタン1が押されたときの処理
    btn1.pack(fill=X) #ボタン1設置
    
    # tkinter作動
    root.mainloop()