from tkinter import *
from math import sqrt, pow

def tablaMultiplicar(numero):
    numero = numero.get()
    numero = int(numero)

    print(f'tabla de multiplicar del {numero}')
    for i in range(1,11):
        print(f'{numero} x {i} = {i*numero}')


def serieFibonacci(numero):
    numero = numero.get()
    numero = int(numero)
    a = 0
    b = 1
    if numero == 0:
        print(f'La serie Fibonacci de {numero} es: {numero}')
    elif numero == 1:
        print(f'La serie Fibonacci de {numero} es: {numero}')
    else:
        for i in range(numero):
            c = b+a
            a = b
            b = c

        print(f'La serie Fibonacci de {numero} es: {a}')


def formulaGeneral(a,b,c):
    a = int(a.get())
    b = int(b.get())
    c = int(c.get())
    x1 = 0
    x2 = 0

    if((pow(b,2))-4*a*c) <=0:
        print("RESULTADO: La solucion de la ecuacion es con numeros complejos")
    else:
        x1 = (-b+sqrt(pow(b,2)-(4*a*c)))/(2*a)
        x2 = (-b-sqrt(pow(b,2)-(4*a*c)))/(2*a)
        print("Las soluciones de la ecuacion son: ")
        print(f'X1: {x1}')
        print(f'X2: {x2}')

def secondWindow():
    newWindow = Toplevel(window)
    newWindow.geometry("250x250")
    newWindow.title("Menu Formula general")
    etiqueta = Label(newWindow, text="Introduce los datos", bg="orange",)
    etiqueta.pack(fill = X)

    etiqueta_A = Label(newWindow, text="Numero A")
    etiqueta_A.pack()
    box_A = Entry(newWindow)
    box_A.insert(0, "0")
    box_A.pack()

    etiqueta_B = Label(newWindow, text="Numero B")
    etiqueta_B.pack()
    box_B = Entry(newWindow)
    box_B.insert(0, "0")
    box_B.pack()

    etiqueta_C = Label(newWindow, text="Numero C")
    etiqueta_C.pack()
    box_C = Entry(newWindow)
    box_C.insert(0, "0")
    box_C.pack()

    button_Calcular = Button(newWindow, text="Calcular", background='white', command= lambda: formulaGeneral(box_A, box_B, box_C))
    button_Calcular.pack()
    button_exit_secondWindow = Button(newWindow, text='Volver al menu', background='pink' ,command=newWindow.destroy)
    button_exit_secondWindow.pack()


window = Tk()
window.geometry("300x300")
window.title("Menu")
etiqueta = Label(window, text="Menu Principal", bg="blue",)
etiqueta.pack(fill = X)

#BOTON 1
etiqueta_Fibonacci = Label(window, text="Numero")
etiqueta_Fibonacci.pack()
box_Fibonacci = Entry(window)
box_Fibonacci.insert(0, "0")
box_Fibonacci.pack()
button_Fibonacci = Button(window, text="Obtener serie Fibonacci", background="yellow", command= lambda: serieFibonacci(box_Fibonacci))
button_Fibonacci.pack()

#BOTON 2
etiqueta_TablaMultiplicar = Label(window, text="Numero")
etiqueta_TablaMultiplicar.pack()
box_Multiplicar = Entry(window)
box_Multiplicar.insert(0, "0")
box_Multiplicar.pack()
button_TablaMultiplicar = Button(window, text="Obtener Tabla de Multiplicar", background='white', command= lambda: tablaMultiplicar(box_Multiplicar))
button_TablaMultiplicar.pack()

#BOTON 3
button_Formula_General = Button(window, text="Formula General", background="orange", command=secondWindow)
button_Formula_General.pack()

#BOTON 4 - SALIR
button_exit = Button(window, text="SALIR", background="red", command=window.quit)
button_exit.pack()

window.mainloop()
    
