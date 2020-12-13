from tkinter import *
from tkinter import messagebox
import os
from Datos import *
from Comentarios import *
import sys
from menuPlantas import *
if "Tkinter" not in sys.modules:
    from tkinter import *



#CREAMOS VENTANA PRINCIPAL.

def Menu_Mis_Comentarios():
    Comentarios()

def Menu_Datos_Curiosos():
    Principal()

def MenuGirasol():
    Girasol()

def MenuRosa():
    Rosa()

def MenuAloeVera():
    AloeVera()

def MenuHortensia():
    Hortensia()

def MenuManzanilla():
    Manzanilla()

def MenuNopal():
    Nopal()

def MenuTulipan():
    Tulipan()

def MenuDiente():
    Diente()
"""def Diente():
    rootDiente=Toplevel()
    frameDiente=Frame(rootDiente)
    frameDiente.pack()
    frameDiente.config(bg="#e2f3d1")
    rootDiente.title("Actividades para Mentener un Diente de Leon")
    rootDiente.iconbitmap("girasol3.ico")
    Tarea1=Label(frameDiente, text="1.-El diente de leon florece en primavera, sobre el mes de mayo", bg="#e2f3d1")
    Tarea1.grid(row=1, column=0, sticky="w")
    Tarea2=Label(frameDiente, text="2.- Lo mas optimo para su cuidado es colocarlo en pleno sol o incluso en semi sombre", bg="#e2f3d1")
    Tarea2.grid(row=2, column=0, sticky="w")
    Tarea3=Label(frameDiente, text="3.-Una de las principales ventajas es que soporta las heladas y el viento", bg="#e2f3d1")
    Tarea3.grid(row=3, column=0, sticky="w")
    Tarea4=Label(frameDiente, text="4.-Prefiere suelos humedos, profundos y ricos en materia organica como huertos", bg="#e2f3d1")
    Tarea4.grid(row=4, column=0, sticky="w")
    Tarea5=Label(frameDiente, text="5.-Sembrar directamente en una maceta, con tierra rica en compost, mantener con buen riego", bg="#e2f3d1")
    Tarea5.grid(row=5, column=0, sticky="w")
    BotonMenu=Button(frameDiente, text="Hecho", command=rootDiente.destroy, bg="#e2f3d1")
    BotonMenu.grid(row=6, column=0)
    rootDiente.mainloop()

def Manzanilla():
    rootManzanilla=Toplevel()
    frameManzanilla=Frame(rootManzanilla)
    frameManzanilla.pack()
    frameManzanilla.config(bg="#e2f3d1")
    rootManzanilla.title("Actividades para Mantener una Manzanilla")
    rootManzanilla.iconbitmap("girasol3.ico")
    Tarea1=Label(frameManzanilla, text="1.-Es una planta que podemos ubicar en el exterior como por ejemplo en terrazas y patios perfectamente en zonas con climas templados.", bg="#e2f3d1")
    Tarea1.grid(row=0, column=0, sticky="w")    
    Tarea2=Label(frameManzanilla, text="2.-No es necesario que el suelo sea rico en material orgánico, abonarlo una vez al año con humus de lombriz será suficiente para que la Manzanilla prospere bien.", bg="#e2f3d1")
    Tarea2.grid(row=1, column=0, sticky="w")
    Tarea3=Label(frameManzanilla, text="3.-Prefiere estar expuesta al sol pero también crece saludables ubicada en una semi sombra.", bg="#e2f3d1")
    Tarea3.grid(row=2, column=0, sticky="w")
    Tarea4=Label(frameManzanilla, text="4.-El momento ideal para cosechar Manzanilla es cuando inicie el proceso de floración.", bg="#e2f3d1")
    Tarea4.grid(row=3, column=0, sticky="w")
    Tarea5=Label(frameManzanilla, text="5.-Al pasar dos semanas, las semillas habrán germinado, elige el brote más fuerte y elimina los más débiles.", bg="#e2f3d1")
    Tarea5.grid(row=4, column=0, sticky="w")
    BotonHechoManzanilla=Button(frameManzanilla, text="Hecho", command=rootManzanilla.destroy, bg="#e2f3d1")
    BotonHechoManzanilla.grid(row=5, column=0)
    rootManzanilla.mainloop()



def AloeVera():
    root3=Toplevel()
    root3.title("Actividades para Mantener un Aloe Vera")
    frame4=Frame(root3)
    frame4.config( bg="#e2f3d1")
    frame4.pack()
    root3.iconbitmap("logo.ico")


    Tarea1=Label(frame4, text="1.-Tu planta de aloe vera debe crecer en tierra que drene bien el agua. Si no es el caso debes trasplantarla", bg="#e2f3d1")
    Tarea1.grid(row=0, column=0, sticky="w")
    Tarea2=Label(frame4, text="2.-Como este tipo de tierra suele ser bastante pobre, añade abono natural o compost no absorbente", bg="#e2f3d1")
    Tarea2.grid(row=1, column=0, sticky="w")
    Tarea3=Label(frame4, text="3.-Sitúa tu planta de aloe vera en un lugar en que reciba el mayor número de horas de Sol posible. Así, procuramos la evaporación del agua", bg="#e2f3d1")
    Tarea3.grid(row=2, column=0, sticky="w")
    Tarea4=Label(frame4, text="4.-Si tienes la planta en el exterior, cuida que no reciba agua de lluvia si no le toca ser regada pues sus raíces se pudren muy fácilmente", bg="#e2f3d1")
    Tarea4.grid(row=3, column=0, sticky="w")
    Tarea5=Label(frame4, text="5.-Una vez al año (preferiblemente en primavera) abona la planta con humus de lombriz, estiércol de caballo, etc", bg="#e2f3d1")
    Tarea5.grid(row=4, column=0, sticky="w")
    botonMenu=Button(frame4, text="Hecho", command=root3.destroy, bg="#e2f3d1")
    botonMenu.grid(row=5, column=0)

    root3.mainloop()
def girasol():
    root2=Toplevel()
    root2.title("Actividades para Mantener un Girasol")
    frame3=Frame(root2)
    frame3.pack()
    frame3.config( bg="#e2f3d1")
    Tarea1=Label(frame3, text="1.-Utiliza jarrones de cristal o transparentes y llenarlos de agua a temperatura ambiente.", bg="#e2f3d1")
    Tarea1.grid(row=0, column=1, sticky="w")
    Tarea2=Label(frame3, text="2.-Agregar Nutrientes para flores para alargar el tiempo de vida de los girasoles.", bg="#e2f3d1")
    Tarea2.grid(row=1, column=1, sticky="w")
    Tarea3=Label(frame3, text="3.-Quitar las hojas sobrantes y evitar que tengan contacto con el agua del jarrón", bg="#e2f3d1")
    Tarea3.grid(row=2, column=1, sticky="w")
    Tarea4=Label(frame3, text="4.-Cambiar el agua regularmente, porque lo girasoles necesitan bastante agua.", bg="#e2f3d1")
    Tarea4.grid(row=3, column=1, sticky="w")
    Tarea5=Label(frame3, text="5.-Colocar el jarrón en un lugar con luz pero que no tenga contacto con la luz solar", bg="#e2f3d1")
    Tarea5.grid(row=4, column=1, sticky="w")
    frame4=Frame(root2)
    botonHecho=Button(frame3,text="Hecho", command=root2.destroy, bg="#e2f3d1")
    botonHecho.grid(row=5, column=1)
    root2.mainloop()

def Rosas():
    rootRosas=Toplevel()
    frame=Frame(rootRosas)
    frame.pack()
    frame.config( bg="#e2f3d1")
    rootRosas.title("Como cuidar de tus Rosas")
    rootRosas.iconbitmap("girasol3.ico")
    Tarea1=Label(frame, text="1.-Lo recomendable es ubicarlas en sitios en los que reciban al menos 5 horas de sol durante el día.", bg="#e2f3d1")
    Tarea1.grid(row=0, column=1, sticky="w")
    Tarea2=Label(frame, text="2.-La maceta ideal para una rosa es de al menos 50 centímetros de diámetro y 60 centímetros de profundidad.", bg="#e2f3d1")
    Tarea2.grid(row=1, column=1, sticky="w")
    Tarea3=Label(frame, text="3.-lo ideal  es agregar suficiente agua para conservar la tierra húmeda y suelta, pero no tanta como para que se compacte y dificulte el drenaje.", bg="#e2f3d1")
    Tarea3.grid(row=2, column=1, sticky="w")
    Tarea4=Label(frame, text="4.-Es recomendable hacer la poda a finales del verano o del  invierno para aumentar la vitalidad en la siguiente floración.", bg="#e2f3d1")
    Tarea4.grid(row=3, column=1, sticky="w")
    Tarea5=Label(frame, text="5.-El día perfecto para trasplantar una rosa es un día nublado, en temporada de crecimiento inactivo para evitar dañar la planta lo menos posible.", bg="#e2f3d1")
    Tarea5.grid(row=4, column=1, sticky="w")
    botonHecho=Button(frame,text="Hecho", command=rootRosas.destroy, bg="#e2f3d1")
    botonHecho.grid(row=5, column=1,sticky="") 
    rootRosas.mainloop()

def Tulipan():
    rootTulipan=Toplevel()
    frame=Frame(rootTulipan)
    frame.pack()
    frame.config(bg="#e2f3d1")
    rootTulipan.title("Como cuidar de tus Tulipanes")
    rootTulipan.iconbitmap("girasol3.ico")
    Tarea1=Label(frame, text="1.-Debes regar el tulipán lo suficiente para que pueda ofrecer las preciosas flores, ésto vamos a hacerlo todos los días pero con cantidades pequeñas", bg="#e2f3d1")
    Tarea1.grid(row=0, column=1, sticky="w")
    Tarea2=Label(frame, text="2.-necesita bastante exposición de luz solar para poder crear correctamente la fotosíntesis", bg="#e2f3d1")
    Tarea2.grid(row=1, column=1, sticky="w")
    Tarea3=Label(frame, text="3.-La separación entre bulbos no debe ser inferior a 2 cm, ya que si no, no podrán crecer con normalidad y la floración será débil..", bg="#e2f3d1")
    Tarea3.grid(row=2, column=1, sticky="w")
    Tarea4=Label(frame, text="4.-Las condiciones ideales de temperatura, después de haber florecido, están entre los 13ºC y los 18ºC.", bg="#e2f3d1")
    Tarea4.grid(row=3, column=1, sticky="w")
    Tarea5=Label(frame, text="5.-Los tulipanes los debes plantar en otoño, de unas 6 a 8 semanas antes del invierno.", bg="#e2f3d1")
    Tarea5.grid(row=4, column=1, sticky="w")
    botonHecho=Button(frame,text="Hecho", command=rootTulipan.destroy, bg="#e2f3d1")
    botonHecho.grid(row=5, column=1,sticky="") 
    rootTulipan.mainloop()

def Hortensia():
    rootHortensias=Toplevel()
    frame=Frame(rootHortensias)
    frame.pack()
    frame.config(bg="#e2f3d1")
    rootHortensias.title("Como cuidar de tus Hortensias")
    rootHortensias.iconbitmap("girasol3.ico")
    Tarea1=Label(frame, text="1.-Para cultivar estas plantas hay que plantar en primavera u otoño. ", bg="#e2f3d1")
    Tarea1.grid(row=0, column=1, sticky="w")
    Tarea2=Label(frame, text="2.-Las hortensias les gusta el sol de la mañana o sol que viene del este, pero esto solo en zonas de clima suave si el clima es cálido tendrán que estar a sol indirecto.", bg="#e2f3d1")
    Tarea2.grid(row=1, column=1, sticky="w")
    Tarea3=Label(frame, text="3.-Las hortensias necesitan un suelos ricos, porosos húmedo y bien drenado para prosperar.", bg="#e2f3d1")
    Tarea3.grid(row=2, column=1, sticky="w")
    Tarea4=Label(frame, text="4.-Estas plantas requieren un suelo húmedo y bien drenado. Regar al menos dos veces en semana sin encharcar el suelo.", bg="#e2f3d1")
    Tarea4.grid(row=3, column=1, sticky="w")
    Tarea5=Label(frame, text="5.-Añadir fertilizante a la tierra de las hortensias ayudará a su floración.", bg="#e2f3d1")
    Tarea5.grid(row=4, column=1, sticky="w")
    botonHecho=Button(frame,text="Hecho", command=rootHortensias.destroy, bg="#e2f3d1")
    botonHecho.grid(row=5, column=1,sticky="") 
    rootHortensias.mainloop()

def Nopal():
    rootNopal=Toplevel()
    frame=Frame(rootNopal)
    frame.pack()
    frame.config( bg="#e2f3d1")
    rootNopal.title("Como cuidar de tus Hortensias")
    rootNopal.iconbitmap("girasol3.ico")
    Tarea1=Label(frame, text="1.-Busca una maceta con agujeros en la base, ya que esto permitirá que se drene el exceso de agua.", bg="#e2f3d1")
    Tarea1.grid(row=0, column=1, sticky="w")
    Tarea2=Label(frame, text="2.-Trasládalo al marco de una ventana u otra zona expuesta a mucha luz solar intensa pero indirecta.", bg="#e2f3d1")
    Tarea2.grid(row=1, column=1, sticky="w")
    Tarea3=Label(frame, text="3.-Una vez establecidas, la mayor parte de las especies de cactus requieren varias horas de luz directa del sol todos los días.", bg="#e2f3d1")
    Tarea3.grid(row=2, column=1, sticky="w")
    Tarea4=Label(frame, text="4.-El riego excesivo puede matarlo, pero necesitará que lo riegues semanalmente durante los periodos de crecimiento activo.", bg="#e2f3d1")
    Tarea4.grid(row=3, column=1, sticky="w")
    Tarea5=Label(frame, text="5.-El cactus también se beneficia de las fertilizaciones regulares durante la primavera, el verano o el otoño.", bg="#e2f3d1")
    Tarea5.grid(row=4, column=1, sticky="w")
    botonHecho=Button(frame,text="Hecho", command=rootNopal.destroy, bg="#e2f3d1")
    botonHecho.grid(row=5, column=1,sticky="") 
    rootNopal.mainloop()"""




