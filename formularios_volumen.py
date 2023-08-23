import tkinter as tk

'''TABLA DE REGISTRO DE VOLUMEN'''

def datos_volumen(parent):

    marco_volumen = tk.LabelFrame(parent,
                                  text='REGISTRO VOLUMEN CACAO',
                                  labelanchor=tk.NW,
                                  bg='white',
                                  font=('Arial',10,'bold underline'),fg='#0D3B66',
                                  borderwidth=2,
                                  relief=tk.RIDGE)
    
    marco_volumen.place(x=405,y=15)
    marco_volumen.config(padx=5,pady=15)

    #Nombre de las columnas 
    for i,etiqueta in enumerate(['TIPO','PRECIO','CANTIDAD','TOTAL']):
        etiqueta_cacao = tk.Label(marco_volumen,text=etiqueta,font=('Arial',10,'bold'),fg='#0D3B66',bg='white')
        etiqueta_cacao.grid(row=1,column=0+i,sticky='w',padx=2)

    #Nombre de las filas
    for i,etiqueta in enumerate(['Premium','Regular','Corriente']):
        etiqueta_cacao = tk.Label(marco_volumen,text=etiqueta,font=('Arial',10,'bold'),fg='#0D3B66',bg='white')
        etiqueta_cacao.grid(row=2+i,column=0,sticky='w',padx=3,pady=2)
    
    ########################

    ##Funcion de Multiplicacion
    def multiplicar(valores):
        lista_totales=[]
        for i in range(3):
            try: 
                precio = valores[i].get()
                cantidad = valores[i+3].get()
                total = float(precio) * float(cantidad)
                lista_totales.append(total)

            except:
                lista_totales.append(0)
        
        return lista_totales

    def actualizar_resultados(*args):
        etiquetas = multiplicar(resultado_volumen_valores)

        for i,tipo in enumerate(etiquetas):
            label = tk.Label(marco_volumen,text=etiquetas[i])
            label.grid(row=2+i,column=3,sticky='w',padx=5) 


    ##########################################################################################################################

    #PRECIO
    etiquetas = ['Precio_Premium','Precio_Regular','Precio_Corriente']
    width = 10
    entryPrecio_vars = []
    
    for i,texto in enumerate(etiquetas):
        entry_var = tk.StringVar()
        entry_var.set("")
        entry = tk.Entry(marco_volumen, bg='#F2F3F4', width=width, textvariable=entry_var,cursor='xterm')
        entry.grid(row=2+i,column=1,sticky='w',padx=5)

        entry_var.trace_add('write', actualizar_resultados)

        entryPrecio_vars.append((texto,entry_var))

    ##########################################################################################################################

    #CANTIDADES
    etiquetas = ['Cantidad_Premium','Cantidad_Regular','Cantidad_Corriente']
    width = 10
    entryCantidad_vars = []
    
    for i,texto in enumerate(etiquetas):
        entry_var = tk.StringVar()
        entry_var.set("")
        entry = tk.Entry(marco_volumen, bg='#F2F3F4', width=width, textvariable=entry_var,cursor='xterm')
        entry.grid(row=2+i,column=2,sticky='w',padx=5)

        entry_var.trace_add('write', actualizar_resultados)

        entryCantidad_vars.append((texto,entry_var))


    #TOTALES RENDERIZACION

    resultado_volumen = entryPrecio_vars + entryCantidad_vars
    resultado_volumen_valores = [valor for etiqueta, valor in resultado_volumen]

    for var in resultado_volumen_valores:
        var.trace_add('write', actualizar_resultados)

    return resultado_volumen
