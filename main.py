import tkinter as tk
from gui import *

def main():

    root = tk.Tk()
    root.title('Registro Compras Cacao v1.0.0')
    root.geometry('840x350')

    marcos = Marco(root,bg='#E9573F',width=840,height=350)
    marcos.marcos_superiores()

    marcos.place(x=0,y=0)

    root.mainloop()

if __name__ == '__main__' :
    main()