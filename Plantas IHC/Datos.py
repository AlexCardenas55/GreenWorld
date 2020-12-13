from tkinter import *


def Huertos():
	global raiz4
	raiz4=Tk()
	miFrame=Frame(raiz4)
	miFrame.pack()
	miFrame.config(bg="#cafaf6")
	raiz4.title("Huertos")
	raiz4.iconbitmap("girasol3.ico")
	labelTitulo=Label(miFrame, text="Para Comenzar", font=("Comic Sans Ms", 15), bg="#cafaf6").grid(row=0, column=0)
	labelActividad1=Label(miFrame, text="1.-Elige un área donde tus plantas tendrán luz natural.", bg="#cafaf6").grid(row=1, column=0, pady=10)
	labelActividad2=Label(miFrame, text="2.-Prepara la tierra con nutrientes que puedes otorgarle a través de abono natural hecho en casa.", wrap=300, bg="#cafaf6").grid(row=2, column=0, pady=10)
	labelActividad3=Label(miFrame, text="3.No aprietes el suelo de tus macetas, principalmente para permitir el paso del agua y oxigeno.", wrap=300, bg="#cafaf6").grid(row=3, column=0, pady=10)
	labelActividad4=Label(miFrame, text="4.-Considera el clima del lugar donde vives, para que tengas mejores frutos.", wrap=300, bg="#cafaf6").grid(row=4, column=0, pady=10)
	labelActividad1=Label(miFrame, text="5.-Elige un área donde tus plantas tendrán luz natural.", wrap=300, bg="#cafaf6").grid(row=5, column=0, pady=10)
	botonSiguiente=Button(miFrame, text="Cuidar un Huerto", command=Huertos2, bg="#cafaf6" ).grid(row=6, column=0)
	raiz4.mainloop()

def Huertos2():
	raiz4.destroy()
	raiz5=Tk()
	raiz5.title("Cuidados")
	raiz5.iconbitmap("girasol3.ico")
	miFrame2=Frame(raiz5)
	miFrame2.pack()
	miFrame2.config(bg="#cafaf6")
	labelTitulo=Label(miFrame2,text="Como cuidar un Huerto", font=("Comic Sans Ms", 15), bg="#cafaf6").grid(row=0, column=0)
	labelTarea1=Label(miFrame2,wrap=300, text="1.-Utiliza tus residuos orgánicos de plantas y verduras, así como las cáscaras de huevo para crear una composta que después podrás añadir a tus sembradíos.", bg="#cafaf6")
	labelTarea1.grid(row=1, column=0, pady=10)
	labelTarea2=Label(miFrame2,wrap=300, text="2.-Riega tus plantas por el atardecer para evitar la evaporación y favorecer la infiltración del agua en el sustrato.", bg="#cafaf6")
	labelTarea2.grid(row=2, column=0, pady=10)
	labelTarea3=Label(miFrame2,wrap=300, text="3.-No aprietes el suelo de tus macetas, principalmente para permitir el paso del agua y oxigeno.", bg="#cafaf6")
	labelTarea3.grid(row=3, column=0, pady=10)
	labelTarea4=Label(miFrame2,wrap=300, text="4.-Considera el clima del lugar donde vives, para que tengas mejores frutos", bg="#cafaf6")
	labelTarea4.grid(row=4, column=0, pady=10)
	labelTarea5=Label(miFrame2,wrap=300, text="5.-Planea tus cultivos de acuerdo al espacio que tengas disponible.", bg="#cafaf6")
	labelTarea5.grid(row=5, column=0, pady=10)
	botonCerrar=Button(miFrame2, text="Cerrar", command=raiz5.destroy,  bg="#cafaf6")
	botonCerrar.grid(row=6, column=0, pady=10)

	raiz5.mainloop()


