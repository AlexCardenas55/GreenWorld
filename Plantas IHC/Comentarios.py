from tkinter import *
import sqlite3


conn=sqlite3.connect('address_book.db')

c = conn.cursor()


#------------------TABLA----------


#c.execute("""CREATE TABLE comentarios(
#		planta text, 
#		comentario text
#				)""")
	





#---------FUNCION DE AGREGAR----------

def agregar():
	conn=sqlite3.connect('address_book.db')
	c = conn.cursor()
	c.execute("INSERT INTO comentarios VALUES(:textoPlanta, :textoComentario)",
		{
			'textoPlanta':textoPlanta.get(),
			'textoComentario': textoComentario.get(1.0, END)
		}



		)
	conn.commit()
	conn.close()
		


	#----------AGREGAR A LA TABLA---------


	textoPlanta.delete(0,END)
	textoComentario.delete(1.0,END)


def query():
	conn=sqlite3.connect('address_book.db')
	c = conn.cursor()
	c.execute("SELECT *  FROM comentarios")
	records=c.fetchall()
	
	print_records=''


	

	for record in records:
		print_records+= str(record) + '\n'
	query_label=Label(miFrame, text=print_records.strip("\n"),bg="#e2f3d1")
	query_label.grid(row=4, column=0, columnspan=2)




	conn.commit()
	conn.close()

conn.commit()

conn.close()

def Comentarios():
	global miFrame
	global textoPlanta
	global textoComentario

	root=Tk()
	miFrame=Frame(root)
	miFrame.pack()
	root.title("Comentarios")
	root.iconbitmap("girasol3.ico")
	miFrame.config(bg="#e2f3d1")
	labelTitulo=Label(miFrame, text="Comentarios", font=("Comic Sans Ms", 15),bg="#e2f3d1")
	labelTitulo.grid(row=0, column=0, pady=10)
	labelPlanta=Label(miFrame, text="Planta: ",bg="#e2f3d1")
	labelPlanta.grid(row=1, column=0, padx=5)
	textoPlanta=Entry(miFrame, width=20,bg="#e2f3d1")
	textoPlanta.grid(row=1, column=1)
	labelComentario=Label(miFrame, text="Agregar un Comentario",bg="#e2f3d1")
	labelComentario.grid(row=2, column=0, padx=5)
	textoComentario=Text(miFrame, width=16, height=5,bg="#e2f3d1")
	textoComentario.grid(row=2, column=1, padx=10, pady=10)
	scrollVert=Scrollbar(miFrame, command=textoComentario.yview,bg="#e2f3d1")
	scrollVert.grid(row=2, column=2, sticky="nswe")
	textoComentario.config(yscrollcommand=scrollVert.set)
	botonAgregar=Button(miFrame, text="Agregar", command=agregar,bg="#e2f3d1")
	botonAgregar.grid(row=3, column=0, pady=10)
	botonMisComentarios=Button(miFrame, text="Mis Comentarios",command=query,bg="#e2f3d1")
	botonMisComentarios.grid(row=3, column=1, padx=20)





	root.mainloop()





