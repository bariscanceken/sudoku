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
path_menupng = os.path.join(base_dir, 'menupng.png')

#Screen
window = tk.Tk()
window.title("SUDOKU")
window.geometry("750x750")

#Main Menu
menu_image = tk.PhotoImage(file=path_menupng)
menuimage_label = tk.Label(window, image=menu_image)
menuimage_label.pack()




window.mainloop()