#--------------INFORMACION DE INTERFAZ--------------
def Menu_Mis_Plantas():
    rootmisp=Toplevel()
    rootmisp.title("Mis Plantas")
    label=Label(rootmisp)
    frame=Frame(rootmisp)
    frame.config(width="500", height="500", bg="#e2f3d1")
    frame.pack()
    rootmisp.iconbitmap("girasol3.ico")
    if var1.get()==1:
        ImagenGirasol=PhotoImage(file="img/misImagenes.png")
        labelGirasol=Label(frame,  image=ImagenGirasol)
        labelGirasol.grid(row=0, column=0, padx=10, pady=10)
        botonGirasol=Button(frame, text="Girasol", command=MenuGirasol, bg="#e1f5ce")
        botonGirasol.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
    if var2.get()==1:
        ImagenAloe=PhotoImage(file="img/Aloe-Vera.png")
        LabelAloe=Label(frame, image=ImagenAloe)
        LabelAloe.grid(row=1,column=0, padx=10, pady=10)
        BotonAloe=Button(frame, text="Aloe Vera", command=MenuAloeVera, bg="#e2f3d1")
        BotonAloe.grid(row=1, column=1, padx=10, pady=10, sticky="nswe")
    if var3.get()==1:
        ImagenManzanilla=PhotoImage(file="img/manzanilla.png")
        LabelManzanilla=Label(frame, image=ImagenManzanilla)
        LabelManzanilla.grid(row=2, column=0, padx=10, pady=10)
        botonManzanilla=Button(frame, text="Manzanilla", command=MenuManzanilla, bg="#e2f3d1")
        botonManzanilla.grid(row=2, column=1, padx=10, pady=10, sticky="nswe")
    if var4.get()==1:
        ImagenDiente=PhotoImage(file="img/diente.png")
        LabelDiente=Label(frame, image=ImagenDiente)
        LabelDiente.grid(row=3, column=0, padx=10, pady=10)
        botonDiente=Button(frame, text="Diente de Leon",  bg="#e2f3d1", command=MenuDiente)
        botonDiente.grid(row=3, column=1, padx=10, pady=10, sticky="nswe")
    if var5.get()==1:
        ImagenRosa=PhotoImage(file="img/rosas.png")
        LabelRosa=Label(frame, image=ImagenRosa)
        LabelRosa.grid(row=0, column=2, padx=10, pady=10)
        botonRosa=Button(frame, text="Rosa", bg="#e2f3d1", command=MenuRosa )
        botonRosa.grid(row=0, column=3, padx=10, pady=10, sticky="nswe")
    if var6.get()==1:
        ImagenHortensia=PhotoImage(file="img/hortensia.png")
        LabelHortensia=Label(frame, image=ImagenHortensia)
        LabelHortensia.grid(row=1, column=2, padx=10, pady=10)
        botonHortensia=Button(frame, text="Hortensia", bg="#e2f3d1", command=MenuHortensia)
        botonHortensia.grid(row=1, column=3, padx=10, pady=10, sticky="nswe")
    if var7.get()==1:
        ImagenTulipan=PhotoImage(file="img/tulipan.png")
        LabelTulipan=Label(frame, image=ImagenTulipan)
        LabelTulipan.grid(row=2, column=2, padx=10, pady=10)
        botonTulipan=Button(frame, text="Tulipan", bg="#e2f3d1", command=MenuTulipan)
        botonTulipan.grid(row=2, column=3, padx=10, pady=10, sticky="nswe")
    if var8.get()==1:
        ImagenNopal=PhotoImage(file="img/nopal.png")
        LabelNopal=Label(frame, image=ImagenNopal)
        LabelNopal.grid(row=3, column=2, padx=10, pady=10)
        botonNopal=Button(frame, text="Nopal", bg="#e2f3d1", command=MenuNopal)
        botonNopal.grid(row=3, column=3, padx=10, pady=10, sticky="nswe")



    #-----------------------Frame para Volver a Menu--------
    
    BotonMenu=Button(frame, text="Menu", command=rootmisp.destroy, bg="#e2f3d1")
    BotonMenu.grid(row=4, column=1 ,padx=10, pady=10, columnspan=2)
    

    rootmisp.mainloop()