def Beneficio():
	raiz3=Tk()
	miFrame=Frame(raiz3)
	miFrame.pack()
	miFrame.config(bg="#cdf1d5")
	raiz3.title("Beneficios de las Plantas")
	raiz3.iconbitmap("girasol3.ico")
	labelTitulo=Label(miFrame,text="Beneficio de las Plantas", font=("Comic Sans Ms", 15), bg="#cdf1d5")
	labelTitulo.grid(row=0, column=0)
	labelBeneficio1=Label(miFrame, text="Las utilizamos de alimento para las personas y para los animales.", bg="#cdf1d5")
	labelBeneficio1.grid(row=1, column=0)
	labelBeneficio2=Label(miFrame, text="Obtenemos materiales de ellas: madera, resina, caucho, fibras,...", bg="#cdf1d5")
	labelBeneficio2.grid(row=2, column=0, sticky="w")
	labelBeneficio3=Label(miFrame, text="Producen oxígeno.", bg="#cdf1d5")
	labelBeneficio3.grid(row=3, column=0, sticky="w")
	labelBeneficio4=Label(miFrame, text="Absorben dióxido de carbono.", bg="#cdf1d5")
	labelBeneficio4.grid(row=4, column=0, sticky="w")
	labelBeneficio5=Label(miFrame, text="Retienen el suelo y la humedad.", bg="#cdf1d5")
	labelBeneficio5.grid(row=5, column=0, sticky="w")
	labelBeneficio6=Label(miFrame, text="Forman entornos bellos y llenos de vida.", bg="#cdf1d5")
	labelBeneficio6.grid(row=6, column=0, sticky="w")
	labelBeneficio7=Label(miFrame, text="Ayudan a regular la temperaturas.", bg="#cdf1d5")
	labelBeneficio7.grid(row=7, column=0, sticky="w")
	botonCerrar=Button(miFrame,text="Volver", command=raiz3.destroy, bg="#cdf1d5")
	botonCerrar.grid(row=8, column=0)

	raiz3.mainloop()




def Rosas():
	raiz.destroy()
	global Imagen
	global Imagen2
	global Imagen3
	raiz2=Toplevel()
	raiz2.title("Rosas")
	miFrame=Frame(raiz2)
	miFrame.pack()
	miFrame.config(bg="Pink")
	LabelTitulo=Label(miFrame, text="Rosas", font=("Comic Sans Ms", 25))
	LabelTitulo.grid(row=0, column=0, columnspan=2)
	LabelTitulo.config(bg="Pink")
	LabelSubtitulo=Label(miFrame, text= "Tipo de FLores", font=("Comic Sans Ms", 15))
	LabelSubtitulo.grid(row=1, column=0)
	LabelSubtitulo.config(bg="Pink")
	Imagen=PhotoImage(file="img/RosaSilv.png")
	LabelImagen=Label(miFrame, image=Imagen)
	LabelImagen.grid(row=3, column=0)
	LabelImagen.config(bg="Pink")
	LabelRosasSilvestres=Label(miFrame, text="El primero tipo es el de las Rosas silvestres, y de estas flores descienden todas las demás rosas de la actualidad.", wrap=300)
	LabelRosasSilvestres.config(bg="Pink")
	LabelRosasSilvestres.grid(row=3, column=1, pady=10)
	Imagen2=PhotoImage(file="img/RosaAnt.png")
	LabelRosaAntigua=Label(miFrame, image=Imagen2)
	LabelRosaAntigua.grid(row=4, column=0, pady=10)
	LabelRosaAntigua.config(bg="Pink")
	LabelRosaAnt=Label(miFrame, text="La rosas Antiguas son aquellas conocidas desde antes de 1867 y no son muy populares en la actualidad. No obstante, son recomendables para quienes se inician en el cultivo de estas flores ya que no requieren mayores cuidados", wrap=300)
	LabelRosaAnt.config(bg="Pink")
	LabelRosaAnt.grid(row=4, column=1, pady=10)
	Imagen3=PhotoImage(file="img/RosaMod.png")
	LabelRosaModderna=Label(miFrame, image=Imagen3)
	LabelRosaModderna.grid(row=5, column=0, pady=10)
	LabelRosaModderna.config(bg="Pink")
	LabelRosaMod=Label(miFrame, text=" Las rosas Modernas están formados por las variedades aparecidas luego de 1867. Este grupo es el más popular actualmente, especialmente los llamados Híbridos de té.", wrap=300)
	LabelRosaMod.config(bg="Pink")
	LabelRosaMod.grid(row=5, column=1, pady=10)
	BotonCerrar=Button(miFrame, text="Cerar", command=raiz2.destroy, height="2", width="20")
	BotonCerrar.grid(row=6, column=1, pady=10)
	BotonCerrar.config(bg="Pink")

	raiz2.mainloop()





