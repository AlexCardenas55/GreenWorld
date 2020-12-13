from tkinter import *
from tkinter import messagebox





def Manzanilla():
    rootManzanilla=Toplevel()
    frameManzanilla=Frame(rootManzanilla)
    frameManzanilla.pack()
    rootManzanilla.title("Actividades para Mantener una Manzanilla")
    rootManzanilla.iconbitmap("girasol3.ico")
    Tarea1=Label(frameManzanilla, text="1.-Es una planta que podemos ubicar en el exterior como por ejemplo en terrazas y patios perfectamente en zonas con climas templados.")
    Tarea1.grid(row=0, column=0, sticky="w")    
    Tarea2=Label(frameManzanilla, text="2.-No es necesario que el suelo sea rico en material orgánico, abonarlo una vez al año con humus de lombriz será suficiente para que la Manzanilla prospere bien.")
    Tarea2.grid(row=1, column=0, sticky="w")
    Tarea3=Label(frameManzanilla, text="3.-Prefiere estar expuesta al sol pero también crece saludables ubicada en una semi sombra.")
    Tarea3.grid(row=2, column=0, sticky="w")
    Tarea4=Label(frameManzanilla, text="4.-El momento ideal para cosechar Manzanilla es cuando inicie el proceso de floración.")
    Tarea4.grid(row=3, column=0, sticky="w")
    Tarea5=Label(frameManzanilla, text="5.-Al pasar dos semanas, las semillas habrán germinado, elige el brote más fuerte y elimina los más débiles.")
    Tarea5.grid(row=4, column=0, sticky="w")
    frameHecho=Frame(rootManzanilla)
    frameHecho.pack()
    BotonHechoManzanilla=Button(frameHecho, text="Hecho", command=rootManzanilla.destroy)
    BotonHechoManzanilla.grid(row=0, column=0)
    rootManzanilla.mainloop()



def AloeVera():
    root3=Toplevel()
    root3.title("Actividades para Mantener un Aloe Vera")
    frame4=Frame(root3)
    frame4.pack()
    root3.iconbitmap("logo.ico")


    Tarea1=Label(frame4, text="1.-Tu planta de aloe vera debe crecer en tierra que drene bien el agua. Si no es el caso debes trasplantarla")
    Tarea1.grid(row=0, column=0, sticky="w")
    Tarea2=Label(frame4, text="2.-Como este tipo de tierra suele ser bastante pobre, añade abono natural o compost no absorbente")
    Tarea2.grid(row=1, column=0, sticky="w")
    Tarea3=Label(frame4, text="3.-Sitúa tu planta de aloe vera en un lugar en que reciba el mayor número de horas de Sol posible. Así, procuramos la evaporación del agua")
    Tarea3.grid(row=2, column=0, sticky="w")
    Tarea4=Label(frame4, text="4.-Si tienes la planta en el exterior, cuida que no reciba agua de lluvia si no le toca ser regada pues sus raíces se pudren muy fácilmente")
    Tarea4.grid(row=3, column=0, sticky="w")
    Tarea5=Label(frame4, text="5.-Una vez al año (preferiblemente en primavera) abona la planta con humus de lombriz, estiércol de caballo, etc")
    Tarea5.grid(row=4, column=0, sticky="w")
    frame5=Frame(root3)
    frame5.pack()
    botonMenu=Button(frame5, text="Hecho", command=root3.destroy)
    botonMenu.grid(row=0, column=0)

    root3.mainloop()
def girasol():
    root2=Toplevel()
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



def Menu_Mis_Plantas():
    root=Toplevel()
    root.title("Mis Plantas")
    label=Label(root)
    frame=Frame(root)
    frame.config(width="500", height="500")
    frame.pack()
    root.iconbitmap("girasol3.ico")
    if var1.get()==1:
        ImagenGirasol=PhotoImage(file="misImagenes.png")
        labelGirasol=Label(frame,  image=ImagenGirasol)
        labelGirasol.grid(row=0, column=0, padx=10, pady=10)
        botonGirasol=Button(frame, text="Girasol", command=girasol)
        botonGirasol.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
    if var2.get()==1:
        ImagenAloe=PhotoImage(file="Aloe-Vera.png")
        LabelAloe=Label(frame, image=ImagenAloe)
        LabelAloe.grid(row=1,column=0, padx=10, pady=10)
        BotonAloe=Button(frame, text="Aloe Vera", command=AloeVera)
        BotonAloe.grid(row=1, column=1, padx=10, pady=10, sticky="nswe")
    if var3.get()==1:
        ImagenManzanilla=PhotoImage(file="manzanilla.png")
        LabelManzanilla=Label(frame, image=ImagenManzanilla)
        LabelManzanilla.grid(row=2, column=0, padx=10, pady=10)
        botonManzanilla=Button(frame, text="Manzanilla", command=Manzanilla)
        botonManzanilla.grid(row=2, column=1, padx=10, pady=1, sticky="nswe")
    #-----------------------Frame para Volver a Menu--------
    frame2=Frame(root)
    frame2.pack()
    BotonMenu=Button(frame2, text="Menu", command=root.destroy)
    BotonMenu.grid(padx=10, pady=10)

    root.mainloop()


rootprueba=Tk()

frame10=Frame(rootprueba)
frame10.pack()
miboton=Button(frame10, text="prueba", command=rootprueba.destroy)
miboton.grid(row=0,column=0)
rootprueba.mainloop()




raiz=Tk()
global var1
var1=IntVar()
global var2
var2=IntVar()
global var3
var3=IntVar()
miFrame=Frame(raiz) 
miFrame.pack()
raiz.title("Agregar Planta")
checkVar1=IntVar()
checkVar2=IntVar()
Titulo=Label(miFrame, text="Favor de seleccionar sus plantas")
Titulo.grid(row=0, column=0)
C1=Checkbutton(miFrame, text="Girasol",variable=var1, onvalue=1, offvalue=0)
C1.grid(row=1, column=0)
C2=Checkbutton(miFrame, text="Aloe Vera", variable=var2, onvalue=1, offvalue=0)
C2.grid(row=2, column=0)
C3=Checkbutton(miFrame, text="Manzanilla", variable=var3,onvalue=1, offvalue=0)
C3.grid(row=3, column=0)
BotonMenu=Button(miFrame, text="Menu", command=Menu_Mis_Plantas)
BotonMenu.grid(row=4, column=0)



raiz.mainloop()



