#おまじない
from tkinter import Tk, Button, X, Frame, GROOVE, W, E, Label, Entry, END
import RPi.GPIO as GPIO
import os
import time
             
# LED点灯
def begin():
    GPIO.output(pin, 1)
    time.sleep(3)
    GPIO.output(pin, 0)

# LED消灯
def end():
    GPIO.output(pin, 0)

def close():
    # GPIO終了
    GPIO.cleanup(pin)
    # tkinter終了
    root.destroy()

#おまじない　↓ここから本文
if __name__ == '__main__':
    # GPIO番号指定の準備
    GPIO.setmode(GPIO.BCM)

    # LEDとスイッチのGPIO番号
    pin = 3

    # LEDピンを出力に設定
    GPIO.setup(pin, GPIO.OUT)

    # tkinter定義
    root = Tk()
    
    # ボタン1
    frame_1 = Frame(root, bd=4, relief=GROOVE) #ボタン1の定義
    frame_1.grid(row=0, column=0) #ボタン1の位置
    btn1 = Button(frame_1, text='点灯', command=begin, font=("",20)) #ボタン1が押されたときの処理
    btn1.pack(fill=X) #ボタン1設置
    
    # ボタン2
    frame_2 = Frame(root, bd=4, relief=GROOVE) #ボタン1の定義
    frame_2.grid(row=1, column=0) #ボタン1の位置
    btn2 = Button(frame_2, text='消灯', command=end, font=("",20)) #ボタン1が押されたときの処理
    btn2.pack(fill=X) #ボタン1設置

    # ボタン3
    frame_3 = Frame(root, bd=4, relief=GROOVE) #ボタン1の定義
    frame_3.grid(row=2, column=0) #ボタン1の位置
    btn3 = Button(frame_3, text='終了', command=close, font=("",20)) #ボタン1が押されたときの処理
    btn3.pack(fill=X) #ボタン1設置

    # tkinter作動
    root.mainloop()