def Flora2():
	global raiz
	raiz2.destroy()
	raiz=Toplevel()
	raiz.title("Flora")
	miFrame=Frame(raiz)
	miFrame.pack()
	miFrame.config(bg="light Blue")
	imagenCasahuate=PhotoImage(file="img/orquidea.png")
	labelimagenC=Label(miFrame, image=imagenCasahuate)
	labelimagenC.grid(row=1, column=0)
	ImagenHortensia=PhotoImage(file="img/hortensia.png")
	labelimagenH=Label(miFrame, image=ImagenHortensia)
	labelimagenH.grid(row=0, column=0)
	labelHortensia=Label(miFrame, text="Las Hortensias son arbustos de entre uno y tres metros de altura, algunas son árboles pequeños, son especies de climas templados",wrap=300)
	labelHortensia.config(bg="light Blue")
	labelHortensia.grid(row=0, column=1, pady=10)
	
	labelOrquideas=Label(miFrame, text="Son una familia de plantas monocotiledóneas que se distinguen por la complejidad de sus flores y por sus interacciones ecológicas con los agentes polinizadores", wrap=300)
	labelOrquideas.config(bg="light Blue")
	labelOrquideas.grid(row=1, column=1, pady=10)
	ImagenTulipan=PhotoImage(file="img/tulipan.png")
	labelimagenT=Label(miFrame, image=ImagenTulipan)
	labelimagenT.grid(row=2, column=0)
	labelTulipan=Label(miFrame, text="El tulipán es una planta bulbosa de constitución herbácea y vivaz, con un corto periodo de floración, normalmente en primavera.", wrap=300)
	labelTulipan.config(bg="light Blue")
	labelTulipan.grid(row=2, column=1, pady=10)
	ImagenRosa=PhotoImage(file="img/rosas.png")
	labelimagenR=Label(miFrame, image=ImagenRosa)
	labelimagenR.grid(row=3, column=0)
	labelRosa=Label(miFrame, text="Se encuentra entre las flores más vendidas del mundo, junto a los tulipanes y los claveles, se utilizan como metodos medicinales modernos", wrap=300)
	labelRosa.config(bg="light Blue")
	labelRosa.grid(row=3, column=1, pady=10)
	botonRosa=Button(miFrame, text="Rosas", command=Rosas)
	botonRosa.grid(row=4, column=1, pady=5, padx=2)
	botonRosa.config(bg="light Blue")
	botonCerrar=Button(miFrame, text="Cerrar", command=raiz.destroy)
	botonCerrar.grid(row=5, column=1)
	botonCerrar.config(bg="light Blue")
	raiz.mainloop()


def Flora1():
	global raiz2
	global imagenCasahuate
	global imagenDamiana
	global ImagenEstafiate
	global ImagenNopal
	raiz2=Toplevel()
	raiz2.title("Flora")

	miFrame2=Frame(raiz2)
	miFrame2.pack()
	miFrame2.config(bg="#F0FFF0")

	imagenCasahuate=PhotoImage(file="img/casahuate.png")
	labelimagenC=Label(miFrame2, image=imagenCasahuate)
	labelimagenC.grid(row=1, column=0)
	labelCasahuate=Label(miFrame2, text="El Casahuate prieto es una planta de los paisajes y climas secos de México que crece de forma silvestre en las áreas secas.", wrap=300)
	labelCasahuate.grid( row=1, column=1, pady=10)
	labelCasahuate.config(bg="#F0FFF0")
	imagenDamiana=PhotoImage(file="img/damiana.png")
	LabelImagenD=Label(miFrame2, image=imagenDamiana)
	LabelImagenD.grid(row=2, column=0, pady=10)
	labelDamiana=Label(miFrame2, text=" la Damiana, es un arbusto de 0,3 a 2 metros de altura. Es también conocido como té mexicano. Posee varias propiedades medicinales", wrap=300)
	labelDamiana.grid(row=2, column=1, pady=10)
	labelDamiana.config(bg="#F0FFF0")
	ImagenEstafiate=PhotoImage(file="img/estafiate.png")
	LabelimagenE=Label(miFrame2, image=ImagenEstafiate)
	LabelimagenE.grid(row=3, column=0, pady=10)
	labelEstafiate=Label(miFrame2, text=" El Estafiate, es un arbusto de 0,2 a 1 metro de altura. Ha sido utilizado ancestralmente en México para aliviar numerosos padecimiento", wrap=300)
	labelEstafiate.grid(row=3, column=1, pady=10)
	labelEstafiate.config(bg="#F0FFF0")
	ImagenNopal=PhotoImage(file="img/nopal.png")
	LabelimagenN=Label(miFrame2, image=ImagenNopal)
	LabelimagenN.grid(row=4, column=0, pady=10)
	labelNopal=Label(miFrame2, text="El Nopal, es de la familia de los cactus. Sus frutos son comestibles y se pueden aprovechar para hacer zumos, dulces y cervezas.", wrap=300)
	labelNopal.grid(row=4, column=1, pady=10)
	labelNopal.config(bg="#F0FFF0")
	botonSiguiente=Button(miFrame2, text="Siguiente", command=Flora2)
	botonSiguiente.grid(row=5, column=1)
	botonSiguiente.config(bg="#F0FFF0")
	botonCerrar=Button(miFrame2, text="Cerrar", command=raiz2.destroy)
	botonCerrar.grid(row=6, column=1, pady=5)
	botonCerrar.config(bg="#F0FFF0")
	raiz2.mainloop()

