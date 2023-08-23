import tkinter as tk
import pandas as pd
import os

from gui import * 

def main():

    root = tk.Tk()
    root.title('Registro Compras Cacao v1.0.0')
    root.geometry('750x350')

    marcos = Marco(root,bg='#289c8e',width=750,height=350)
    marcos.marcos_superiores()
    marcos.barra_menu()

    marcos.place(x=0,y=0)

    root.mainloop()

if __name__ == '__main__' :
    main()