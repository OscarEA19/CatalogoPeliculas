import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter.constants import INSERT, NONE
from tkinter.font import BOLD
from tkinter import ttk
from typing import Text
from typing_extensions import ParamSpec
from model.pelicula_dao import crear_trablas,borrar_tabla
from model.pelicula_dao import Pelicula,guardar,listar,editar,eliminar

def barra_menu(root):
    barra_menu=tk.Menu(root)
    root.config(menu=barra_menu, width=300,height=300)
    menu_inicio=tk.Menu(barra_menu)


    menu_inicio=tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Inicio',menu=menu_inicio)

    menu_inicio.add_command(label="Crear Registro en DB",command=crear_trablas)
    menu_inicio.add_command(label="Eliminar Registro en DB",command=borrar_tabla)
    menu_inicio.add_command(label="Salir ",command=root.destroy)
    
    menu_consulta=tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Consultas',menu=menu_consulta)
    menu_consulta.add_command(label='Habilita tu consulta con: 30$')

    menu_configuracion=tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Configuración',menu=menu_configuracion)
    menu_configuracion.add_command(label='Habilita tu configuración con: 30$')
    
    menu_ayuda=tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Ayuda',menu=menu_ayuda)
    menu_ayuda.add_command(label='Habilita tu ayuda con: 20$')
 
   
   


class Frame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.winfo_root=root
        self.pack()
        self.config(width=400, height=400,)
        self.campo_pelicula()
        self.desabilitar_campo()
        self.tabla_peliculas()
        self.id_pelicula=None

    def campo_pelicula(self):
        #label de cada campo

        self.label_nombre=tk.Label(self,text="Nombre: ")
        self.label_nombre.config(font=('Arial',12,BOLD))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.label_duracion=tk.Label(self,text="Duración: ")
        self.label_duracion.config(font=('Arial',12,BOLD))
        self.label_duracion.grid(row=1,column=0,padx=10,pady=10)

        self.label_genero=tk.Label(self,text="Genero: ")
        self.label_genero.config(font=('Arial',12,BOLD))
        self.label_genero.grid(row=2,column=0,padx=10,pady=10)

        #Entry de cada campo

        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial',12))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.mi_duracion=tk.StringVar()
        self.entry_duracion=tk.Entry(self,textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50,font=('Arial',12))
        self.entry_duracion.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.mi_genero=tk.StringVar()
        self.entry_genero=tk.Entry(self,textvariable=self.mi_genero)
        self.entry_genero.config(width=50,font=('Arial',12))
        self.entry_genero.grid(row=2,column=1,padx=10,pady=10,columnspan=2)

        #botones

        self.btn_nuevo=tk.Button(self,text="Nuevo",command=self.habilitar_campo)
        self.btn_nuevo.config(width=20,font=('Arial',12,'bold'),bg='#1CA203',fg='#E2FFFF',
        cursor='hand2',activebackground='#1C6D03')
        self.btn_nuevo.grid(row=3,column=0,padx=10,pady=10)
        
        self.btn_guardar=tk.Button(self,text="Guardar",command=self.guardar_datos)
        self.btn_guardar.config(width=20,font=('Arial',12,'bold'),bg='#1B15D4',fg='#E2FFFF',
        cursor='hand2',activebackground='#1B81FF')
        self.btn_guardar.grid(row=3,column=1,padx=10,pady=10)


        self.btn_cancelar=tk.Button(self,text="Cancelar",command=self.desabilitar_campo)
        self.btn_cancelar.config(width=20,font=('Arial',12,'bold'),bg='#DC4E41',fg='#E2FFFF',
        cursor='hand2',activebackground='#DC1C00')
        self.btn_cancelar.grid(row=3,column=2,padx=10,pady=10)

    def habilitar_campo(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')

        self.btn_guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')

    def desabilitar_campo(self):

        self.id_pelicula=None
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')

        self.btn_guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')

    def guardar_datos(self):
        pelicula=Pelicula(self.mi_nombre.get(),self.mi_duracion.get(),self.mi_genero.get())
        
        if self.id_pelicula==None:
            guardar(pelicula)
        else:
            editar(pelicula,self.id_pelicula)

        self.tabla_peliculas()
        #Desabilida campos
        self.desabilitar_campo()

    def tabla_peliculas(self):


        #Recuperar lista
        self.lista_peliculas=listar()
        self.lista_peliculas.reverse()
        self.tabla=ttk.Treeview(self,columns=('Nombre','Duración','Genero'))
        self.tabla.grid(row=4,column=0,columnspan=4,sticky='nse')

        #scrollbar para la tabla si exede 10 registros
        self.scroll=ttk.Scrollbar(self,orient='vertical',command=self.tabla.yview)
        self.scroll.grid(row=4,column=4,sticky='nse')
        self.tabla.config(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='NOMBRE')
        self.tabla.heading('#2',text='DURACION')
        self.tabla.heading('#3',text='GENERO')

        #iterar la lista de peliculas

        for p in self.lista_peliculas:
            self.tabla.insert('',0,text=p[0],values=(p[1],p[2],p[3]))

        #botones
        self.btn_editar=tk.Button(self,text="Editar",command=self.editar_datos)
        self.btn_editar.config(width=20,font=('Arial',12,'bold'),bg='#1CA203',fg='#E2FFFF',
        cursor='hand2',activebackground='#1C6D03')
        self.btn_editar.grid(row=5,column=0,padx=10,pady=10)

        self.btn_eliminar=tk.Button(self,text="Eliminar",command=self.eliminar_datos)
        self.btn_eliminar.config(width=20,font=('Arial',12,'bold'),bg='#DC4E41',fg='#E2FFFF',
        cursor='hand2',activebackground='#DC1C00')
        self.btn_eliminar.grid(row=5,column=2,padx=10,pady=10)

    def editar_datos(self):

        try:    
            self.id_pelicula=self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula=self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula=self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula=self.tabla.item(self.tabla.selection())['values'][2]

            self.habilitar_campo()

            self.entry_nombre.insert(0,self.nombre_pelicula)
            self.entry_duracion.insert(0,self.duracion_pelicula)
            self.entry_genero.insert(0,self.genero_pelicula)
        except:
            titulo='Edicion de datos'
            mensaje='No ha seleccionado ningun registro'
            messagebox.showerror(titulo,mensaje)

    def eliminar_datos(self):
        try:
            self.id_pelicula=self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_pelicula)
            self.tabla_peliculas()
            self.id_pelicula=None

        except:
            titulo='Eliminar un Registro'
            mensaje='No ha seleccionado ningun registro'
            messagebox.showerror(titulo,mensaje)






