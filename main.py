'''
numpy matrisi oluşturacak
tkinter görseli hazırlayacak
sayılar düzgün mantıkla yerleştirilecek
kordinata tıklanıp sayı girilecek
oyun sonlandırmak istenecek
doğruluk yanlışlık geçen zaman
'''

#Libraries
import numpy as np
import tkinter as tk
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
path_menupng = os.path.join(base_dir, 'realmenu.png')

#Screen
window = tk.Tk()
window.title("SUDOKU")
window.geometry("750x750")

#Main Menu
menu_image = tk.PhotoImage(file=path_menupng)
menuimage_label = tk.Label(window, image=menu_image)
menuimage_label.pack()

def ninevnine():
    print('a')

def start ():
    text_which = tk.Label(text="CHOOSE: ")
    text_which.place(x=300,y=350)
    button_nine = tk.Button(text="9X9",command="ninevnine")
    button_six = tk.Button(text="6X6",command="sixvsix")
    button_nine.place(x=300,y=375,width=100,height=50)
    button_six.place(x=300,y=425,width=100,height=50)



#Buttons
button_start = tk.Button(text="Start",command= start)
button_start.pack()
button_start.place(x=420,y=265,width=50,height=50)

window.mainloop()
