#ほぼ丸コピペ
import os, tkinter
def func():      # Etnerキー押下時の動作
    getvalue = textBox1.get()
    print("in the function =",getvalue)
    textBox1.delete(0,tkinter.END)
    label3["text"] = getvalue
def calc(event):  # ボタン押下時の動作 
    getvalue = textBox1.get()
    print("in the function =",getvalue)
    textBox1.delete(0,tkinter.END)
    label3["text"] = getvalue
# ウインドウ
root = tkinter.Tk()              # Tkクラス生成
root.title(u"ウインドウタイトル")  # 画面タイトル  
root.geometry("350x150")         # 画面サイズ 

# 入出力エリア
label1 = tkinter.Label(text='InputData')  # 入力用ラベル
label1.place(x=5,y=5)                     # ラベルの表示位置 
textBox1 = tkinter.Entry(width=5)         # 入力用テキストボックス 
textBox1.place(x=100, y=5)                # テキストボックス位置指定
label2 = tkinter.Label(text='OutputData') # 出力用ラベル
label2.place(x=100,y=50)                  # ラベル位置
label3 = tkinter.Label(text='')
label3.place(x=100,y=70)
textBox1.focus_set()                      # テキストボックスにフォーカス指定 
btn = tkinter.Button(text='Go', command=func) # ボタン作成
btn.pack()
textBox1.bind('<Return>', calc)           # Enterキーが押されイベント設定

root.mainloop()                           # 画面を表示