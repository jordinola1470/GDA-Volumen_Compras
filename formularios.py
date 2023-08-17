import tkinter as tk

'''FORMULARIO DE DATOS GENERALES DEL PRODUCTOR'''
def crear_datos_productor (parent):
    etiquetas = ['Nombres', 'Primer Apellido', 'Segundo Apellido','N° Documento']
    entries = ['#F2F3F4', '#F2F3F4', '#F2F3F4', '#F2F3F4']
    
    width = 40
    y = 20
    entry_vars = []
    first_entry = None
    
    for texto_etiqueta, bg_entry in zip(etiquetas, entries):
        etiqueta = tk.Label(parent, text=texto_etiqueta,bg='white',font=('Arial',10),fg='#0D3B66')
        etiqueta.place(x=20, y=y)

        entry_var = tk.StringVar()
        entry_var.set("")
        entry = tk.Entry(parent, bg=bg_entry, width=width, textvariable=entry_var,cursor='xterm')
        entry.place(x=140, y=y)

        entry_vars.append((texto_etiqueta,entry_var))

        if not first_entry:
            first_entry = entry

        y += 31
    
    if first_entry:
        first_entry.focus_set()

    return entry_vars

'''FORMULARIO DE CHECKBOX PARA GENERO DEL PRODUCTOR'''
def datos_genero(parent):

    etiqueta_genero = tk.Label(parent,text='Género',bg='white',font=('Arial',10),fg='#0D3B66')
    etiqueta_genero.place(x=20,y=140)

    genero_var = tk.StringVar()
    genero_var.set('masculino')

    masculino_radio = tk.Radiobutton(parent,text='Masculino',bg='white',variable=genero_var,value='masculino',cursor='hand2')
    femenino_radio  = tk.Radiobutton(parent,text='Femenino',bg='white',variable=genero_var,value='femenino',cursor='hand2')
    otro_radio      = tk.Radiobutton(parent,text='Otro',bg='white',variable=genero_var,value='otro',cursor='hand2')
    
    masculino_radio.place(x=140,y=140)
    femenino_radio.place(x=140,y=160)
    otro_radio.place(x=140,y=180)

    genero_resultado = [('Género',genero_var)]

    return genero_resultado