"""def Abrir_Agregar_Planta():
	Menu_Agregar_Plantas()"""

def Menu_Principal():
    raiz=Toplevel()
    raiz.title("Menu Principal",)
    miFrame=Frame(raiz)
    fondo=PhotoImage(file="img/fondogeneral.png")
    labelfondo=Label(miFrame,image=fondo)
    labelfondo.place(relwidth=1, relheight=1)
    miFrame.pack()
    miFrame.config(width="400", height="375")
    miFrame.config(bg="Gray")

    raiz.iconbitmap("girasol3.ico")

    labelTitulo=Label(miFrame,text="GreenWorld", font=("Comic Sans Ms", 25), bg="#edfedc")
    labelTitulo.place(x=100,y=30)




    #-------------IMAGENES-------------
    """imagenLogo=PhotoImage(file="logo2.png")
    labelLogo=Label(miFrame, image=imagenLogo)
    labelLogo.place(x=70,y=30,)"""
    imagenDatos=PhotoImage(file="img/datos4.png")
    labelDatos=Label(miFrame, image=imagenDatos)	
    labelDatos.place(x=100,y=100)
    imagenAgregar=PhotoImage(file="img/AgregarPlanta.png")
    labelAgregar=Label(miFrame, image=imagenAgregar)
    labelAgregar.place(x=100,y=230)
    imagenMisPlantas=PhotoImage(file="img/misPlantas4.png")
    labelMisPlantas=Label(miFrame, image=imagenMisPlantas)
    labelMisPlantas.place(x=200,y=100)
    imagenMisImagenes=PhotoImage(file="img/misImagenes.png")
    labelMisImagenes=Label(miFrame, image=imagenMisImagenes)
    labelMisImagenes.place(x=200,y=230)




    #------------BOTONES-------------------

    botonDatos=Button(miFrame, text="Datos Curiosos", width=11, height=2, command= Menu_Datos_Curiosos, bg="#edfedc")
    botonDatos.place(x=100,y=180)
    botonMisPlantas=Button(miFrame, text="Mis Plantas", width=11, height=2, command=Menu_Mis_Plantas, bg="#edfedc")
    botonMisPlantas.place(x=200,y=180)
    botonAgregarPlanta=Button(miFrame, text="Agregar Planta", width=11, height=2 ,command=raiz.destroy, bg="#edfedc")
    botonAgregarPlanta.place(x=100, y=325)
    botonMisComentarios=Button(miFrame, text="Mis Comentarios", width=12, height=2,  bg="#edfedc", command=Menu_Mis_Comentarios)
    botonMisComentarios.place(x=200, y=325)

    """miImagen=PhotoImage(file="logo.png")
    miLabel12=Label(miFrame, image=miImagen)
    miLabel12.place(x=10,y=10)"""



    raiz.mainloop()


