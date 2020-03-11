# 関数を紐づけたボタンを配置
#--------------------------

import tkinter
import random
import math
root = tkinter.Tk()
root.title('demo_Tkinter')
root.geometry("400x400")

# コンソールに"Button is clicked."を出力する関数
def clicked():
  print("Button is clicked.")
  print("サイコロ"+str(random.randint(1, 6)))

# ラベルを使って文字を画面上に出す
Static1 = tkinter.Label(text=u'▼　Entryだぞ！　▼')
Static1.pack()

# ボタンの作成（text=ボタンに表示されるテキスト, command=押下時に呼び出す関数）
button = tkinter.Button(root, text="ボタン", command=clicked)

# ボタンの表示
button.grid()

root.mainloop()