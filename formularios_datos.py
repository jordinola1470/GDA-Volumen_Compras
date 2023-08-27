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



