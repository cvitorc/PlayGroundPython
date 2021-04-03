from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import filedialog

import numpy as np
import sympy as sp
import pandas as pd
import os
sp.init_printing(use_latex="mathjax")

# trabalhando com Grid

window = Tk()
window.title(" Trabalhando com Gerenciador de Layout Grid ")

#dimensoes da janela

largura = 200
altura = 100

#dimensoes no sistema

largura_screen = window.winfo_screenwidth()
altura_screen = window.winfo_screenheight()

#posicao da janela

posx = largura_screen*0.5 - largura*0.5
posy = altura_screen*0.5 - altura*0.5

#definir a geometry

window.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

lbl1 = Label (window, text = "Login:")


lbl2 = Label (window, text = "Senha:")


ed1 = Entry (window)
ed2 = Entry (window)

bt1 = Button (window, text = "Confirmar")

#definindo gerenciador de layout

lbl1.grid(row=0, column = 0)
lbl2.grid(row=1, column = 0)
ed1.grid(row=0, column = 1)
ed2.grid(row=1, column = 1)
bt1.grid(row=2, column = 1)






window.mainloop() 
