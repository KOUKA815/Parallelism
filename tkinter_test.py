import tkinter as tk
import Scraping_zozo as zozo
import Scraping_beams as beams
import Scraping_nike as nike
import tkinter.ttk as ttk
import webbrowser
from PIL import ImageTk, Image
from functools import partial
# デザインテーマの設定

# ウィンドウを作成 --- (*1)
root = tk.Tk()
root.geometry("1280x720") # サイズを指定
root.title("Parallelism")
iconfile = 'icon2.ico'
root.iconbitmap(default=iconfile)

def jump_to_link(url, e):
    webbrowser.open_new(url)



tk.Button(root, text="←" ,font=("", 30),bg='navy',fg='sandy brown').grid(row=0, column=0,padx=5, pady=10)
entry = tk.Entry(root,width=30, font=("", 50))
entry.grid(row=0,column=1, sticky="e", padx=5, pady=10)

#検索ボタンをクリックすると、スクレイピングが始まる
def btn_click(value):
    if value == "":
        return

    p1 = nike.excute(value)
    p2 = zozo.excute(value)
    p3 = beams.excute(value)

    if not p1 or not p2 or not p3:
        return

    for i in range(2):
        result = [p1[i],p2[i],p3[i]]
        sorted_p = sorted(result)

    word = ttk.Label(root,anchor="w",text="あなたが求めている"+value+"はこれだ！！",font=(u"MSゴシック", "24", "bold"),background="gray")
    word.grid(row=5,column=1,sticky="w")
    #forでラベルを５つ表示させる
    for i in range(2):
        result = [p1[i],p2[i],p3[i]]
        sorted_p = sorted(result)
        for num in range(3):

            index = 0
            if i == 1:
                index = (i+1)*(num+1)*4+8
            else:
                index = (i+1)*(num+1)*4
            sep1 = ttk.Separator(root, orient="horizontal",style="blue.TSeparator")
            sep1.grid(row=index,columnspan=3,sticky="ew")

            goods1 = ttk.Label(root,width=50,anchor="w",text=sorted_p[num].title,font=(u"MSゴシック", "24", "bold"),background="gray")
            goods1.grid(row=index+1,column=1,sticky="w")
            goods1.bind("<Button-1>",  partial(jump_to_link, sorted_p[num].url))

            gval1 = ttk.Label(root,width=15,anchor="w",text="￥"+sorted_p[num].price,font=(u"MSゴシック", "24", "bold"),background="gray")
            gval1.grid(row=index+2,column=1,sticky="w")

            brand1 = ttk.Label(root,width=15,anchor="e",text=sorted_p[num].brand,font=(u"MSゴシック", "24", "bold"),background="gray")
            brand1.grid(row=index+2,column=1,sticky="e")
            brand_name = sorted_p[num].brand
            if brand_name == "zozo":
                brand1.bind("<Button-1>",  partial(jump_to_link,"https://zozo.jp/"))
            elif brand_name == "nike":
                brand1.bind("<Button-1>",  partial(jump_to_link,"https://www.nike.com/"))
            else:
                brand1.bind("<Button-1>",  partial(jump_to_link,"https://www.beams.co.jp/"))



button = tk.Button(root,width=7, text="検索",font=("", 30),bg='navy',fg='sandy brown',command=lambda:btn_click(entry.get()))
button.grid(row=0, column=2, pady=10)
frame_for_radio = tk.Frame(root)
frame_for_radio.grid(row=1, column=1, padx=10, pady=10)
iv1 = tk.IntVar()
iv1.set(1)
man = tk.Radiobutton(frame_for_radio, text="MAN", value=1, variable=iv1,font=(u'ＭＳ ゴシック', 24, 'bold'),bg='navy',fg='aquamarine')
man.pack(side='left')
woman = tk.Radiobutton(frame_for_radio, text="WOMAN", value=2, variable=iv1, font=(u'ＭＳ ゴシック', 24, 'bold'),bg='navy',fg='brown3')
woman.pack(side='right')


root.configure(bg='gray')
# ウィンドウを動かす
root.mainloop()
