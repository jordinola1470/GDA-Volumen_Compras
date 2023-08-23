import tkinter as tk
import pandas as pd
import os

from datetime import date
from openpyxl import load_workbook
from tkinter import messagebox

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

            #---------------------------------------------------------------------------------

            #RESULTADOS EN FORMA DE DICTIONARIO PARA LA CREACION DE UN DATAFRAME
            resultados = dict(self.valores_registrados + self.volumen_precios)
            matriz_resultados = pd.DataFrame([resultados])

            #CREACION DEL ARCHIVO EXCEL EN LA RUTA ESPECIFICA / INGRESO DE NUEVAS CELDAS   

            fecha  = (date.today()).strftime('%d%m%Y')
            nombre = str(f'matriz_registros_{fecha}.xlsx')

            directorio_actual = os.getcwd()
            directorio_madre  = os.path.dirname(directorio_actual)
            nombre_ruta = os.path.join(directorio_madre,nombre)
        
            if os.path.exists(nombre_ruta):
                workbook  = load_workbook(nombre_ruta)
                worksheet = workbook.active

                nueva_fila = []
                for valores in resultados.values():
                    nueva_fila.append(valores)

                worksheet.append(nueva_fila)
                workbook.save(nombre_ruta)
                
            else:
                matriz_resultados.to_excel(nombre_ruta,index=False) 
       
            return print('EJECUTADO')

        #-------------------------------------------------------------------------------------------
        ##AVISO
        def aviso_seguridad():
            resultado = messagebox.askokcancel('Aviso','¿Estás seguro de realizar el registro?')
            if resultado:
                registro_compra()
                messagebox.showinfo('Exito','La compra se ha registrado correctamente')


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
                                         command=lambda : ((aviso_seguridad()))) 
                                        #  command=lambda : (registro_compra(),alertas_datos()))
        
        self.boton_registrar.place(x=620,y=235)

    #--------------------------------------------------------------------------------------------------
    
    def barra_menu(self):

        self.barra_menu = tk.Menu(self.root)
        self.root.config(menu=self.barra_menu)

        self.file_menu = tk.Menu(self.barra_menu,tearoff=0)
        self.barra_menu.add_cascade(label='Registro',menu=self.file_menu)

        self.file_menu.add_command(label='Salir',command=self.root.quit)

          