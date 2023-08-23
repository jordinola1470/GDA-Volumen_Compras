import tkinter as tk
import pandas as pd
import os

from formularios_datos import crear_datos_productor,datos_genero,datos_gda
from formularios_volumen import datos_volumen

class Marco(tk.Frame):
    def __init__(self, root=None, bg=None,width=None,height=None):
        super().__init__(root,bg=bg,width=width,height=height)

        self.root = root
        self.pack()
        self.valores_registrados = []

    def marcos_superiores(self):
        self.marco_izquierdo = tk.Frame(self,bg='white',width=850,height=300)
        self.marco_izquierdo.place(x=0,y=0)
               

        #DATOS BASE PRODUCTOR
        self.entry_vars_datos = crear_datos_productor(self.marco_izquierdo)
        #DATOS GENERO PRODUCTOR
        self.entry_vars_genero = datos_genero(self.marco_izquierdo)
        #DATOS GDA CACAO CONECTA
        self.entry_vars_gda = datos_gda(self.marco_izquierdo)
        
        #DATOS VOLUMEN VENTAS
        self.entry_vars_volumen = datos_volumen(self.marco_izquierdo)
        
    #-----------------------------------------------------------------------------------------------------------

        #MANIPULACION DE ENTRADAS Y DATOS
        def registro_compra():
            #VARIABLES
            datos_productor_registrados = [self.entry_vars_datos,self.entry_vars_genero,self.entry_vars_gda]   
            datos_volumen_registrados   = self.entry_vars_volumen
            #DATOS GENERALES
            self.valores_registrados =[]
            for datos in datos_productor_registrados:
                for etiqueta, entry_general in datos:
                    self.valores_registrados.append((etiqueta,entry_general.get()))

            #PRECIOS/CANTIDAD
            self.volumen_precios = []
            for key, value in datos_volumen_registrados:

                self.volumen_precios.append((key,value.get()))


            #RESULTADOS EN FORMA DE DICTIONARIO PARA LA CREACION DE UN DATAFRAME
            resultados = dict(self.valores_registrados + self.volumen_precios)

            matriz_resultados = pd.DataFrame([resultados])

            try:


                nombre = '/Users/josealonsoordinolaaucca/Documents/Documentos/Programacion/Proyecto GDA - Registro Compra Cacao/prueba.xlsx'
                matriz_resultados.to_excel(nombre,index=False)

            except:
                pass   

                
            return print('EJECUTADO')
        
        # def alertas_datos():
        #     print(self.valores_registrados[0][1])


        #-------------------------------------------------------------------------------------------
        ##BOTON REGISTRAR

        self.boton_registrar = tk.Button(self.marco_izquierdo,text='REGISTRAR',
                                         font=('Helvetica Neue',9,'bold'),
                                         fg='#289c8e',
                                         height=2,
                                         width=12,
                                         activebackground='#289c8e',
                                         activeforeground='white',
                                         relief='raised',
                                         borderwidth=6,
                                         cursor='hand2',
                                         command=lambda : (registro_compra())) 
                                        #  command=lambda : (registro_compra(),alertas_datos()))
        
        self.boton_registrar.place(x=620,y=235)


    def barra_menu(self):

        self.barra_menu = tk.Menu(self.root)
        self.root.config(menu=self.barra_menu)

        self.file_menu = tk.Menu(self.barra_menu,tearoff=0)
        self.barra_menu.add_cascade(label='Registro',menu=self.file_menu)

        # self.file_menu.add_command(label='Nuevo Registro')
        # self.file_menu.add_command(label='Eliminar Registros')
        self.file_menu.add_command(label='Salir',command=self.root.quit)

        


    # def marcos_inferiores(self):    