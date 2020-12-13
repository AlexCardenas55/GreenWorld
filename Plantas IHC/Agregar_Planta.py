from tkinter import *
from tkinter import messagebox
import os
import sqlite3



#-----------------funciones---------------

def Menu_Agregar_Plantas():
	root2=Tk()
	def conexionBBDD():

		miConexion=sqlite3.connect("Plantas")

		miCursor=miConexion.cursor()

		try:

			miCursor.execute('''
				CREATE TABLE MISPLANTAS (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				NOMBRE_PLANTA VARCHAR(50),
				TIEMPO_VIDA VARCHAR(50),
				COMENTARIOS VARCHAR(100))
				''')
			messagebox.showinfo("BBDD", "BBDD creada con éxito")

		except:
			messagebox.showwarning("Atencion", "La BBDD ya existe")


	def crear():

		miConexion=sqlite3.connect("Plantas")
		miCursor=miConexion.cursor()

		datos=miNombre.get(), miTiempo_Vida.get(),textoComentario.get(1.0, END)

		"""miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, '"+miNombre.get()+
			"','"+miPass.get()+
			"','"+miApellido.get()+
			"','"+miDireccion.get()+
			"','"+textoComentario.get("1.0", END)+"')")"""

		miCursor.execute("INSERT INTO MISPLANTAS VALUES(NULL,?,?,?)",(datos))

		miConexion.commit()
		messagebox.showinfo("BBDD", "Planta insertada con exito")

	def leer():
		miConexion=sqlite3.connect("Plantas")
		miCursor=miConexion.cursor()

		miCursor.execute("SELECT * FROM MISPLANTAS WHERE ID="+miId.get())
		
		elUsuario=miCursor.fetchall()
		for usuario in elUsuario:
			miId.set(usuario[0])
			miNombre.set(usuario[1])
			miTiempo_Vida.set(usuario[2])
			textoComentario.insert(1.0, usuario[3])

		miConexion.commit()

	def SalirAplicacion():

		valor=messagebox.askquestion("Salir", "Deseas Salir de la Aplicacion?")
		if valor=="yes":
			root2.destroy()

	def actualizar():
		miConexion=sqlite3.connect("Plantas")
		miCursor=miConexion.cursor()

		datos=miNombre.get(), miTiempo_Vida.get(), textoComentario.get(1.0, END)

		"""miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='"+miNombre.get()+
			"', PASSWORD='"+miPass.get() + 
			"' ,APELLIDO='"+miApellido.get() + 
			"' ,DIRECCION='"+miDireccion.get() + 
			"', COMENTARIOS='"+textoComentario.get("1.0", END) +
			"' WHERE ID=" +miId.get())""" 

		miCursor.execute("UPDATE MISPLANTAS SET NOMBRE_PLANTA=?, TIEMPO_VIDA=?, COMENTARIOS=? WHERE ID="+miId.get(),(datos))

		miConexion.commit()
		messagebox.showinfo("BBDD", "Planta actualizada con éxito")


	def eliminar():
		miConexion=sqlite3.connect("Plantas")

		miCursor=miConexion.cursor()

		miCursor.execute("DELETE FROM MISPLANTAS WHERE ID="+miId.get())

		miConexion.commit()

		messagebox.showinfo("BBDD", "Planta borrada con éxito")

	#------------Menu------------------
	root2.title("Ingresar Planta")
	root2.iconbitmap("girasol3.ico")
	barraMenu=Menu(root2)
	root2.config(menu=barraMenu, width=300, height=300)

	archivoMenu=Menu(barraMenu, tearoff=0)
	archivoMenu.add_command(label="Conectar", command=conexionBBDD)
	archivoMenu.add_command(label="Salir", command=SalirAplicacion)
	barraMenu.add_cascade(label="BBDD", menu=archivoMenu)



	#------------------Los cuadros de texto----------------
	miId=StringVar()
	miNombre=StringVar()
	miTiempo_Vida=StringVar()


	miFrame=Frame(root2)
	miFrame.pack()

	cuadroID=Entry(miFrame, textvariable=miId)
	cuadroID.grid(row=0, column=1, padx=10, pady=10)

	cuadroNombre=Entry(miFrame, textvariable=miNombre)
	cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

	cuadroTiempo_Vida=Entry(miFrame, textvariable=miTiempo_Vida)
	cuadroTiempo_Vida.grid(row=2, column=1, padx=10, pady=10)

	textoComentario=Text(miFrame, width=16, height=5)
	textoComentario.grid(row=5, column=1, padx=10, pady=10)

	scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
	scrollVert.grid(row=5, column=2, sticky="nswe")
	textoComentario.config(yscrollcommand=scrollVert.set)

	#------------------Los Label----------------

	idLabel=Label(miFrame, text="id:")
	idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

	nombreLabel=Label(miFrame, text="Nombre:")
	nombreLabel.grid(row=1,column=0, sticky="e", padx=10, pady=10)

	tiempo_vidaLabel=Label(miFrame, text="Tiempo de Vida:")
	tiempo_vidaLabel.grid(row=2,column=0, sticky="e", padx=10, pady=10)

	comentariosLabel=Label(miFrame, text="Comentarios:")
	comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

	#------------------BOTONES----------------------

	miFrame2=Frame(root2)
	miFrame2.pack()
	botonCrear=Button(miFrame2, text="Crear", command=crear)
	botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

	botonActualizar=Button(miFrame2, text="Actualizar", command=actualizar)
	botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

	botonLeer=Button(miFrame2, text="Leer", command=leer)
	botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

	botonBorrar=Button(miFrame2, text="Eliminar", command=eliminar)
	botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


	root2.mainloop()

def Abrir_Agregar_Planta():
	Menu_Agregar_Plantas()


#CREAMOS VENTANA PRINCIPAL.