#CREANDO LOGIN CON PYTHON Y TKINTER.

#IMPORTAMOS LIBRERÍAS NECESARIAS.

#CREAMOS VENTANA PRINCIPAL.

def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry("300x250")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("GreenWorld")#TITULO DE LA VENTANA
    ventana_principal.iconbitmap("girasol3.ico")
    miFrame=Frame(ventana_principal)
    imagenfondo=PhotoImage(file="img/fondoh.png")
    labelfondo=Label(miFrame, image=imagenfondo)
    labelfondo.place(relwidth=1, relheight=1)
    miFrame.pack()
    titulo=Label(miFrame, text="Bienvenido a GreenWorld", bg="#884673", width="30", height="2", font=("Calibri", 14))#ETIQUETA CON TEXTO
    titulo.grid(row=0, column=0)
    espacio=Label(miFrame,text="", bg="#c8a8fe")
    espacio.grid(row=1, column=0)

    acceder=Button(miFrame,text="Acceder", height="2", width="30", bg=pestas_color, command=login) #BOTÓN "Acceder"
    acceder.grid(row=2, column=0)
    espacio2=Label(miFrame,text="", bg="#c8a8fe")
    espacio2.grid(row=3, column=0)
    registrarse=Button(miFrame,text="Registrarse", height="2", width="30", bg=pestas_color, command=registro) #BOTÓN "Registrarse".
    registrarse.grid(row=4, column=0)
    espacio3=Label(miFrame,text="", bg="#c8a8fe")
    espacio3.grid(row=5, column=0)
    espacio3=Label(miFrame,text="", bg="#c8a8fe")
    espacio3.grid(row=6, column=0)
    espacio3=Label(miFrame,text="", bg="#c8a8fe")
    espacio3.grid(row=7, column=0)
    espacio3=Label(miFrame,text="", bg="#c8a8fe")
    espacio3.grid(row=8, column=0)
    ventana_principal.mainloop()

