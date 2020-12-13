from tkinter import  *

def funcion():
    otra_ventana = Toplevel(root)
    root.iconify()

root = Tk()
boton = Button(root, text="Abrir otra ventana", command=funcion)
boton.pack()
root.mainloop()