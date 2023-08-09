import tkinter as tk
from formularios import crear_datos_productor,datos_genero,datos_gda,datos_volumen

class Marco(tk.Frame):
    def __init__(self, root=None, bg=None,width=None,height=None):
        super().__init__(root,bg=bg,width=width,height=height)

        self.root = root
        self.pack()

    def marcos_superiores(self):
        self.marco_izquierdo = tk.Frame(self,bg='white',width=850,height=300)
        self.marco_izquierdo.place(x=0,y=0)
               

        #DATOS BASE PRODUCTOR
        self.entry_vars_datos = crear_datos_productor(self.marco_izquierdo)
        #DATOS GENERO PRODUCTOR
        self.entry_vars_genero = datos_genero(self.marco_izquierdo)
        #DATOS GDA CACAO CONECTA
        self.entry_vars_gda = datos_gda(self.marco_izquierdo)
        #DATOS TABLA REGISTRO
        self.entry_vars_volumen = datos_volumen(self.marco_izquierdo)
        
        #MANIPULACION DE ENTRADAS Y DATOS

        def registro_compra():
            datos_registrados = [self.entry_vars_datos,self.entry_vars_genero,self.entry_vars_gda]   
            valores_registrados = []
            for datos in datos_registrados:
                for etiqueta, entry_var in datos:    
                    print(f"{etiqueta}: {entry_var.get()}")
                    valores_registrados.append((etiqueta,entry_var.get()))

            return print(valores_registrados)

        
        ##BOTON REGISTRAR

        # self.boton_registrar = tk.Button(self.marco_izquierdo,text='Registrar',height=4,command=registro_compra)
        # self.boton_registrar.place(x=638,y=215)

        self.boton_registrar = tk.Button(self.marco_izquierdo,text='Registrar',height=6,relief='sunken',command=registro_compra)
        self.boton_registrar.place(x=730,y=182)


    def barra_menu(self):

        self.barra_menu = tk.Menu(self.root)
        self.root.config(menu=self.barra_menu)

        self.file_menu = tk.Menu(self.barra_menu)
        self.barra_menu.add_cascade(label='Registro',menu=self.file_menu)

        self.file_menu.add_command(label='Nuevo Registro')
        self.file_menu.add_command(label='Eliminar Registros')
        self.file_menu.add_command(label='Salir',command=self.root.quit)

        


    # def marcos_inferiores(self):    