#CREAMOS VENTANA PARA REGISTRO.
def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")
    ventana_registro.iconbitmap("girasol3.ico")
    ventana_registro.config(bg="#c8a8fe")
 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "nombre_usuario"
    clave = StringVar() #DECLARAMOS "sytring" COMO TIPO DE DATO PARA "clave"
 
    Label(ventana_registro, text="Introduzca datos",bg="#c8a8fe", font=("Calibri", 13)).pack()
    Label(ventana_registro, text="",bg="#c8a8fe").pack()
    etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario * ",bg="#c8a8fe")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario,bg="#d6d6d6") #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contraseña * ",bg="#c8a8fe")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*',bg="#d6d6d6") #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_clave.pack()
    Label(ventana_registro, text="",bg="#c8a8fe").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1,bg="#d6d6d6", command = registro_usuario).pack() #BOTÓN "Registrarse"

#CREAMOS VENTANA PARA LOGIN.

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    ventana_login.iconbitmap("girasol3.ico")
    ventana_login.config(bg="#c8a8fe")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña",bg="#c8a8fe", font=("Calibri", 12)).pack()
    Label(ventana_login, text="",bg="#c8a8fe").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ",bg="#c8a8fe").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario,bg="#d6d6d6")
    entrada_login_usuario.pack()
    Label(ventana_login, text="",bg="#c8a8fe").pack()
    Label(ventana_login, text="Contraseña * ",bg="#c8a8fe").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*',bg="#d6d6d6")
    entrada_login_clave.pack()
    Label(ventana_login, text="",bg="#c8a8fe").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login,bg="#d6d6d6").pack()

