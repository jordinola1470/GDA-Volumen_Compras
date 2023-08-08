import tkinter as tk
from formularios import crear_datos_productor,datos_genero,datos_gda,datos_volumen

class Marco(tk.Frame):
    def __init__(self, root=None, bg=None,width=None,height=None):
        super().__init__(root,bg=bg,width=width,height=height)

        self.pack()

    def marcos_superiores(self):

        self.marco_izquierdo = tk.Frame(self,bg='white',width=850,height=300)
        self.marco_izquierdo.place(x=0,y=0)
               
        #DATOS BASE PRODUCTOR
        self.entry_vars_datos = crear_datos_productor(self)
        
        #DATOS GENERO PRODUCTOR
        self.entry_vars_genero = datos_genero(self)

        #DATOS GDA CACAO CONECTA
        self.entry_vars_gda = datos_gda(self)

        #DATOS TABLA REGISTRO
        self.entry_vars_volumen = datos_volumen(self)


        #MANIPULACION DE ENTRADAS Y DATOS


    # def marcos_inferiores(self):    