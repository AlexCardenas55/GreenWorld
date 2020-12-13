from tkinter import *


#-----------------------TAREAS AL PRESIONAR EL BOTON---------
def girasol():
	root2=Tk()
	root2.title("Actividades para Mantener un Girasol")
	frame3=Frame(root2)
	frame3.pack()
	Tarea1=Label(frame3, text="1.-Utiliza jarrones de cristal o transparentes y llenarlos de agua a temperatura ambiente.")
	Tarea1.grid(row=0, column=1)
	Tarea2=Label(frame3, text="2.-Agregar Nutrientes para flores para alargar el tiempo de vida de los girasoles.")
	Tarea2.grid(row=1, column=1)
	Tarea3=Label(frame3, text="3.-Quitar las hojas sobrantes y evitar que tengan contacto con el agua del jarrón")
	Tarea3.grid(row=2, column=1)
	Tarea4=Label(frame3, text="4.-Cambiar el agua regularmente, porque lo girasoles necesitan bastante agua.")
	Tarea4.grid(row=3, column=1)
	Tarea5=Label(frame3, text="5.-Colocar el jarrón en un lugar con luz pero que no tenga contacto con la luz solar")
	Tarea5.grid(row=4, column=1)
	frame4=Frame(root2)
	frame4.pack()
	botonHecho=Button(frame4,text="Hecho", command=root2.destroy)
	botonHecho.grid()
	root2.mainloop()
#--------------INFORMACION DE INTERFAZ--------------
def Menu_Mis_Plantas():
	root=Tk()
	root.title("Mis Plantas")
	frame=Frame(root)
	frame.config(width="500", height="500")
	frame.pack()
	root.iconbitmap("girasol3.ico")
	ImagenGirasol=PhotoImage(file="misImagenes.png")
	labelGirasol=Label(frame,  image=ImagenGirasol)
	labelGirasol.grid(row=0, column=0, padx=10, pady=10)
	botonGirasol=Button(frame, text="Girasol", command=girasol)
	botonGirasol.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
	ImagenAloe=PhotoImage(file="Aloe-Vera.png")
	LabelAloe=Label(frame, image=ImagenAloe)
	LabelAloe.grid(row=1,column=0, padx=10, pady=10)
	BotonAloe=Button(frame, text="Aloe Vera")
	BotonAloe.grid(row=1, column=1, padx=10, pady=10, sticky="nswe")

	#-----------------------Frame para Volver a Menu--------
	frame2=Frame(root)
	frame2.pack()
	BotonMenu=Button(frame2, text="Menu")
	BotonMenu.grid(padx=10, pady=10)

	root.mainloop()