#VENTANA "VERIFICACION DE LOGIN".

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
 
    lista_archivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if clave1 in verifica:
            exito_login() #...EJECUTAR FUNCIÓN "exito_login()"
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
        else:
            no_clave() #...EJECUTAR "no_clave()"
    #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
    else:
        no_usuario() #..EJECUTA "no_usuario()".


# VENTANA "Login finalizado con exito".
 
def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.iconbitmap("girasol3.ico")
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    ventana_exito.config(bg="#c8a8fe")
    Label(ventana_exito, text="Login finalizado con exito",bg="#c8a8fe").pack()
    Button(ventana_exito, text="OK", command=borrar_exito_login).pack()
 
#VENTANA DE "Contraseña incorrecta".
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    ventana_no_clave.config(bg="#c8a8fe")
    Label(ventana_no_clave, text="Contraseña incorrecta ",bg="#c8a8fe").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".
 
#VENTANA DE "Usuario no encontrado".
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    ventana_no_usuario.config(bg="#c8a8fe")
    Label(ventana_no_usuario, text="Usuario no encontrado",bg="#c8a8fe").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"

#CERRADO DE VENTANAS


def borrar_exito_login():
    ventana_exito.destroy()
    ventana_login.destroy()
    ventana_principal.destroy()



 
