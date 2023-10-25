from tkinter import *
from ttkbootstrap import *
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
import os
import sqlite3
from datetime import *
import string
from dateutil.relativedelta import relativedelta
from ttkbootstrap.validation import add_regex_validation

class App:
    # constructor de clase
    def __init__(self,root,c,conn):
        self.wind = root
        self.icono = 'unnamed.ico'
        self.wind.title('Automatización de Carga')
        self.wind.resizable(False,False)
        self.wind.iconbitmap(self.icono)
        self.wind.geometry('+560+240')
        self.c = c
        self.conn = conn
        #-------------------------------MAIN--------------------------------------------------#
        titulo=ttk.Label(self.wind, text='Sistema de carga.', font=('Time New Roman', 28),
                            foreground='#fff').grid(row=0, column=0, columnspan=4, pady=(10, 10), padx=(250))
        # ----------------------------------------------------------------------------------#

        content = ttk.LabelFrame(self.wind, text='Menú',
                                padding=10, borderwidth=3, relief="ridge")
        content.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        # ----------------------------------------------------------------------------------#
        # ----------------------------------TITULAR---------------------------------------------#
        #   BTN Y LABEL CARGA TITULAR
        ttk.Label(content, text='Titular', font=(
            'Time New Roman', 14), padding=5, borderwidth=3, relief="groove", anchor=W).grid(row=0, column=0, sticky="nsew", pady=10)
        btn_carga_tit = ttk.Button(
        content, text='Cargar Titular', command=self.carga_titular)
        btn_carga_tit.grid(row=0, column=1, pady=8, padx=10, sticky="ew")
        #   BTN Buscar Titular
        btn_buscarTitular = ttk.Button(
            content, text='Buscar Titular', command=lambda: self.buscar_dni('Titular'))
        btn_buscarTitular.grid(row=0, column=2, pady=8, padx=10, sticky="ew")

        # ----------------------------------------------------------------------------------#

        # ----------------------------------Cónyuge------------------------------------------------#
        #   BTN Y LABEL CARGA CONYUGE
        cargaConyuge = ttk.Label(content, text='Cónyuge', font=(
            'Time New Roman', 14), padding=5, borderwidth=3, relief="groove", anchor=W)
        cargaConyuge.grid(row=2, column=0, sticky="nsew", pady=10)

        btn_carga_cony = ttk.Button(
            content, text='Cargar Cónyuge', command=self.carga_conyuge)
        btn_carga_cony.grid(row=2, column=1, pady=8, padx=10, sticky="ew")
        #   BTN Buscar Cónyuge
        btn_buscarConyuge = ttk.Button(
            content, text='Buscar Cónyuge', command=lambda: self.buscar_dni('Cónyuge'))
        btn_buscarConyuge.grid(row=2, column=2, pady=8, padx=10, sticky='ew')
        # ----------------------------------------------------------------------------------#

        # ----------------------------------Hijo/s------------------------------------------------#
        #   BTN Y LABEL CARGA HIJO
        cargaHijo = ttk.Label(content, text='Hijo/s', font=(
            'Time New Roman', 14), padding=5, borderwidth=3, relief="groove", anchor=W)
        cargaHijo.grid(row=3, column=0, sticky="nsew", pady=10)
        btn_carga_hijo = ttk.Button(
            content, text='Cargar Hijo/s', command=self.carga_hijo)
        btn_carga_hijo.grid(row=3, column=1, pady=8, padx=10, sticky="ew")
        #   BTN Buscar Hijo
        btn_buscarHijo = ttk.Button(
            content, text='Buscar Hijo/s', command=lambda: self.buscar_dni('Hijo/s'))
        btn_buscarHijo.grid(row=3, column=2, pady=8, padx=10, sticky='ew')
        # ----------------------------------------------------------------------------------#


        # ----------------------------------Resultado de LLamada------------------------------------------------#
        # BTN Carga de Resultado de LLamada
        cargaLlamadaTit = ttk.Label(content, text='Cargar Resultado de Llamada', font=(
            'Time New Roman', 14), padding=5, borderwidth=3, relief="groove", anchor=W)
        cargaLlamadaTit.grid(row=0, column=4, sticky="nsew", pady=10)
        btn_cargaLlamadaTit = ttk.Button(content, text= 'Cargar Resultado de Llamada', command=self.cargar_llamada)
        btn_cargaLlamadaTit.grid(row=0, column=5, pady=8, padx=10, sticky="ew")
                
                # BTN SALIR
        btnSalir=ttk.Button(self.wind, text='Salir', command=lambda:self.wind.quit()).grid(column=3, row=5)    
    
    #Abecedario en mayúscula
    def listAlphabetUpper(self):
        return list(string.ascii_lowercase.upper())

    #Abecedario en minúscula
    def listAlphabetLower(self):
        return list(string.ascii_lowercase.lower())
    
    def definir_edad(self,fecha):
        # calcula la Edad según la fecha de nacimiento que le pasemos en la carga.
        fecha = fecha.replace('-', '/')
        fecha_nacimiento = datetime.strptime(fecha, "%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        return edad.years

    #Valida que los Entry solo sean números
    def validar_Enreys_Solo_Numeros(self,entry):
        return add_regex_validation(entry,r'^[0-9]*$')

    #Valida que los Entry solo sean letras
    def validar_Enreys_Solo_Letras(self,entry):
        return add_regex_validation(entry,r'^[a-zA-Z ]*$')
    
    #       TITULAR.
    def carga_titular(self):
        self.top = Toplevel()
        self.top.iconbitmap(self.icono)
        self.top.resizable(False,False)
        self.top.geometry('+830+240')
        """_summary_
        Lo que hace esta función es dar pie al carga del Titular, creando una nueva ventana, que a su vez contiene otra función la cual se encarga de exponer 
            y guardar la carga de datos.
        """

        #Datos de carga

        x = ttk.LabelFrame(self.top, text='Titular', padding=5,
                    borderwidth=3, relief="ridge")
        x.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

            #DNI
        ttk.Label(x, text='DNI:', font=('Time New Roman', 14),
                        borderwidth=3, relief="groove", anchor=W).grid(row=0, column=0, sticky="nsew", pady=8)
        self.dni = ttk.Entry(x, width=40, font=(16))
        self.dni.focus()
        self.dni.grid(row=0, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Numeros(self.dni)
        

            #Nombre
        ttk.Label(x, text='Nombre/s:', font=('Time New Roman', 14),
                            borderwidth=3, relief="groove").grid(row=1, column=0, sticky="nsew", pady=8)
        self.nombre = ttk.Entry(x, width=40, font=(16))
        self.nombre.grid(row=1, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Letras(self.nombre)
            
            #Apellido
        ttk.Label(x, text='Apellido/s:', font=('Time New Roman', 14),
                            borderwidth=3, relief="groove", anchor=W).grid(row=2, column=0, sticky="nsew", pady=8)
        self.apellido = ttk.Entry(x, width=40, font=(16))
        self.apellido.grid(row=2, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Letras(self.apellido)
            
            #cuil/cuit
        ttk.Label(x, text='CUIL / CUIT:', font=('Time New Roman', 14),
                                borderwidth=3, relief="groove", anchor=W).grid(row=3, column=0, sticky="nsew", pady=8)
        self.cuil_cuit = ttk.Entry(x, width=40, font=(16))
        self.cuil_cuit.grid(row=3, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Numeros(self.cuil_cuit)

            #Fecha de nacimiento
        ttk.Label(x, text='Fecha de Nacimiento:', font=(
                'Time New Roman', 14), borderwidth=3, relief="groove", anchor=W).grid(row=4, column=0, sticky="nsew", pady=8)
        self.sel = StringVar()
        self.fNacimiento = ttk.DateEntry(
                x, bootstyle='solar', dateformat='%d-%m-%Y', firstweekday=0)
        self.fNacimiento.grid(row=4, column=1, pady=8, padx=10)

            #Teléfono
        ttk.Label(x, text='Teléfono:', font=('Time New Roman', 14),
                                borderwidth=3, relief="groove", anchor=W).grid(row=6, column=0, sticky="nsew", pady=8)
        self.telef = ttk.Entry(x, width=40, font=(16))
        self.telef.grid(row=6, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Numeros(self.telef)

            #Mail
        ttk.Label(x, text='Mail:',  font=('Time New Roman', 14),
                            borderwidth=3, relief="groove", anchor=W).grid(row=7, column=0, sticky="nsew", pady=8)
        self.mail = ttk.Entry(x, width=40, font=(16))
        self.mail.grid(row=7, column=1, pady=8, padx=10)

            #Localidad de Residencia
        ttk.Label(x, text='Localidad de residencia:', font=(
                'Time New Roman', 14), borderwidth=3, relief="groove", anchor=W).grid(row=8, column=0, sticky="nsew", pady=8)
        self.localidad_r = ttk.Entry(x, width=40, font=(16))
        self.localidad_r.grid(row=8, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Letras(self.localidad_r)
            
            #Nota con respecto al cliente
        ttk.Label(x, text='Nota:', font=(
                'Time New Roman', 14), borderwidth=3, relief="groove", anchor=W).grid(row=9, column=0, sticky="nsew", pady=8)
        self.nota = ttk.Entry(x, width=40, font=(16))
        self.nota.grid(row=9, column=1, pady=8, padx=10)
            
            # ---------------------------------------------------------------------#

        def guardar():
                """_summary_
                    Guarda los datos y aplica el button guardar el cual si un campo no esta completo se le da un mensaje al usuario.
                """
                self.fecha = self.fNacimiento.entry.get()
                self.edad = self.definir_edad(self.fecha)
                self.ahora = datetime.date(datetime.now())
                if not self.dni.get():
                    Messagebox.show_error(
                        'El campo "DNI" es obligatorio.', 'Error')
                    return
                elif not self.nombre.get():
                    Messagebox.show_error(
                        'El campo "Nombre/s" es obligatorio.', 'Error')
                    return
                elif not self.apellido.get():
                    Messagebox.show_error(
                        'El campo "Apellido/s" es obligatorio.', 'Error')
                    return
                elif not self.cuil_cuit.get:
                    Messagebox.show_error(
                        'El campo "CUIL / CUIT" es obligatorio.''Error')
                    return
                elif not self.fNacimiento.entry.get():
                    Messagebox.show_error(
                        'El campo "Fecha de Nacimiento" es obligatorio.', 'Error')
                    return
                elif not self.telef.get():
                    Messagebox.show_error(
                        'El campo "Teléfono" es obligatorio.', 'Error')
                    return
                elif not self.mail.get():
                    Messagebox.show_error(
                        'El campo "Mail" es obligatorio.', 'Error')
                    return
                elif not self.localidad_r.get():
                    Messagebox.show_error(
                        'El campo "Localidad de residencia" es obligatorio.', 'Error')
                    return
                elif not self.nota.get():
                    Messagebox.show_error(
                        'El campo "Nota" es obligatorio.', 'Error')
                    return
                
                try:
                    #si los campos fueron llenados con exito, agrupa los mismos en un diccionarios para despues usarlos para guardar en su respectiva tabla
                    self.resultados = {
                        'DNITIT': int(self.dni.get()),
                        'NOMTIT': self.nombre.get(),
                        'APETIT': self.apellido.get(),
                        'CUIL_CUIT_TIT': int(self.cuil_cuit.get()),
                        'FNATIT': self.fNacimiento.entry.get(),
                        'EDATIT': self.edad,
                        'TELTIT': int(self.telef.get()),
                        'MAILTIT': self.mail.get(),
                        'LOCTIT': self.localidad_r.get(),
                        'FCHTIT': self.ahora,
                        'NOTTIT':self.nota.get()
                    }
                    rows = self.c.execute(
                    """SELECT * From Titular WHERE DNITIT = ?""", (self.resultados['DNITIT'], )).fetchall()

                    if not rows:
                        # Messagebox.show_info(
                        #     '¡¡¡EL contenido fue Enviado con éxito 👌!!!', 'Enviado')
                        self.insertar_Titular(self.resultados)
                        self.top.destroy()
                    else:
                        Messagebox.show_error(
                        f'Ya existe un registro con el DNI: {self.resultados["DNITIT"]}', 'Error')
                        return

                except ValueError:
                    Messagebox.show_warning(
                        'Verifique los CAMPOS', 'Error en algun Campo')
        ttk.Button(self.top, text='Guardar', command=guardar).grid(column=2, row=3, padx=15, pady=15)
        self.top.mainloop()
    
    def insertar_Titular(self,resultados):
        """insertar datos titular
            hace un comit de los datos recopilados de los entry para guardarlos en la DB correspondiente
        """
        self.c.execute("""
                INSERT INTO Titular (DNITIT,NOMTIT,APETIT,CUIL_CUIT_TIT,FNATIT,EDATIT,TELTIT,MAILTIT,LOCTIT,FCHTIT,NOTTIT) VALUES(?,?,?,?,?,?,?,?,?,?,?)
            """, (self.resultados['DNITIT'], self.resultados['NOMTIT'], self.resultados['APETIT'], self.resultados['CUIL_CUIT_TIT'], self.resultados['FNATIT'], self.resultados['EDATIT'], self.resultados['TELTIT'], self.resultados['MAILTIT'], self.resultados['LOCTIT'], self.resultados['FCHTIT'], self.resultados['NOTTIT']))
        self.conn.commit()
    
    #       CÓNYUGE.
    def carga_conyuge(self):
        self.top = Toplevel()
        self.top.title('Carga Cónyuge')
        self.top.resizable(False, False)
        self.top.iconbitmap('unnamed.ico')
        self.top.geometry('+830+240')
        # top.configure(background='#304c94')

        """carga_conyuge
            Lo que hace esta función es dar pie al carga del Conyuge, creando una nueva ventana, que a su vez contiene otra función la cual se encarga de exponer 
                y guardar la carga de datos 

        """
        
        x = ttk.LabelFrame(self.top, text='Cónyuge', padding=5,
                            borderwidth=3, relief="ridge")
        x.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

        ttk.Label(x, text='DNI:',  font=('Time New Roman', 14),
                            borderwidth=3, relief="groove", anchor=W).grid(row=0, column=0, sticky="nsew", pady=8)
        self.dni = ttk.Entry(x, width=40, font=(16))
        self.dni.focus()
        self.dni.grid(row=0, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Numeros(self.dni)

        ttk.Label(x, text='Nombre/s:', font=('Time New Roman', 14),
                                borderwidth=3, relief="groove").grid(row=1, column=0, sticky="nsew", pady=8)
        self.nombre = ttk.Entry(x, width=40, font=(16))
        self.nombre.grid(row=1, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Letras(self.nombre)

        ttk.Label(x, text='Apellido/s:', font=('Time New Roman', 14),
                                borderwidth=3, relief="groove", anchor=W).grid(row=2, column=0, sticky="nsew", pady=8)
        self.apellido = ttk.Entry(x, width=40, font=(16))
        self.apellido.grid(row=2, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Letras(self.apellido)

        ttk.Label(x, text='CUIL / CUIT:', font=('Time New Roman', 14),
                                    borderwidth=3, relief="groove", anchor=W).grid(row=3, column=0, sticky="nsew", pady=8)
        self.cuil_cuit = ttk.Entry(x, width=40, font=(16))
        self.cuil_cuit.grid(row=3, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Numeros(self.cuil_cuit)

        ttk.Label(x, text='Fecha de Nacimiento:', font=(
                'Time New Roman', 14), borderwidth=3, relief="groove", anchor=W).grid(row=4, column=0, sticky="nsew", pady=8)
        self.sel = StringVar()
        self.fNacimiento = ttk.DateEntry(
                x, bootstyle='solar', dateformat='%d-%m-%Y', firstweekday=0)
        self.fNacimiento.grid(row=4, column=1, pady=8, padx=10)

        ttk.Label(x, text='Teléfono:', font=('Time New Roman', 14),
                                borderwidth=3, relief="groove", anchor=W).grid(row=6, column=0, sticky="nsew", pady=8)
        self.telef = ttk.Entry(x, width=40, font=(16))
        self.telef.grid(row=6, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Numeros(self.telef)

        ttk.Label(x, text='Mail:', font=('Time New Roman', 14),
                            borderwidth=3, relief="groove", anchor=W).grid(row=7, column=0, sticky="nsew", pady=8)
        self.mail = ttk.Entry(x, width=40, font=(16))
        self.mail.grid(row=7, column=1, pady=8, padx=10)

        ttk.Label(x, text='Localidad de residencia:', font=(
                'Time New Roman', 14), borderwidth=3, relief="groove", anchor=W).grid(row=8, column=0, sticky="nsew", pady=8)
        self.localidad_r = ttk.Entry(x, width=40, font=(16))
        self.localidad_r.grid(row=8, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Letras(self.localidad_r)

        ttk.Label(x, text='DNI Titular', font=(
                'Time New Roman', 14), borderwidth=3, relief="groove", anchor=W).grid(row=9, column=0, sticky="nsew", pady=8)
        self.Tit_DNITIT = ttk.Entry(x, width=40, font=(16))
        self.Tit_DNITIT.grid(row=9, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Numeros(self.Tit_DNITIT)
            # ---------------------------------------------------------------------#

        def guardar():
                """_summary_
                    Guarda los datos y aplica el button guardar el cual si un campo no esta completo se le da un mensaje al usuario.
                """
                
            

                if not self.dni.get():
                    Messagebox.show_error(
                        'El campo "DNI" es obligatorio.', 'Error')
                    return
                elif not self.nombre.get():
                    Messagebox.show_error(
                        'El campo "Nombre/s" es obligatorio.', 'Error')
                    return
                elif not self.apellido.get():
                    Messagebox.show_error(
                        'El campo "Apellido/s" es obligatorio.', 'Error')
                    return
                elif not self.cuil_cuit.get:
                    Messagebox.show_error(
                        'El campo "CUIL / CUIT" es obligatorio.''Error')
                    return
                elif not self.fNacimiento.entry.get():
                    Messagebox.show_error(
                        'El campo "Fecha de Nacimiento" es obligatorio.', 'Error')
                    return

                elif not self.telef.get():
                    Messagebox.show_error(
                        'El campo "Teléfono" es obligatorio.', 'Error')
                    return
                elif not self.mail.get():
                    Messagebox.show_error(
                        'El campo "Mail" es obligatorio.', 'Error')
                    return
                elif not self.localidad_r.get():
                    Messagebox.show_error(
                        'El campo "Localidad de residencia" es obligatorio.', 'Error')
                    return

                try:
                    #si los campos fueron llenados con exito, agrupa los mismos en un diccionarios para despues usarlos para guardar en su respectiva tabla
                    self.fecha = self.fNacimiento.entry.get()
                    self.edad = self.definir_edad(self.fecha)
                    self.ahora = datetime.date(datetime.now())
                    self.resultados = {
                        'DNICON': int(self.dni.get()),
                        'NOMCON': self.nombre.get(),
                        'APECON': self.apellido.get(),
                        'CUIL_CUIT_CON': int(self.cuil_cuit.get()),
                        'FNACON': self.fNacimiento.entry.get(),
                        'EDACON': self.edad,
                        'TELCON': int(self.telef.get()),
                        'MAILCON': self.mail.get(),
                        'LOCCON': self.localidad_r.get(),
                        'FCHCON': self.ahora,
                        'Titular_DNITIT': int(self.Tit_DNITIT.get())
                    }
                    rows = self.c.execute(
                    """SELECT * From Conyuge WHERE DNICON = ?""", (self.resultados['DNICON'], )).fetchall()

                    if not rows:
                        # Messagebox.show_info(
                        #     '¡¡¡EL contenido fue Enviado con éxito 👌!!!', 'Enviado')
                        self.insertar_Conyuge(self.resultados)
                        self.top.destroy()
                    else:
                        Messagebox.show_error(
                        f'Ya existe un registro con el DNI: {self.resultados["DNITIT"]}', 'Error')
                        return
                except ValueError:
                    Messagebox.show_warning(
                        'Verifique los CAMPOS', 'Error en algun Campo')

        ttk.Button(self.top, text='Guardar', command=guardar).grid(column=2, row=3, padx=15, pady=15)
        self.top.mainloop()
            
    def insertar_Conyuge(self,resultados):
        """insertar datos conyuge
            hace un comit de los datos recopilados de los entry para guardarlos en la DB correspondiente
        """
        self.c.execute("""
            INSERT INTO Conyuge (DNICON,NOMCON,APECON,CUIL_CUIT_CON,FNACON,EDACON,TELCON,MAILCON,LOCCON,FCHCON,Titular_DNITIT) VALUES(?,?,?,?,?,?,?,?,?,?,?)
        """, (self.resultados['DNICON'], self.resultados['NOMCON'], self.resultados['APECON'], self.resultados['CUIL_CUIT_CON'], self.resultados['FNACON'], self.resultados['EDACON'], self.resultados['TELCON'], self.resultados['MAILCON'], self.resultados['LOCCON'], self.resultados['FCHCON'], self.resultados['Titular_DNITIT']))
        self.conn.commit()

    #       HIJO.
    def carga_hijo(self):
        self.top = Toplevel()
        self.top.title('Carga Cónyuge')
        self.top.resizable(False, False)
        self.top.iconbitmap('unnamed.ico')
        self.top.geometry('+830+240')

        """carga_hijo
            Lo que hace esta función es dar pie al carga del Hijo, creando una nueva ventana, que a su vez contiene otra función la cual se encarga de exponer 
                y guardar la carga de datos 

        """
    

        x = ttk.LabelFrame(self.top, text='Hijo', padding=5,
                           borderwidth=3, relief="ridge")
        x.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

        ttk.Label(x, text='DNI:',  font=('Time New Roman', 14),
                          borderwidth=3, relief="groove", anchor=W).grid(row=0, column=0, sticky="nsew", pady=8)
        self.dni = ttk.Entry(x, width=40, font=(16))
        self.dni.focus()
        self.dni.grid(row=0, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Numeros(self.dni)

        ttk.Label(x, text='Nombre/s:', font=('Time New Roman', 14),
                             borderwidth=3, relief="groove").grid(row=1, column=0, sticky="nsew", pady=8)
        self.nombre = ttk.Entry(x, width=40, font=(16))
        self.nombre.grid(row=1, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Letras(self.nombre)

        ttk.Label(x, text='Apellido/s:', font=('Time New Roman', 14),
                               borderwidth=3, relief="groove", anchor=W).grid(row=2, column=0, sticky="nsew", pady=8)
        self.apellido = ttk.Entry(x, width=40, font=(16))
        self.apellido.grid(row=2, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Letras(self.apellido)

        ttk.Label(x, text='CUIL / CUIT:', font=('Time New Roman', 14),
                                borderwidth=3, relief="groove", anchor=W).grid(row=3, column=0, sticky="nsew", pady=8)
        self.cuil_cuit = ttk.Entry(x, width=40, font=(16))
        self.cuil_cuit.grid(row=3, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Numeros(self.cuil_cuit)

        ttk.Label(x, text='Fecha de Nacimiento:', font=(
            'Time New Roman', 14), borderwidth=3, relief="groove", anchor=W).grid(row=4, column=0, sticky="nsew", pady=8)
        self.fNacimiento = ttk.DateEntry(
            x, bootstyle='solar', dateformat='%d-%m-%Y', firstweekday=0)
        self.fNacimiento.grid(row=4, column=1, pady=8, padx=10)

        

        ttk.Label(x, text='Hijo de:', font=(
            'Time New Roman', 14), borderwidth=3, relief="groove", anchor=W).grid(row=7, column=0, sticky="nsew", pady=8)
        lista_datos = ['-----------',
                       'Titular',
                       'Cónyuge',
                       'Titular y Cónyuges'
                       ]
        # value es el valor asignado de la lista desplegable
        self.value = StringVar()
        self.value.set(lista_datos[0])
        hijo_de = OptionMenu(x, self.value, *lista_datos)
        hijo_de.grid(row=7, column=1, pady=8, padx=10)

        ttk.Label(x, text='Localidad de residencia:', font=(
            'Time New Roman', 14), borderwidth=3, relief="groove", anchor=W).grid(row=8, column=0, sticky="nsew", pady=8)
        self.localidad_r = ttk.Entry(x, width=40, font=(16))
        self.localidad_r.grid(row=8, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Letras(self.localidad_r)

        ttk.Label(x, text='DNI Titular', font=(
            'Time New Roman', 14), borderwidth=3, relief="groove", anchor=W).grid(row=9, column=0, sticky="nsew", pady=8)
        self.Tit_DNITIT = ttk.Entry(x, width=40, font=(16))
        self.Tit_DNITIT.grid(row=9, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Numeros(self.Tit_DNITIT)
        # ---------------------------------------------------------------------#

        def guardar():
            """_summary_
                Guarda los datos y aplica el button guardar el cual si un campo no esta completo se le da un mensaje al usuario.
            """

            

            if not self.dni.get():
                Messagebox.show_error(
                    'El campo "DNI" es obligatorio.', 'Error')
                return
            elif not self.nombre.get():
                Messagebox.show_error(
                    'El campo "Nombre/s" es obligatorio.', 'Error')
                return
            elif not self.apellido.get():
                Messagebox.show_error(
                    'El campo "Apellido/s" es obligatorio.', 'Error')
                return
            elif not self.cuil_cuit.get:
                Messagebox.show_error(
                    'El campo "CUIL / CUIT" es obligatorio.''Error')
                return
            elif not self.fNacimiento.entry.get():
                Messagebox.show_error(
                    'El campo "Fecha de Nacimiento" es obligatorio.', 'Error')
                return

            elif not self.value.get():
                Messagebox.show_error(
                    'El campo "Mail" es obligatorio.', 'Error')
                return
            elif not self.localidad_r.get():
                Messagebox.show_error(
                    'El campo "Localidad de residencia" es obligatorio.', 'Error')
                return

            try:
                #si los campos fueron llenados con exito, agrupa los mismos en un diccionarios para despues usarlos para guardar en su respectiva tabla
                self.fecha = self.fNacimiento.entry.get()
                self.edad = self.definir_edad(self.fecha)
                if self.edad >= 18:
                    self.mayor = 'Si'
                else:
                    self.mayor = 'No'
                self.ahora = datetime.date(datetime.now())
                self.resultados = {
                    'DNIHIJ': int(self.dni.get()),
                    'NOMHIJ': self.nombre.get(),
                    'APEHIJ': self.apellido.get(),
                    'CUIL_CUIT_HIJ': int(self.cuil_cuit.get()),
                    'FNAHIJ': self.fNacimiento.entry.get(),
                    'EDAHIJ': self.edad,
                    'MAYORHIJ': self.mayor,
                    'LOCHIJ': self.localidad_r.get(),
                    'PDSHIJ': str(self.value.get()),
                    'FCHHIJ': self.ahora,
                    'DNITIT_HIJO': int(self.Tit_DNITIT.get())
                }
                rows = self.c.execute(
                """SELECT * From Hijo WHERE DNIHIJ = ?""", (self.resultados['DNIHIJ'], )).fetchall()

                if not rows:
                    # Messagebox.show_info(
                    #     '¡¡¡EL contenido fue Enviado con éxito 👌!!!', 'Enviado')
                    self.insertar_Hijo(self.resultados)
                    self.top.destroy()
                else:
                    Messagebox.show_error(
                    f'Ya existe un registro con el DNI: {self.resultados["DNIHIJ"]}', 'Error')
                    return

            except ValueError:
                Messagebox.show_warning(
                    'Verifique los CAMPOS', 'Error en algun Campo')

        ttk.Button(self.top, text='Guardar', command=guardar).grid(column=2, row=3, padx=15, pady=15)
        self.top.mainloop()
        # ---------------------------------------------------------------------#

    def insertar_Hijo(self,resultados):
        """insertar datos hijo
            hace un comit de los datos recopilados de los entry para guardarlos en la DB correspondiente
        """
        self.c.execute("""
            INSERT INTO Hijo (DNIHIJ,NOMHIJ,APEHIJ,CUIL_CUIT_HIJ,FNAHIJ,EDAHIJ,MAYORHIJ,LOCHIJ,PDSHIJ,FCHHIJ,DNITIT_HIJO) VALUES(?,?,?,?,?,?,?,?,?,?,?)
        """, (self.resultados['DNIHIJ'], self.resultados['NOMHIJ'], self.resultados['APEHIJ'], self.resultados['CUIL_CUIT_HIJ'], self.resultados['FNAHIJ'], self.resultados['EDAHIJ'], self.resultados['MAYORHIJ'], self.resultados['LOCHIJ'], self.resultados['PDSHIJ'], self.resultados['FCHHIJ'], self.resultados['DNITIT_HIJO']))
        self.conn.commit()
    
    #   Carga de Resultado de LLamada
    def cargar_llamada(self):
        """Carga los resultados de las llamada a los clientes.
        """
        self.top = Toplevel()
        self.top.title('Carga de Resultado de LLamada')
        self.top.resizable(False, False)
        self.top.iconbitmap('unnamed.ico')
        self.top.geometry('+830+240')
        

        
        x = ttk.LabelFrame(self.top, text='Datos Llamada', padding=5,
                            borderwidth=3, relief="ridge")
        x.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)
        #   DNI
        ttk.Label(x, text='DNI:',  font=('Time New Roman', 14),
                            borderwidth=3, relief="groove", anchor=W).grid(row=0, column=0, sticky="nsew", pady=8)
        self.dni = ttk.Entry(x, width=40, font=(16))
        self.dni.focus()
        self.dni.grid(row=0, column=1, pady=8, padx=10)
        self.validar_Enreys_Solo_Numeros(self.dni)
        #   VENTA
        ttk.Label(x,text='Vendido',  font=('Time New Roman', 14),
                            borderwidth=3, relief="groove", anchor=W).grid(row=1,column=0,sticky="nsew", pady=8)
        lista_datos = ['-----------',
                        'Si',
                        'No'
                        ]
            # value es el valor asignado de la lista desplegable
        self.resultado_vendido = StringVar()
        self.resultado_vendido.set(lista_datos[0])
        ventas = OptionMenu(x, self.resultado_vendido, *lista_datos)
        ventas.grid(row=1, column=1, pady=8, padx=10)
        #   Breve descripcion del Resultado del Llamado.
        ttk.Label(x,text='Resultado \n     del\n Llamado ',  font=('Time New Roman', 14),
                            borderwidth=3, relief="groove", anchor=W).grid(row=2,column=0,sticky="nsew", pady=8)
        self.result_llamado = ttk.Entry(x,font=(16),width=100)
        self.result_llamado.grid(row=2,column=1,padx=10,pady=8)

        def guardar():
                if not self.dni.get():
                    Messagebox.show_error(
                        'El campo "DNI" es obligatorio.', 'Error')
                    return
                elif not self.resultado_vendido.get():
                    Messagebox.show_error('El campo "Vendido" es obligatorio.', 'Error')
                try:
                    #si los campos fueron llenados con exito, agrupa los mismos en un diccionarios para despues usarlos para guardar en su respectiva tabla
                    self.ahora = datetime.date(datetime.now())
                    self.resultados = {'LVENT_DNITIT':self.dni.get(),
                                'VENTA':str(self.resultado_vendido.get()),
                                'FECHA_VENTA':self.ahora,
                                'RESULT_LLAMADO':self.result_llamado.get()
                                }
                    # Messagebox.show_info(
                    #     '¡¡¡EL contenido fue Guardado con éxito 👌!!!', 'Guardado')
                    self.insertar_resultado_llamada(self.resultados)
                    self.top.destroy()
                except ValueError:
                    Messagebox.show_warning(
                        'Verifique los CAMPOS', 'Error en algun Campo')
                
        ttk.Button(self.top, text='Guardar', command=guardar).grid(column=2, row=3, padx=15, pady=15)
        self.top.mainloop()

    #   Insertar Resultado de LLamada
    def insertar_resultado_llamada(self,resultados):
        """Inserta en la tabla Llamados_Ventas lo recopilado al guardar"""
        self.c.execute("""
            INSERT INTO Llamados_Ventas (RESULT_LLAMADO,VENTA,FECHA_VENTA,LVENT_DNITIT) VALUES(?,?,?,?)
        """, (self.resultados['RESULT_LLAMADO'], self.resultados['VENTA'], self.resultados['FECHA_VENTA'], self.resultados['LVENT_DNITIT']))
        self.conn.commit()




    # Busquedas.

    #   BUSCAR DNI
    def buscar_dni(self,quien):
        """buscar_dni
            Lo que hace es tomar el DNI ingresado segun de (quien) lo solicita si es Hijo, cónyuge o  Titular.

            return: todos los datos relacionados con el individuo, no los de cotización u otros.
        """

        self.top = Toplevel()
        self.top.title('Buscar')
        

        self.top.iconbitmap('unnamed.ico')
        quien = quien
        self.estilo = ttk.Style()
        self.estilo.configure("mystyle.Treeview", font=(
            'Time New Roman', 10), background='#DCE6F2', foreground='#000')

        def extraer_datos_dni(self,quien, dato):
            quien = str(quien)
            if quien == 'Titular':
                rows = self.c.execute(
                    """SELECT * From Titular WHERE DNITIT = ?""", (self.dato['DNI'], )).fetchall()
            if quien == 'Cónyuge':
                rows = self.c.execute(
                    """SELECT * From Conyuge WHERE DNICON = ?""", (self.dato['DNI'], )).fetchall()
            if quien == 'Titular_DNITIT':
                rows = self.c.execute(
                    """SELECT * From Conyuge WHERE Titular_DNITIT = ?""", (self.dato['DNI_T'], )).fetchall()
            if quien == 'Hijo/s':
                rows = self.c.execute(
                    """SELECT * From Hijo WHERE DNIHIJ = ?""", (self.dato['DNI'], )).fetchall()
            if quien == 'DNITIT_HIJO':
                rows = self.c.execute(
                    """SELECT * From Hijo WHERE DNITIT_HIJO = ?""", (self.dato['DNI_T'], )).fetchall()
            if not rows:
                Messagebox.show_warning(
                    f'No existe ningun registro con ese DNI', 'Error')
            self.tree.delete(*self.tree.get_children())
            if quien == 'Hijo/s' or quien == 'Cónyuge' or quien == 'Titular_DNITIT' or quien == 'DNITIT_HIJO':
                for row in rows:
                    self.tree.insert('', END, row[0], values=(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[10]))
            else:
                for row in rows:
                    self.tree.insert('', END, row[0], values=(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[10]))
        # ---------------------------------------------------------------------#

        def buscar(self,quien):
            # gurada los datos en diccionarios para despues poder hacer el select correspondiente
            try:
                if quien == 'Hijo/s' or quien == 'Cónyuge' or quien == 'Titular_DNITIT' or quien == 'DNITIT_HIJO':
                    self.dato = {'DNI': self.dni.get(),
                            'DNI_T': self.dni_t.get()}
                    extraer_datos_dni(quien, self.dato)
                else:
                    self.dato = {'DNI': self.dni.get()}
                    extraer_datos_dni(quien, self.dato)
            except ValueError:
                Messagebox.show_warning(
                    'Verifique los CAMPOS', 'Error en algun Campo')

        # ---------------------------------------------------------------------#
        y = ttk.LabelFrame(self.top,
                            padding=5, borderwidth=3, relief="ridge")
        y.grid(row=2, column=0, padx=10, pady=10)
        self.tree = ttk.Treeview(y, bootstyle='success', style="mystyle.Treeview")
        if quien == 'Hijo/s':
            # Grilla de datos Hijo.
            self.tree['columns'] = ('DNI', 'Nombre', 'Apellido', 'CUIL/CUIT', 'Fecha_de_Nacimiento',
                                    'Edad', 'Mayor_hijo', 'Localidad', 'Padre_Hijo', 'DNITIT_HIJO')
            self.tree.column('#0', width=0, stretch=NO)
            self.tree.column('DNI', anchor=CENTER)
            self.tree.column('Nombre', anchor=CENTER)
            self.tree.column('Apellido', anchor=CENTER)
            self.tree.column('CUIL/CUIT', anchor=CENTER)
            self.tree.column('Fecha_de_Nacimiento', anchor=CENTER)
            self.tree.column('Edad', anchor=CENTER, width=80)
            self.tree.column('Mayor_hijo', anchor=CENTER)
            self.tree.column('Localidad', anchor=CENTER)
            self.tree.column('Padre_Hijo', anchor=CENTER)
            self.tree.column('DNITIT_HIJO', anchor=CENTER)

            self.tree.heading('DNI', text='DNI', anchor=CENTER)
            self.tree.heading('Nombre', text='Nombre/s', anchor=CENTER)
            self.tree.heading('Apellido', text='Apellido/s', anchor=CENTER)
            self.tree.heading('CUIL/CUIT', text='CUIL/CUIT', anchor=CENTER)
            self.tree.heading('Fecha_de_Nacimiento',
                                text='Fecha de Nacimiento', anchor=CENTER)
            self.tree.heading('Edad', text='Edad', anchor=CENTER)
            self.tree.heading('Mayor_hijo', text='¿Es Mayor de 18?', anchor=CENTER)
            self.tree.heading('Localidad', text='Localidad', anchor=CENTER)
            self.tree.heading('Padre_Hijo', text='Es Hijo de:', anchor=CENTER)
            self.tree.heading('DNITIT_HIJO', text='DNI Titular', anchor=CENTER)
            self.tree.grid(row=2, column=0)

                # ---------------------------------------------------------------------#
            
        if quien == 'Cónyuge':
                # Grilla de datos cónyuge.
            self.tree['columns'] = ('DNI', 'Nombre', 'Apellido', 'CUIL/CUIT', 'Fecha_de_Nacimiento',
                                'Edad', 'Telefono', 'Mail', 'Localidad', 'Titular_DNITIT')
            self.tree.column('#0', width=0, stretch=NO)
            self.tree.column('DNI', anchor=CENTER)
            self.tree.column('Nombre', anchor=CENTER)
            self.tree.column('Apellido', anchor=CENTER)
            self.tree.column('CUIL/CUIT', anchor=CENTER)
            self.tree.column('Fecha_de_Nacimiento', anchor=CENTER)
            self.tree.column('Edad', anchor=CENTER, width=80)
            self.tree.column('Telefono', anchor=CENTER)
            self.tree.column('Mail', anchor=CENTER)
            self.tree.column('Localidad', anchor=CENTER)
            self.tree.column('Titular_DNITIT', anchor=CENTER)

            self.tree.heading('DNI', text='DNI', anchor=CENTER)
            self.tree.heading('Nombre', text='Nombre/s', anchor=CENTER)
            self.tree.heading('Apellido', text='Apellido/s', anchor=CENTER)
            self.tree.heading('CUIL/CUIT', text='CUIL/CUIT', anchor=CENTER)
            self.tree.heading('Fecha_de_Nacimiento',
                            text='Fecha de Nacimiento', anchor=CENTER)
            self.tree.heading('Edad', text='Edad', anchor=CENTER)
            self.tree.heading('Telefono', text='Teléfono', anchor=CENTER)
            self.tree.heading('Mail', text='Mail', anchor=CENTER)
            self.tree.heading('Localidad', text='Localidad', anchor=CENTER)
            self.tree.heading('Titular_DNITIT', text='DNI del Titular', anchor=CENTER)
            self.tree.grid(row=2, column=0)
                # ---------------------------------------------------------------------#

        if quien == 'Titular':
                # Grilla de datos Titular.
            self.tree['columns'] = ('DNI', 'Nombre', 'Apellido', 'CUIL/CUIT',
                                'Fecha_de_Nacimiento', 'Edad', 'Telefono', 'Mail', 'Localidad','NOTTIT')
            self.tree.column('#0', width=0, stretch=NO)
            self.tree.column('DNI', anchor=CENTER)
            self.tree.column('Nombre', anchor=CENTER)
            self.tree.column('Apellido', anchor=CENTER)
            self.tree.column('CUIL/CUIT', anchor=CENTER)
            self.tree.column('Fecha_de_Nacimiento', anchor=CENTER)
            self.tree.column('Edad', anchor=CENTER, width=80)
            self.tree.column('Telefono', anchor=CENTER)
            self.tree.column('Mail', anchor=CENTER)
            self.tree.column('Localidad', anchor=CENTER)
            self.tree.column('NOTTIT', anchor=CENTER)

            self.tree.heading('DNI', text='DNI', anchor=CENTER)
            self.tree.heading('Nombre', text='Nombre/s', anchor=CENTER)
            self.tree.heading('Apellido', text='Apellido/s', anchor=CENTER)
            self.tree.heading('CUIL/CUIT', text='CUIL/CUIT', anchor=CENTER)
            self.tree.heading('Fecha_de_Nacimiento',
                            text='Fecha de Nacimiento', anchor=CENTER)
            self.tree.heading('Edad', text='Edad', anchor=CENTER)
            self.tree.heading('Telefono', text='Teléfono', anchor=CENTER)
            self.tree.heading('Mail', text='Mail', anchor=CENTER)
            self.tree.heading('Localidad', text='Localidad', anchor=CENTER)
            self.tree.heading('NOTTIT', text='Nota Cliente', anchor=CENTER)
            self.tree.grid(row=2, column=0)
            # ---------------------------------------------------------------------#

            # Frame, Label, Entry y Button de DNI
        x = ttk.LabelFrame(self.top, text=f'Buscar {quien}',
                            padding=5, borderwidth=3, relief="ridge")
        x.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
        if quien == 'Hijo/s':
            # verifica si es Hijo o Cónyuge para agregar el button de buscar por titular al Hijo.
            ttk.Label(x, text='DNI TITULAR:', font=('Time New Roman', 14), borderwidth=3,
                                    relief="groove", anchor=W, pad=2).grid(row=0, column=3, sticky="nsew", pady=8, padx=10)
            self.dni_t = ttk.Entry(x, width=40, font=(16))
            self.dni_t.grid(row=0, column=4, pady=8, padx=10)
            self.validar_Enreys_Solo_Numeros(self.dni_t)
                
                # cambio de referencia para hacer la busqueda, en vez de "quien" se pone "F"
            F = 'DNITIT_HIJO'
            btn_buscar_dni_t = ttk.Button(
                    x, text='Buscar', bootstyle='info-outline', command=lambda: buscar(F))
            btn_buscar_dni_t.grid(row=0, column=5, sticky='ew')
                
            ttk.Label(x, text='DNI:', font=('Time New Roman', 14),
                                borderwidth=3, relief="groove", anchor=W).grid(row=0, column=0, sticky="nsew", pady=8)
            self.dni = ttk.Entry(x, width=40, font=(16))
            self.dni.grid(row=0, column=1, pady=8, padx=10)
            self.validar_Enreys_Solo_Numeros(self.dni)
                
            btn_buscar_dni = ttk.Button(
                    x, text='Buscar', bootstyle='info-outline', command=lambda: buscar(quien))
            btn_buscar_dni.grid(row=0, column=2, sticky='ew')

        if quien == 'Titular':
            ttk.Label(x, text='DNI:', font=('Time New Roman', 14),
                                borderwidth=3, relief="groove", anchor=W).grid(row=0, column=0, sticky="nsew", pady=8)
            self.dni = ttk.Entry(x, width=40, font=(16))
            self.dni.grid(row=0, column=1, pady=8, padx=10)
            self.validar_Enreys_Solo_Numeros(self.dni)

            btn_buscar_dni = ttk.Button(
                    x, text='Buscar', bootstyle='info-outline', command=lambda: buscar(quien))
            btn_buscar_dni.grid(row=0, column=2, sticky='ew')

        if quien == 'Cónyuge':
                # verifica si es Hijo o Cónyuge para agregar el button de buscar por titular al Cónyuge.
            ttk.Label(x, text='DNI TITULAR:', font=('Time New Roman', 14),borderwidth=3,
                                    relief="groove", anchor=W, pad=2).grid(row=0, column=3, sticky="nsew", pady=8, padx=10)
            self.dni_t = ttk.Entry(x, width=40, font=(16))
            self.dni_t.grid(row=0, column=4, pady=8, padx=10)
            self.validar_Enreys_Solo_Numeros(self.dni_t)
                
            # cambio de referencia para hacer la busqueda, en vez de "quien" se pone "F"
            F = 'Titular_DNITIT'
            btn_buscar_dni_t = ttk.Button(
                    x, text='Buscar', bootstyle='info-outline', command=lambda: buscar(F))
            btn_buscar_dni_t.grid(row=0, column=5, sticky='ew')
                
            ttk.Label(x, text='DNI:', font=('Time New Roman', 14),
                                borderwidth=3, relief="groove", anchor=W).grid(row=0, column=0, sticky="nsew", pady=8)
            self.dni = ttk.Entry(x, width=40, font=(16))
            self.dni.grid(row=0, column=1, pady=8, padx=10)
            self.validar_Enreys_Solo_Numeros(self.dni)
                
            btn_buscar_dni = ttk.Button(
                    x, text='Buscar', bootstyle='info-outline', command=lambda: buscar(quien))
            btn_buscar_dni.grid(row=0, column=2, sticky='ew')
        # ---------------------------------------------------------------------#






if __name__ == '__main__':
    # concepción DB
    conn = sqlite3.connect('prueba.db')
    c = conn.cursor()
    #   Creando base de datos.
    #   TABLA Titular
    c.execute("""
        CREATE TABLE IF NOT EXISTS Titular (
            DNITIT INTEGER NOT NULL,
            NOMTIT VARCHAR(150) NOT NULL,
            APETIT VARCHAR(150) NOT NULL,
            CUIL_CUIT_TIT INTEGER NOT NULL,
            FNATIT DATE NOT NULL,
            EDATIT INTEGER NOT NULL,
            TELTIT INTEGER NOT NULL,
            MAILTIT VARCHAR(100) NOT NULL,
            LOCTIT VARCHAR(500) NOT NULL,
            FCHTIT TIMESTAMP NOT NULL,
            NOTTIT VARCHAR(400),
            PRIMARY KEY (DNITIT));
    """)
    #   TABLA Conyuge
    c.execute("""
        CREATE TABLE IF NOT EXISTS Conyuge(
            DNICON INTEGER NOT NULL,
            NOMCON VARCHAR(150) NOT NULL,
            APECON VARCHAR(150) NOT NULL,
            CUIL_CUIT_CON INTEGERNOT NULL,
            FNACON DATE NOT NULL,
            EDACON INTEGER NOT NULL,
            TELCON INTEGER NOT NULL,
            MAILCON VARCHAR(100) NOT NULL,
            LOCCON VARCHAR(500) NOT NULL,
            FCHCON TIMESTAMP NOT NULL,
            Titular_DNITIT INTEGER NOT NULL,
            PRIMARY KEY (DNICON)
            FOREIGN KEY (Titular_DNITIT) REFERENCES Titular(DNITIT));
    """)
    #   TABLA Hijo
    c.execute("""
        CREATE TABLE IF NOT EXISTS Hijo(
            DNIHIJ INTEGER NOT NULL,
            NOMHIJ VARCHAR(150) NOT NULL,
            APEHIJ VARCHAR(150) NOT NULL,
            CUIL_CUIT_HIJ INT NOT NULL,
            FNAHIJ DATE NOT NULL,
            EDAHIJ INTEGER NOT NULL,
            MAYORHIJ VARCHAR(4) NOT NULL,
            LOCHIJ VARCHAR(500) NOT NULL,
            PDSHIJ VARCHAR(50),
            FCHHIJ TIMESTAMP NOT NULL,
            DNITIT_HIJO INTEGER NOT NULL,
            PRIMARY KEY (DNIHIJ),
            FOREIGN KEY (DNITIT_HIJO) REFERENCES Titular(DNITIT));
    """)

    #   TABLA Cotizacion
    c.execute("""
        CREATE TABLE IF NOT EXISTS Cotizacion (
            IDCOT  INTEGER PRIMARY KEY AUTOINCREMENT,
            TIPO_COT VARCHAR(50),
            TRES_POR_APORTE INTEGER NULL,
            SUELDO_BRUTO INTEGER NULL,
            FCH_ING_LAB DATE NULL,
            CATEGORIA VARCHAR(150) NOT NULL,
            PER_APORTA INTEGER NULL,
            COB_ACTUAL VARCHAR(150),
            PREPAGA CHARACTER(2),
            PLAN VARCHAR(150),
            MOTIVO_CAMBIO VARCHAR(700) NULL,
            DAT_REF VARCHAR(700) NULL,
            DNITIT_COT INTEGER NOT NULL,
            FOREIGN KEY (DNITIT_COT) REFERENCES Titular(DNITIT));
    """)
    #   TABLA Cobertura_Titular
    c.execute(""" 
        CREATE TABLE IF NOT EXISTS Cobertura_Titular (
            ID_COBER INTEGER PRIMARY KEY AUTOINCREMENT,
            COBERTURA VARCHAR(45), 
            PLAN_OS VARCHAR(100) ,
            COB_DNITIT INTEGER NOT NULL,
            FOREIGN KEY (COB_DNITIT) REFERENCES Titular(DNITIT));
    """)

    #   TABLA Alta_SanCor_Salud
    c.execute("""
        CREATE TABLE IF NOT EXISTS Alta_SanCor_Salud (
            ID_ALTA INTEGER PRIMARY KEY AUTOINCREMENT,
            PLAN_ELEGIDO VARCHAR(10) NOT NULL,
            DATBANC_TITULAR VARCHAR(10) NOT NULL,
            ALTA_DNITIT INTEGER NOT NULL,
            FOREIGN KEY (ALTA_DNITIT) REFERENCES Titular(DNITIT));
    """)

    # TABLA Cobertura_Hijos
    c.execute(""" 
        CREATE TABLE IF NOT EXISTS Cobertura_Hijos (
            ID_COBER INTEGER PRIMARY KEY AUTOINCREMENT,
            COBERTURA VARCHAR(45) NULL,
            PLAN_OS VARCHAR(100) NULL,
            COB_DNIHIJ INTEGER NOT NULL,
            FOREIGN KEY (COB_DNIHIJ) REFERENCES Hijo(DNIHIJ));
    """)

    #   TABLA Cobertura_Conyuge
    c.execute("""
        CREATE TABLE IF NOT EXISTS Cobertura_Conyuge (
            ID_COBER INTEGER PRIMARY KEY AUTOINCREMENT,
            COBERTURA VARCHAR(45) NULL,
            PLAN_OS VARCHAR(100) NULL,
            COB_DNICON INTEGER NOT NULL,
            FOREIGN KEY (COB_DNICON) REFERENCES Conyuge(DNICON));
    """)

    #   TABLA Medio_pago
    c.execute("""
        CREATE TABLE IF NOT EXISTS Medio_pago (
            ID_MEDIO_PAGO INTEGER PRIMARY KEY AUTOINCREMENT,
            DOMICILIO VARCHAR(500) NOT NULL,
            CIUDAD VARCHAR(500) NOT NULL,
            CODPOSTAL INTEGER NOT NULL,
            TARJ_CRED VARCHAR(100),
            BANC_TARJ VARCHAR(150),
            NRO_TARJ INTEGER NULL,
            VTO_TARJ VARCHAR(45) NULL,
            CBU_NUM INTEGER NULL,
            CBU_ALI VARCHAR(200) NULL,
            BANC_CBU VARCHAR(150) NULL,
            TIPO_CUENT VARCHAR(25),
            MED_ID_ALTA_SANCORD INTEGER NOT NULL,
            FOREIGN KEY (MED_ID_ALTA_SANCORD) REFERENCES Alta_SanCor_Salud(ID_ALTA));
    """)

    #   TABLA Datos_Empleador
    c.execute("""
        CREATE TABLE IF NOT EXISTS Datos_Empleador (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMEMP VARCHAR(500) NOT NULL,
            CUIT INTEGER NOT NULL,
            DIRE VARCHAR(500) NOT NULL,
            RRHHTEL INTEGER NOT NULL,
            DEMP_ID_ALTA_SANCORD INTEGER NOT NULL,
            FOREIGN KEY (DEMP_ID_ALTA_SANCORD) REFERENCES Alta_SanCor_Salud(ID_ALTA));
    """)

    #   TABLA Titular_Datos_Bancarios
    c.execute("""
        CREATE TABLE IF NOT EXISTS Titular_Datos_Bancarios (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DNI INTEGER NOT NULL,
            APELLIDO VARCHAR(150) NOT NULL,
            NOMBRE VARCHAR(150) NOT NULL,
            FNACIM DATE NOT NULL,
            Medio_PAGO_ID INTEGER NOT NULL,
            FOREIGN KEY (Medio_PAGO_ID) REFERENCES Medio_pago(ID_MEDIO_PAGO));
    """)

    #   TABLA Beneficiario_Seg_Vida
    c.execute("""
        CREATE TABLE IF NOT EXISTS Beneficiario_Seg_Vida (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DNI INTEGER NOT NULL,
            APELLIDO VARCHAR(150) NOT NULL,
            NOMBRE VARCHAR(150) NOT NULL,
            FNABENEF DATE NOT NULL,
            Alta_Salud_ID INTEGER NOT NULL,
            FOREIGN KEY (Alta_Salud_ID) REFERENCES Alta_SanCor_Salud(ID_ALTA));
    """)

    #   TABLA Declaracion_Salud_T
    c.execute("""
        CREATE TABLE IF NOT EXISTS Declaracion_Salud_T (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DISCAPACIDAD VARCHAR(500) NOT NULL,
            DATOENF VARCHAR(500) NOT NULL,
            PESO INTEGER NOT NULL,
            ALTURA INTEGER NOT NULL,
            DECT_DNITIT INTEGER NOT NULL,
            FOREIGN KEY (DECT_DNITIT) REFERENCES Titular(DNITIT));
    """)

    #   TABLA Declaracion_Salud_H
    c.execute("""
        CREATE TABLE IF NOT EXISTS Declaracion_Salud_H (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DISCAPACIDAD VARCHAR(500) NULL,
            DATOENF VARCHAR(500) NULL,
            PESO INTEGER NULL,
            ALTURA INTEGER NULL,
            DECH_DNIHIJ INTEGER NOT NULL,
            FOREIGN KEY (DECH_DNIHIJ) REFERENCES Hijo(DNIHIJ));
    """)

    #   TABLA Declaracion_Salud_C
    c.execute("""
        CREATE TABLE IF NOT EXISTS Declaracion_Salud_C (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DISCAPACIDAD VARCHAR(500) NULL,
            DATOENF VARCHAR(500) NULL,
            PESO INTEGER NULL,
            ALTURA INTEGER NULL,
            DECC_DNICON INT NOT NULL,
            FOREIGN KEY (DECC_DNICON) REFERENCES Conyuge(DNICON));
    """)

    #   TABLA Gestion_OP_Cambio_AFIP_TIT
    c.execute("""
        CREATE TABLE IF NOT EXISTS Gestion_OP_Cambio_AFIP_TIT (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CONAFI VARCHAR(50) NOT NULL,
            Mail_CONFIRMACION VARCHAR(100) NOT NULL,
            CUIT INTEGER NOT NULL,
            GAFI_DNITIT INTEGER NOT NULL,
            FOREIGN KEY (GAFI_DNITIT) REFERENCES Titular(DNITIT));
    """)

    #   TABLA Gestion_OP_Cambio_AFIP_CONY
    c.execute("""
        CREATE TABLE IF NOT EXISTS Gestion_OP_Cambio_AFIP_CONY (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CONTRASENIA VARCHAR(50) NOT NULL,
        MAIL_CONFIRMACION VARCHAR(100) NOT NULL,
        CUIT INT NOT NULL,
        GAFI_DNICON INT NOT NULL,
        FOREIGN KEY (GAFI_DNICON) REFERENCES Conyuge(DNICON));
    """)

    #   TABLA Datos_OS_Cambio
    c.execute("""
        CREATE TABLE IF NOT EXISTS Datos_OS_Cambio (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            OBRA_SOS_ORIG VARCHAR(100) NOT NULL,
            NROCERTIF INTEGER NOT NULL,
            OBRA_SOS_DES VARCHAR(100) NOT NULL,
            DOSC_DNITIT INTEGER NOT NULL,
            FOREIGN KEY (DOSC_DNITIT) REFERENCES Titular(DNITIT));
    """)

    #   TABLA Datos_OS_Cambio_CONY
    c.execute("""
        CREATE TABLE IF NOT EXISTS Datos_OS_Cambio_CONY (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            OBRA_SOS_ORIG VARCHAR(100) NOT NULL,
            NROCERTIF INTEGER NOT NULL,
            OBRA_SOS_DES VARCHAR(100) NOT NULL,
            DOSC_DNICON INTEGER NOT NULL,
            FOREIGN KEY (DOSC_DNICON) REFERENCES Conyuge(DNICON));
    """)

    #   TABLA Llamados_Ventas
    c.execute("""
        CREATE TABLE IF NOT EXISTS Llamados_Ventas (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            RESULT_LLAMADO VARCHAR(400),
            VENTA VARCHAR(4) NOT NULL,
            FECHA_VENTA TIMESTAMP NOT NULL,
            LVENT_DNITIT INTEGER NOT NULL,
            FOREIGN KEY (LVENT_DNITIT) REFERENCES Titular(DNITIT));
    """)
    
    root = ttk.Window(themename='solar')
    application = App(root,c,conn)
    root.mainloop()
        