def Principal():
	global raiz

	raiz=Toplevel()
	miFrame=Frame(raiz)
	raiz.title("Datos Curiosos")
	raiz.iconbitmap("girasol3.ico")

	miFrame.config(width="400", height="400", bg="#7aa708")
	miFrame.pack()
	fondo=PhotoImage(file="img/hojas.png")
	labelfondo=Label(miFrame, image=fondo)
	labelfondo.place(relwidth=1, relheight=1)
	botonFlora=Button(miFrame, text="Flora de Nuevo Leon", command=Flora1)
	botonFlora.grid(row=0, column=0, padx=5)
	botonFlora.config(bg="#7aa708")
	botonSalud=Button(miFrame, text="Beneficios de las Plantas", command=Beneficio)
	botonSalud.grid(row=0, column=1, padx=5)
	botonSalud.config(bg="#7aa708")
	botonHuerto=Button(miFrame, text="Huertos", command=Huertos)
	botonHuerto.grid(row=0, column=2, padx=5) 
	botonHuerto.config(bg="#7aa708")
	Titulo=Label(miFrame, text="Datos Curiosos",  font=("Comic Sans Ms", 25))
	Titulo.grid(row=1, column=1, pady=10)
	Titulo.config(bg="#7aa708")


	def Datos():
		miFrame2=Frame(raiz)
		miFrame2.pack()
		imagenCasahuate=PhotoImage(file="img/manzanilla.png")
		labelimagenC=Label(miFrame2, image=imagenCasahuate)
		labelimagenC.grid(row=1, column=0)
		labelCasahuate=Label(miFrame2, text="El casahuate prieto es una planta de los paisajes y climas secos de México que crece de forma silvestre en las áreas secas.", wrap=300)
		labelCasahuate.grid( row=1, column=1, pady=10)

		labelDamiana=Label(miFrame2, text="Es un arbusto de 0,3 a 2 metros de altura. Es también conocido como té mexicano. Posee varias propiedades medicinales", wrap=300)
		labelDamiana.grid(row=2, column=1, pady=10)
		labelEstafiate=Label(miFrame2, text="Es un arbusto de 0,2 a 1 metro de altura. Ha sido utilizado ancestralmente en México para aliviar numerosos padecimiento", wrap=300)
		labelEstafiate.grid(row=3, column=1, pady=10)
		labelNopal=Label(miFrame2, text="Es de la familia de los cactus. Sus frutos son comestibles y se pueden aprovechar para hacer zumos, dulces y cervezas.", wrap=300)
		labelNopal.grid(row=4, column=1, pady=10)


	raiz.mainloop()


"""def Flora():
	miFrame2=Frame(raiz)
	miFrame2.pack()
	botonCasahuate=Button(miFrame2, text="Casahuate Prieto")
	botonCasahuate.grid(row=0, column=0, padx=10, pady=10)
	botonDamiana=Button(miFrame2, text="Damiana")
	botonDamiana.grid(row=1, column=0, padx=0, pady=0)
	botonEstafiate=Button(miFrame2, text="Estafiate")
	botonEstafiate.grid(row=2, column=0, padx=10, pady=10)
	Imagen=PhotoImage(file="manzanilla.png")
	labelImagen=Label(miFrame2,image=Imagen)
	labelImagen.grid(row=0, column=1)"""
#---------------------FLORA DE NUEVO LEON------------