def borrar_no_clave():
    ventana_no_clave.destroy()

 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()

#REGISTRO USUARIO
 
def registro_usuario():
 
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
 
    file = open(usuario_info, "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
 
    Label(ventana_registro, text="Registro completado con éxito", bg="#c8a8fe", font=("calibri", 11)).pack()

def abrir_Menu():
    miFrame=Tkinter.Toplevel(raiz)
 


ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.
raizagregar=Tk()
raizagregar.iconbitmap("girasol3.ico")
global var1
var1=IntVar()
global var2
var2=IntVar()
global var3
var3=IntVar()
global var4
var4=IntVar()
global var5
var5=IntVar()
global var6
var6=IntVar()
global var7
var7=IntVar()
global var8
var8=IntVar()
miFrame=Frame(raizagregar) 
miFrame.pack()
miFrame.config( bg="#edfedc")
raizagregar.title("Agregar Planta")
checkVar1=IntVar()
checkVar2=IntVar()
Titulo=Label(miFrame, text="Favor de seleccionar sus plantas", bg="#edfedc", font=("Comic Sans Ms", 10))
Titulo.grid(row=0, column=0)
C1=Checkbutton(miFrame, text="Girasol",variable=var1, onvalue=1, offvalue=0, bg="#edfedc")
C1.grid(row=1, column=0, sticky="w")
C2=Checkbutton(miFrame, text="Aloe Vera", variable=var2, onvalue=1, offvalue=0, bg="#edfedc")
C2.grid(row=2, column=0, sticky="w")
C3=Checkbutton(miFrame, text="Manzanilla", variable=var3,onvalue=1, offvalue=0, bg="#edfedc")
C3.grid(row=3, column=0, sticky="w")
C4=Checkbutton(miFrame, text="Diente de Leon", variable=var4, onvalue=1, offvalue=0, bg="#edfedc")
C4.grid(row=4, column=0, sticky="w")
C5=Checkbutton(miFrame, text="Rosa", variable=var5, onvalue=1, offvalue=0,bg="#edfedc")
C5.grid(row=1, column=1, sticky="w")
C6=Checkbutton(miFrame, text="Hortensia", variable=var6, onvalue=1, offvalue=0,bg="#edfedc")
C6.grid(row=2, column=1, sticky="w")
C7=Checkbutton(miFrame, text="Tulipan", variable=var7, onvalue=1, offvalue=0,bg="#edfedc")
C7.grid(row=3, column=1, sticky="w")
C8=Checkbutton(miFrame, text="Nopal", variable=var8, onvalue=1, offvalue=0,bg="#edfedc")
C8.grid(row=4, column=1, sticky="w")
BotonMenu=Button(miFrame, text="Menu", command=Menu_Principal, bg="#edfedc")
BotonMenu.grid(row=5, column=0)
raizagregar.mainloop() 

