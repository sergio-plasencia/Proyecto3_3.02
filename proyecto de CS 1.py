from tkinter import *
root=Tk()


def Limpiar_datos():
    Nota_promedio1.delete(0,END)
    Nota_promedio2.delete(0,END)
    Nota_promedio3.delete(0,END)
    Nota_promedio4.delete(0,END)
    Nota_promediofinal_real.delete(0,END)
    Nota_promediofinal_redondeado.delete(0,END)
    PC_1i.delete(0,END)
    EC_1i.delete(0,END)
    PC_2i.delete(0,END)
    EC_2i.delete(0,END)
    PC_3i.delete(0,END)
    EC_3i.delete(0,END)
    PC_4i.delete(0,END)
    EC_4i.delete(0,END)

def Calcular():

    #Variables
    num_1=EC_1i.get()
    num_2=PC_1i.get()
    num_3=EC_2i.get()
    num_4=PC_2i.get()
    num_5=EC_3i.get()
    num_6=PC_3i.get()
    num_7=EC_4i.get()
    num_8=PC_4i.get()

    num_1=float(num_1)
    num_2=float(num_2)
    num_3=float(num_3)
    num_4=float(num_4)
    num_5=float(num_5)
    num_6=float(num_6)
    num_7=float(num_7)
    num_8=float(num_8)




    Promedio_1=float(num_1*0.75+num_2*0.25)
    Promedio_2=float(num_3*0.75+num_4*0.25)
    Promedio_3=float(num_5*0.75+num_6*0.25)
    Promedio_4=float(num_7*0.75+num_8*0.25)


    Nota_promedio1.insert(END,Promedio_1)
    Nota_promedio2.insert(END,Promedio_2)
    Nota_promedio3.insert(END,Promedio_3)
    Nota_promedio4.insert(END,Promedio_4)



    Promediofinal=float((Promedio_1+Promedio_2+Promedio_3+Promedio_4)/4)
    Nota_promediofinal_redondeado.insert(END,round(Promediofinal))
    Nota_promediofinal_real.insert(END,Promediofinal,)
    print(Promediofinal)
    print(round(Promediofinal))

#screen
root.geometry('{}x{}'.format(800, 370),)

#título
root.title("Calculadora de notas de mate :D")


#Etiquetas
EC_1e=Label(root,text="EC 1",font=1,fg="blue")
PC_1e=Label(root,text="PC 1",font=1,fg="blue")
EC_2e=Label(root,text="EC 2",font=1,fg="blue")
PC_2e=Label(root,text="PC 2",font=1,fg="blue")
EC_3e=Label(root,text="EC 3",font=1,fg="blue")
PC_3e=Label(root,text="PC 3",font=1,fg="blue")
EC_4e=Label(root,text="EC 4",font=1,fg="blue")
PC_4e=Label(root,text="PC 4",font=1,fg="blue")
PFredondeada=Label(root,text="Su nota redondeada es: ",font=2,fg="green")
PFreal=Label(root,text="Su nota real es: ",font=2,fg="green")

#espaciados
espaciado_0=Label(root,text="       ")
espaciado_1=Label(root,text="   ")
espaciado_2=Label(root,text="   ")
espaciado_3=Label(root,text="   ")
espaciado_4=Label(root,text="   ")
espaciado_5=Label(root,text="   ")
espaciado_6=Label(root,text="   ")
espaciado_7=Label(root,text="   ")
espaciado_8=Label(root,text="   ")
espaciado_9=Label(root,text="   ")
espaciado_10=Label(root,text="   ")
espaciado_11=Label(root,text="   ")
espaciado_12=Label(root,text="   ")


#Entradas
EC_1i=Entry()
PC_1i=Entry()
EC_2i=Entry()
PC_2i=Entry()
EC_3i=Entry()
PC_3i=Entry()
EC_4i=Entry()
PC_4i=Entry()
Nota_promedio1=Listbox(root,height=1, width=10)
Nota_promedio2=Listbox(root,height=1, width=10)
Nota_promedio3=Listbox(root,height=1, width=10)
Nota_promedio4=Listbox(root,height=1, width=10)
Nota_promediofinal_real=Listbox(root,height=1, width=10)
Nota_promediofinal_redondeado=Listbox(root,height=1, width=10)

#Botones
boton_1=Button(root,text="Calcular",command=Calcular,font=1,fg="red",bd=4,bg="pink")
boton_2=Button(root,text="Limpiar datos",command=Limpiar_datos,font=1,fg="red",bd=4,bg="pink")




#Grids
# #columna 1
espaciado_0.grid(row=0)
espaciado_1.grid(row=0,column=1)
EC_1e.grid(row=1,column=1)
espaciado_2.grid(row=2,column=1)
PC_1e.grid(row=3,column=1)
espaciado_3.grid(row=4,column=1)
espaciado_4.grid(row=5,column=1)
EC_2e.grid(row=6,column=1)
espaciado_5.grid(row=7,column=1)
PC_2e.grid(row=8,column=1)
#espacio
espaciado_6.grid(row=0,column=2)
#columna2
EC_1i.grid(row=1,column=3)
PC_1i.grid(row=3,column=3)
EC_2i.grid(row=6,column=3)
PC_2i.grid(row=8,column=3)

#columna3
espaciado_9.grid(row=0,column=4)
#IMAGEN

#promedio 1 y 2

Nota_promedio1.grid(row=2,column=5)
Nota_promedio2.grid(row=7,column=5)

#espacio
espaciado_7.grid(row=0,column=6)
#columna4
EC_3e.grid(row=1,column=7)
PC_3e.grid(row=3,column=7)
EC_4e.grid(row=6,column=7)
PC_4e.grid(row=8,column=7)

espaciado_10.grid(row=0,column=8)
EC_3i.grid(row=1,column=9)
PC_3i.grid(row=3,column=9)
EC_4i.grid(row=6,column=9)
PC_4i.grid(row=8,column=9)
#promedio 3 y 4

espaciado_11.grid(row=0,column=10)
Nota_promedio3.grid(row=2,column=11)
Nota_promedio4.grid(row=7,column=11)

#promedio final
espaciado_12.grid(row=11,column=0)
espaciado_8.grid(row=9,column=0)
Nota_promediofinal_real.grid(row=10,column=3)
Nota_promediofinal_redondeado.grid(row=12,column=3)
PFreal.grid(row=10,column=1)
PFredondeada.grid(row=12,column=1)
#Botón
boton_1.grid(row=10,column=9)
boton_2.grid(row=12,column=9)
root.mainloop()
