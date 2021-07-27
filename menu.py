from tkinter import *

def tablaMultiplicar(num):
    print(num)
    numero = 4
    for i in range(1,11):
        print(f'{numero} x {i} = {i*numero}')


window = Tk()
window.geometry("600x500")
window.title("Menu")
etiqueta = Label(window, text="Menu Principal", bg="blue",)
etiqueta.pack(fill = X)

etiqueta_Fibonacci = Label(window, text="Numero")
etiqueta_Fibonacci.pack()
box_Fibonacci = Entry(window)
box_Fibonacci.pack()
button_Fibonacci = Button(window, text="Obtener serie Fibonacci", background="yellow")
button_Fibonacci.pack()

etiqueta_TablaMultiplicar = Label(window, text="Numero")
etiqueta_TablaMultiplicar.pack()
box_Multiplicar = Entry(window)
box_Multiplicar.pack()
num_multiplicar = box_Multiplicar.get()
button_TablaMultiplicar = Button(window, text="Obtener Tabla de Multiplicar",background='white', command= lambda: tablaMultiplicar(num_multiplicar))
button_TablaMultiplicar.pack()

button_Formula_General = Button(window, text="Formula General", background="orange")
button_Formula_General.pack()

window.mainloop()
    
