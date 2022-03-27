from typing_extensions import Concatenate
from .conexion_db import ConexionDB as DB
from tkinter import messagebox
def crear_trablas():
    conexion=DB()
    sql='''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(50),
        duracion VARCHAR(50),
        genero VARCHAR(50),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        title='Crear Registro'
        mensaje='Se creo la tabla en la base de datos'
        messagebox.showinfo(title,mensaje)

    except:
        title='Crear Registro'
        mensaje='La tabla ya esta creada'
        messagebox.showwarning(title,mensaje)

def borrar_tabla():
    conexion=DB()

    sql='DROP TABLE peliculas'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        title='Borrar Registro'
        mensaje='La tabla de la base de datos se borro con exito'
        messagebox.showinfo(title,mensaje)
    except:
        title='Borrar Registro'
        mensaje='No hay tabla para borrar'
        messagebox.showerror(title,mensaje)

class Pelicula:
    def __init__(self,nombre,duracion,genero):
        self.id_pelicula=None
        self.nombre=nombre
        self.duracion=duracion
        self.genero=genero

    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'

def guardar(pelicula):
    conexion=DB()

    sql=f"""INSERT INTO peliculas(nombre,duracion,genero) VALUES('{pelicula.nombre}','{pelicula.duracion}','{pelicula.genero}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        title='Conexion al Registro'
        mensaje='La tabla peliculas no esta creada'
        messagebox.showerror(title,mensaje)

def listar():
    conexion=DB()

    lista_peliculas=[]
    sql='SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas=conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        title='Conexion al Registro'
        mensaje='Crea la tabla en la base de datos'
        messagebox.showerror(title,mensaje)
    return lista_peliculas

def editar(pelicula,id_pelicula):
    conexion=DB()
    sql=f"""UPDATE peliculas
    SET nombre ='{pelicula.nombre}',duracion='{pelicula.duracion}',genero='{pelicula.genero}'
    WHERE id_pelicula='{id_pelicula}'"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        
    except:
        title='Edicion de datos'
        mensaje='No se pudo editar correctamente'
        messagebox.showerror(title,mensaje)

def eliminar(id_pelicula):
    conexion=DB()

    sql=f'DELETE FROM peliculas WHERE id_pelicula={id_pelicula}'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        
    except:
        title='Eliminar datos'
        mensaje='No se pudo eliminar el registro'
        messagebox.showerror(title,mensaje)




