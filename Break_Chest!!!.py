#Eklentiler
import tkinter as tk
import random as rd
from PIL import Image, ImageTk
root = tk.Tk()
root.title('Break Chest !!!')
root.state('zoomed')

#Fotolar
krakenorm = Image.open('C:/Users/lenovo/Desktop/Game_Break_Chest/Cute_Megaladon_Normal.png')
krakenorm = ImageTk.PhotoImage(krakenorm)

megaladonhuge = Image.open('C:/Users/lenovo/Desktop/Game_Break_Chest/Cute_Megaladon_Huge.png')
megaladonhuge = ImageTk.PhotoImage(megaladonhuge)

megaladontit = Image.open('C:/Users/lenovo/Desktop/Game_Break_Chest/Cute_Megaladon_Titanic.png')
megaladontit = ImageTk.PhotoImage(megaladontit)

megaladonmeg = Image.open('C:/Users/lenovo/Desktop/Game_Break_Chest/Cute_Megaladon_Titanic.png')
megaladonmeg = ImageTk.PhotoImage(megaladonmeg)

#Fonksiyonlar
def cıkar():
    label.pack_forget()
    label1.pack_forget()
    label2.pack_forget()
    label3.pack_forget()
    a = rd.randint(1,1000)
    if a < 900:
        label.pack()
    if a < 950 and a > 900:
        label1.pack()
    if a < 975 and a > 950:
        label2.pack()
    if a < 1000 and a > 990:
        label3.pack()

#butonlar
button = tk.Button(root,text='Beta için deneme',command=cıkar)
button.pack()

#resimler
label = tk.Label(root,image= krakenorm)
label1 = tk.Label(root, image=megaladonhuge)
label2 = tk.Label(root,image=megaladontit)
label3 = tk.Label(root,image=megaladonmeg)

#çalıştırma
root.mainloop()