'''FORMULARIO DE CHECKBOX PARA TIPO DE PRODUCTOR'''
def datos_gda(parent):
    marco_gda = tk.LabelFrame(parent,
                              text='¿Beneficiario Cacao Conecta?',
                              font=('Arial',10),fg='#0D3B66',
                              bg='white',
                              borderwidth=2,
                              relief=tk.RIDGE,
                              width=360,height=80)
    marco_gda.place(x=20,y=210)

    #Booleanos de beneficiarios
    opcion_var = tk.BooleanVar()
    opcion_var.set(False)

    si_radio = tk.Radiobutton(marco_gda,text='Si',font=('Arial',9),fg='#0D3B66',cursor='hand2',variable=opcion_var,bg='white',value=True)
    no_radio = tk.Radiobutton(marco_gda,text='No',font=('Arial',9),fg='#0D3B66',cursor='hand2',variable=opcion_var,bg='white',value=False)

    si_radio.place(x=80,y=5)
    no_radio.place(x=20,y=5)

    #Codigo de Finca Cacao Conecta
    def mostrar_etiqueta(*args):
        if opcion_var.get():
            etiqueta_benef.place(x=140, y=5)
            etiqueta_benef_entry.place(x=160, y=30)  
            etiqueta_benef_entry.focus_set()
        else:
            etiqueta_benef.place_forget()
            etiqueta_benef_entry.place_forget()

    opcion_var.trace("w", mostrar_etiqueta)
    etiqueta_benef = tk.Label(marco_gda, text='COD Beneficiario / Finca',font=('Arial',10),fg='#0D3B66',bg='white')

    COD_benef = tk.StringVar()
    COD_benef.set('/GDA')
    
    etiqueta_benef_entry  = tk.Entry(marco_gda,bg='#F2F3F4',textvariable=COD_benef,width=30) 
    
    opcion_resultado = [('Beneficiario',opcion_var),('COD',COD_benef)]

    return opcion_resultado

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

    #Etiquetas Columnas
    for i,etiqueta in enumerate(['TIPO','PRECIO','CANTIDAD','TOTAL']):
        etiqueta_cacao = tk.Label(marco_volumen,text=etiqueta,font=('Arial',10,'bold'),fg='#0D3B66',bg='white')
        etiqueta_cacao.grid(row=1,column=0+i,sticky='w',pady=0,padx=2)

    #Checkbutton's
    ## Funcion Estado Columna 1 y 2
    def verificacion_check(*args):
        lista_widgets = [entries_lista,entries_listaCantidad,entries_listaTotal]
        for widget in lista_widgets:
            for j in range(len(widget)):
                if checkbox_states[j].get():
                    widget[j].config(state='normal')
                else :
                    widget[j].delete(0, tk.END)
                    widget[j].config(state='disabled')
                    
                   
    ## Checkbuttons-Valores            
    var_premium   = tk.BooleanVar()
    var_premium.set(True)

    var_regular   = tk.BooleanVar()
    var_corriente = tk.BooleanVar()

    ### Trace_Funcion
    checkbox_states = [var_premium,var_regular,var_corriente]
    for var in checkbox_states:
        var.trace('w', verificacion_check)
    
    ## Checkbuttons-Renderizacion/Etiqueta
    etiquetas = ['Premium','Regular','Corriente']
    for i,tipo in enumerate(etiquetas):
        tipo = tk.Checkbutton(marco_volumen, text=etiquetas[i], variable=checkbox_states[i],bg='white',cursor='hand2')
        tipo.grid(row=2+i,column=0,sticky='w',padx=3,pady=2)
    
    ##########################################################################################################################

    #Precio-Entry
    var_entry_premium   = tk.StringVar()
    var_entry_regular   = tk.StringVar()
    var_entry_corriente = tk.StringVar()

    entry_premium   = tk.Entry(marco_volumen, bg='#F2F3F4',disabledbackground='#616A6B', width=10, textvariable=var_entry_premium,state='normal')
    entry_regular   = tk.Entry(marco_volumen, bg='#F2F3F4',disabledbackground='#616A6B', width=10, textvariable=var_entry_regular,state='disabled')
    entry_corriente = tk.Entry(marco_volumen, bg='#F2F3F4',disabledbackground='#616A6B', width=10, textvariable=var_entry_corriente,state='disabled')
    
    valores_entry_precio = [var_entry_premium,var_entry_regular,var_entry_corriente]
    entries_lista = [entry_premium,entry_regular,entry_corriente]

    for i,tipo in enumerate(entries_lista):
        tipo.grid(row=2+i,column=1,sticky='w',padx=5)

    #Cantidad-Entry
    var_entry_premiumCantidad   = tk.StringVar()
    var_entry_regularCantidad   = tk.StringVar()
    var_entry_corrienteCantidad = tk.StringVar()

    cantidad_entry_premium   = tk.Entry(marco_volumen, bg='#F2F3F4',disabledbackground='#616A6B', width=10, textvariable=var_entry_premiumCantidad,state='normal')
    cantidad_entry_regular   = tk.Entry(marco_volumen, bg='#F2F3F4',disabledbackground='#616A6B', width=10, textvariable=var_entry_regularCantidad,state='disabled')
    cantidad_entry_corriente = tk.Entry(marco_volumen, bg='#F2F3F4',disabledbackground='#616A6B', width=10, textvariable=var_entry_corrienteCantidad,state='disabled')
    
    valores_entry_cantidad = [var_entry_premiumCantidad,var_entry_regularCantidad,var_entry_corrienteCantidad]
    entries_listaCantidad = [cantidad_entry_premium,cantidad_entry_regular,cantidad_entry_corriente]

    for i,tipo in enumerate(entries_listaCantidad):
        tipo.grid(row=2+i,column=2,sticky='w',padx=5)

    #Totales-Entry
    
    
    ## Multiplicacion Funcion
    
    def actualizar_totales(index):
        precio = entries_lista[index].get()
        cantidad = entries_listaCantidad[index].get()

        try:
            total = float(precio) * float(cantidad)
            entries_listaTotal[index].delete(0, tk.END)
            entries_listaTotal[index].insert(0, total)
        except:
            pass

    ## Trace - Precio/Cantidad
    for i in range(len(entries_lista)):
        var_entry_precio = valores_entry_precio[i]
        var_entry_cantidad = valores_entry_cantidad[i]
        var_entry_precio.trace_add("write", lambda *args, index=i: actualizar_totales(index))
        var_entry_cantidad.trace_add("write", lambda *args, index=i: actualizar_totales(index))
            
    var_total_premium = tk.StringVar()
    var_total_regular = tk.StringVar()
    var_total_corriente = tk.StringVar()

    total_entry_premium   = tk.Entry(marco_volumen, bg='#F2F3F4',disabledbackground='#616A6B', width=10, textvariable=var_total_premium,state='normal')
    total_entry_regular   = tk.Entry(marco_volumen, bg='#F2F3F4',disabledbackground='#616A6B', width=10, textvariable=var_total_regular,state='disabled')
    total_entry_corriente = tk.Entry(marco_volumen, bg='#F2F3F4',disabledbackground='#616A6B', width=10, textvariable=var_total_corriente,state='disabled')
    
    entries_listaTotal = [total_entry_premium,total_entry_regular,total_entry_corriente]

    for i,tipo in enumerate(entries_listaTotal):
        tipo.grid(row=2+i,column=3,sticky='w',padx=5)

    

    #Retorno de los valores ingresados en todo el bloque de widgets
    tipo_cacao_elegido = [('premium',var_premium),('regular',var_regular),('corriente',var_corriente)]
    


    return tipo_cacao_elegido,valores_entry_precio,valores_entry_cantidad