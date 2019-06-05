from tkinter import *
import os
from tkinter import simpledialog
import math
from tkinter import messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
from fractions import Fraction as fr
import matplotlib.pyplot as plt
import math as mathmt
import tkinter.filedialog as filedialog
#ELÍAS DÁVILA TORRES
#05/JUNIO/2019
#ESTE PROGRAMA HACE CALCULOS DE PRIMERO Y SEGUNDO GRADO, CON PLOTEOS DE RECTA Y CIRCUNFERENCIA, TAMBIÉN DECODIFICA A VARIAS BASES INCLUYENDO LA BASE MAYA CON SUS RESPECTIVOS SIMBOLOS
#NOTA : SE DEBE DE INCLUIR LA CARPETA "mayas-resize" EN EL ORIGEN DONDE SE GUARDE ESTE PROGRAMA, SE PUEDE DESCARGAR DE GITHUB, O DESCARGAR EL PROYECTO COMPLETO https://github.com/DanteFX/Programming-Final-Project
####MAIN CONFIG WINDOW###########################
ventana = Tk()
ventana.title('CALCULATOR')
label = Label(ventana, text= 'Enter operation:')
label.grid(row=1,column=1)
entry = Entry(ventana)
#entry.insert(END)
print("RUNING")
#####MODE VAR############################################
mode = 1
#####COMMANDS VAR########################################
cl = "clear"
cl_INFO = "clear --help"
as_maya = "in maya"
as_bin = "in bin"
as_hex = "in hex"
as_octal = "in octal"
exit = "exit()"
entrada = 0
env_user = os.environ["USER"]
####DEFINITIIONS#########################################

#Esta función evalua la entrada y la decodifica a base binario.
def BIN():
	print("BIN MODE")
	s = str(entry.get())
	if as_bin in s:
		entrada = entry.get()
		entrada = entrada.translate({ord(i): None for i in 'inbin'})
		entrada = int(entrada)
		decimal = int(entrada)
		text.insert(END, bin(decimal)+ '\n')
	else:
		entrada = eval(entry.get())
		entrada = int(entrada)
		decimal = int(entrada)
		text.insert(END, bin(decimal)+ '\n')
#Esta función evalua la entrada y la decodifica a base hexadecimal.
def HEX():
	print("HEX MODE")
	s = str(entry.get())
	if as_hex in s:
		entrada = entry.get()
		entrada = entrada.translate({ord(i): None for i in 'inhex'})
		entrada = int(entrada)
		decimal = int(entrada)
		text.insert(END, hex(decimal)+ '\n')
	else:
		entrada = eval(entry.get())
		entrada = int(entrada)
		decimal = int(entrada)
		text.insert(END, hex(decimal)+ '\n')
#Esta función evalua la entrada y la decodifica a base octal.
def OCTAL():
	print("OCTAL MODE")
	s = str(entry.get())
	if as_octal in s:
		entrada = entry.get()
		entrada = entrada.translate({ord(i): None for i in 'inoctal'})
		entrada = int(entrada)
		decimal = int(entrada)
		text.insert(END, oct(decimal)+ '\n')
	else:
		entrada = eval(entry.get())
		entrada = int(entrada)
		decimal = int(entrada)
		text.insert(END, oct(decimal)+ '\n')
#Esta función decodifica la salida de la operación recibida ara convertirlo a maya.
def MA():
	s = str(entry.get())
	if as_maya in s:
		entrada = entry.get()
		entrada = entrada.translate({ord(i): None for i in 'inmaya'})
		entrada = int(entrada)
	else:
		entrada = eval(entry.get())
		entrada = int(entrada)

	print("MAYA MODE")
	mode = 3
	#window = tk.Toplevel(ventana)
	newwin = Toplevel(ventana)
	display = Label(newwin)
	display.pack()
	#Esta condición es por si la entrada es menor a 20 entonces se utiliza un solo nivel de altura para la salida en maya.
	if int(entrada) < 20:
		# img0 = ImageTk.PhotoImage(Image.open("./mayas-resize/ts.png"))
		# img1 = ImageTk.PhotoImage(Image.open("./mayas-resize/ts.png"))
		img2 = ImageTk.PhotoImage(Image.open("./mayas-resize/ts.png"))
		img3 = ImageTk.PhotoImage(Image.open("./mayas-resize/ts.png"))
		img4 = ImageTk.PhotoImage(Image.open("./mayas-resize/%s.png"% entrada))
		# label0 = Label(newwin,  image=img0)
		# label1 = Label(newwin,  image=img1)
		label2 = Label(newwin,  image=img2)
		label3 = Label(newwin,  image=img3)
		label4 = Label(newwin,  image=img4)
		# label0.image = img0
		# label1.image = img1
		label2.image = img2
		label3.image = img3
		label4.image = img4
		# label0.pack(padx=30, pady=30)
		# label1.pack(padx=30, pady=30)
		label2.pack(padx=30, pady=30)
		label3.pack(padx=30, pady=30)
		label4.pack(padx=30, pady=30)
	#Si la entrada es mayor a 20 entonces se decodifica la entrada para usar mas de 1 nivel de altura para los numeros mayas.
	else:
		a = entrada / 20
		a = int(a)
		remainder_a = entrada % 20
		remainder_a = int(remainder_a)
		b = a / 20
		b = int(b)
		remainder_b = a % 20
		remainder_b = int(remainder_b)
		print(b)
		print(remainder_b)
		print(remainder_a)

		# img0 = ImageTk.PhotoImage(Image.open("./mayas-resize/ts.png"))
		# img1 = ImageTk.PhotoImage(Image.open("./mayas-resize/ts.png"))
		img2 = ImageTk.PhotoImage(Image.open("./mayas-resize/%s.png"% b))
		img3 = ImageTk.PhotoImage(Image.open("./mayas-resize/%s.png"% remainder_b))
		img4 = ImageTk.PhotoImage(Image.open("./mayas-resize/%s.png"% remainder_a))
		# label0 = Label(newwin,  image=img0)
		# label1 = Label(newwin,  image=img1)
		label2 = Label(newwin,  image=img2)
		label3 = Label(newwin,  image=img3)
		label4 = Label(newwin,  image=img4)
		# label0.image = img0
		# label1.image = img1
		label2.image = img2
		label3.image = img3
		label4.image = img4
		# label0.pack(padx=30, pady=30)
		# label1.pack(padx=30, pady=30)
		label2.pack(padx=30, pady=30)
		label3.pack(padx=30, pady=30)
		label4.pack(padx=30, pady=30)


#Esta función es el botón primario para operaciónes simples y comandos especificos.
def go():
	s = str(entry.get())
	if entry.get() == cl:
		text.delete(1.0, END)
	else:
		if entry.get() == cl_INFO:
			messagebox.showinfo("CLEAR INFO",(str("EL COMANDO CLEAR LIMPIA LA PANTALLA DE RESULTADOS")))
		else:

			if as_maya in s:
				MA()
			else:
				if as_bin in s:
					BIN()
				else:
					if as_hex in s:
						HEX()
					else:
						if as_octal in s:
							OCTAL()
						else:
							if exit in s:
								ventana.destroy()
							else:
								print("LET'S GO ;)")
								entrada = eval(entry.get())
								entrada = str(entrada)
								text.insert(END, entrada + '\n')
#Esta función hace operación de mutliplicación con fracciones
def fraccionmulti():
    num1 = fr(simpledialog.askstring("FRACCIONES", "Ingresa el primer numero"))
    num2 = fr(simpledialog.askstring("FRACCIONES", "Ingresa el segundo numero"))
    output = num1*num2
	#messagebox.showinfo("Resultado",(str(output)))
#Esta función hace operación de division con fracciones
def fracciodivi():
    num1 = fr(simpledialog.askstring("FRACCIONES", "Ingresa el primer numero"))
    num2 = fr(simpledialog.askstring("FRACCIONES", "Ingresa el segundo numero"))
    output = num1/num2
    messagebox.showinfo("Resultado",(str(output)))
	#text.insert(END, str(output) + '\n')
#Esta función hace operación de suma con fracciones
def fraccionsuma():
    num1 = fr(simpledialog.askstring("FRACCIONES", "Ingresa el primer numero"))
    num2 = fr(simpledialog.askstring("FRACCIONES", "Ingresa el segundo numero"))
    output = num1+num2
    messagebox.showinfo("Resultado",(str(output)))
	#text.insert(END, str(output) + '\n')
#Esta función hace operación de resta con fracciones
def fraccionresta():
    num1 = fr(simpledialog.askstring("FRACCIONES", "Ingresa el primer numero"))
    num2 = fr(simpledialog.askstring("FRACCIONES", "Ingresa el segundo numero"))
    output = num1-num2
    messagebox.showinfo("Resultado",(str(output)))
	#text.insert(END, str(output) + '\n')
#Esta función hace el calculo de una ecuación de primer grado, la entrada con dialogo y salida con caja de información.
def ecuacion():
    rl = int(simpledialog.askstring("ECUACIONES", "Numero Real:"))
    x = int(simpledialog.askstring("ECUACIONES", "Numero de x:"))
    r = int(simpledialog.askstring("ECUACIONES", "Resultado:"))
    num1 = r - rl
    num2 = num1 / x
    output= rl, "+",x,"x =",r, "x =", num2
    messagebox.showinfo("Resultado:",(str(output)))
	#text.insert(END, str(output) +'\n)
#Esta función hace el calculo de una recta con ambos puntos, entrada con dialogo, salida con caja de información y ploteo de la recta con matplot.
def ecuacionambos():
    y2 = float(simpledialog.askstring("RECTA", "Numero de y2:"))
    y1 = float(simpledialog.askstring("RECTA", "Numero de y1:"))
    x2 = float(simpledialog.askstring("RECTA", "Numero de x2:"))
    x1 = float(simpledialog.askstring("RECTA", "Numero de x1:"))
    m = (y2 - y1) / (x2 - x1)
    b= ((y2) - (m * (x2)))
    op = 'y = {}X + {} = ' .format (m,b)
    messagebox.showinfo("COMPUTANDO...",(str(op)))
    x = [1,2,3,4,5,6,7,8,9,10]
    y = []
    z = 0
    for t in x:
        z = z+1

        y.append((m * z) + b)
    plt.scatter(x,y)
    plt.show()

#Esta función hace el calculo de una recta con un punto y la b, entrada con dialogo, salida con caja de información y ploteo de la recta con matplot.
def pb():
    b = float(simpledialog.askstring("RECTA", "Numero de b:"))
    y = float(simpledialog.askstring("RECTA", "Numero de y:"))
    x = float(simpledialog.askstring("RECTA", "Numero de x:"))
    m = (y - b) / x

    op = " y = {}x + {} = ".format(m, b)
    messagebox.showinfo("COMPUTANDO...",(str(op)))
    x = [1,2,3,4,5,6,7,8,9,10]
    y = []
    z = 0
    for t in x:
        z = z+1

        y.append((m * z) + b)
    plt.scatter(x,y)
    plt.show()
#Esta función hace el calculo de una recta con un punto y la m, entrada con dialogo, salida con caja de información y ploteo de la recta con matplot.
def pm():

    m = float(simpledialog.askstring("RECTA", "Numero de m:"))
    y = float(simpledialog.askstring("RECTA", "Numero de y:"))
    x = float(simpledialog.askstring("RECTA", "Numero de x:"))

    b =  ((y) - (m * (x)))
    op = "y = {}x + {} = ".format(m, b)
    messagebox.showinfo("COMPUTANDO...",(str(op)))
    x = [1,2,3,4,5,6,7,8,9,10]
    y = []
    z = 0
    for t in x:
        z = z+1

        y.append((m * z) + b)
    plt.scatter(x,y)
    plt.show()

#Esta función hace el calculo y plteo de una circunferencia, con entradra de un dialogo y salida de caja de información, y salida de ploteo con la libreia matplot
def ecuacioncirc():

    y2 = float(simpledialog.askstring("CIRCUNFERENCIA", "Y2:"))
    y1 = float(simpledialog.askstring("CIRCUNFERENCIA", "Y1:"))
    x2 = float(simpledialog.askstring("CIRCUNFERENCIA", "X2:"))
    x1 = float(simpledialog.askstring("CIRCUNFERENCIA", "X1:"))
    op = int((x1 -x2)**2)
    op1 = int((y1 -y2)**2)
    r1 = op + op1
    r = (r1)**.5

    messagebox.showinfo("Resultado:",(str(r)))
	#text.insert(END, str(r) + '\n')
    x = plt.Circle((op,op1), r, color='r')
    plt.gcf().gca().add_artist(x)
    plt.axis([-(op+5),(op+5),-(op1+5),(op1+5)])
    plt.grid()
    plt.show()

#Esta función hace el calculo de numeros imaginarios, con entradra de un dialogo y salida de caja de información.
def numerosimaginarios():
    real = float(simpledialog.askstring("Real", "Numero Real:"))
    imag = float(simpledialog.askstring("Imaginario", "Numero Imaginario:"))
    out1 = (real**2 + imag**2)**.5
    tangente = mathmt.degrees(mathmt.atan(imag/real))
    info = str("¡LISTO!")
    out = messagebox.showinfo("COMPUTANDO...",str(info))
    if out == 1:
        tangente = tangente
    elif out == 2:
        tangente = 180 - tangente
    elif out == 3:
        tangente = 180 + tangente
    elif out == 4:
        tangente = 360 - tangente
        output = ("{} (cos {} + sin {})".format(out1,tangente,tangente))
    messagebox.showinfo("Resultado", "{} (cos {} + sin {})".format(out1,tangente,tangente))
	#text.insert(END, str("{} (cos {} + sin {})".format(out1,tangente,tangente)) + '\n')


    plt.scatter(real,imag, s=100 ,marker='o',)
    plt.grid()
    plt.title("Resultado")
    plt.show()
#Esta función hace el calculo de una ecuacion de segundo grado, desplegando ventanas de texto
def ecuacionsegundogrado():
    a = float(simpledialog.askstring("N.- a", "\n a:"))
    b = float(simpledialog.askstring("N.- b", "\n b:"))
    c = float(simpledialog.askstring("N.- c", "\n c:"))
    if b**2 - 4*a*c < 0 :
        r=-b/float(2*a)
        i=(math.sqrt(-(b**2-4*a*c)))/(2*a)
        x=complex(r,i)
        output = ("\n\a x (+) = "+str(x.real)+'+'+str(x.imag)+"\n")
        output1 = ("\n\a x (-) = "+str(x.real)+'-'+str(x.imag)+"\n")
        messagebox.showinfo("Resultado Imaginario:",(str(output)))
		#text.insert(END, str("Resultado Imaginario:") + '\n')
		#text.insert(END, str(output) + '\n')
        messagebox.showinfo("Resultado Imaginario:",(str(output1)))
		#text.insert(END, str("Resultado Real:") + '\n')
		#text.insert(END, str(output1) + '\n')

        messagebox.showinfo("\n\a x (+) = "+str(x.real)+'+'+str(x.imag)+"j\n")
        messagebox.showinfo("\n\a x (-) = "+str(x.real)+'-'+str(x.imag)+"j\n")
    else:
        xmas = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        xmenos = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        output2 = ("\n\a x (+) = "+str(xmas)+"\n")
        output3 = ("\n\a x (-) = "+str(xmenos)+"\n")
        messagebox.showinfo("\n\a x (+) = "+str(xmas)+"\n")
        messagebox.showinfo("\n\a x (-) = "+str(xmenos)+"\n")
        messagebox.showinfo("Resultado Real:",(str(output2)))
		#text.insert(END, str("Resultado Real:") + '\n')
		#text.insert(END, str(output2) + '\n')
        messagebox.showinfo("Resultado Real:",(str(output3)))
		#text.insert(END, str(output3) + '\n')

    input()
#Esta función despliega una ventana de dialogo para especificar la ruta para guardar el archivo, a la vez que pide el nombre y escribe el archivo
def file_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    text2save = str(text.get(1.0, END))
    f.write(text2save)
    f.close() # `()` was missing.
#Esta función despliega una ventana de dialogo para especificar la ruta para abrir el archivo, ya especificado lee y escribe en el area de texto
def open_file():
	f = filedialog.askopenfilename()
	file = open(f, "r")
	if file is None:
		return
	text.delete(1.0, END)
	for linea in file.readlines():
		text.insert(END, linea)
	file.close()

#####INICIALIZACIÓN DEL MENU Y SUS DERIVADOS###########################################
button = Button(ventana, text='Go', command = go)
text = Text(ventana)
barra=Menu(ventana)
submenu=Menu(barra)
submenu2=Menu(barra)
submenu3=Menu(barra)
menucalculo=Menu(barra)
menuecuaciones=Menu(barra)
menurecta=Menu(barra)
menufracciones=Menu(barra)
menuguardar=Menu(barra)
######INSTANCIA DE LOS LABEL DE CONVERCIÓN DE BASE#######################################
submenu.add_command(label="MAYA",command=MA)
submenu.add_command(label="BIN",command=BIN)
submenu.add_command(label="HEX",command=HEX)
submenu.add_command(label="OCTAL", command=OCTAL)
barra.add_cascade(label="DECODE",menu=submenu)
#######CALCULO LABEL##########################################
menuecuaciones.add_command(label="ECUACIONES PRIMER GRADO",command=ecuacion)
menuecuaciones.add_command(label="ECUACIONES SEGUNDO GRADO",command=ecuacionsegundogrado)
menuecuaciones.add_command(label="ECUACIONES DE LA RECTA",command=ecuacionambos)
menuecuaciones.add_command(label="ECUACIONES DE LA CIRCUNFERENCIA",command=ecuacioncirc)
menuecuaciones.add_command(label="NUMEROS IMAGINARIOS",command=numerosimaginarios)
menufracciones.add_command(label="MULTIPLICACION",command=fraccionmulti)
menufracciones.add_command(label="DIVISION",command=fracciodivi)
menufracciones.add_command(label="SUMA",command=fraccionsuma)
menufracciones.add_command(label="RESTA",command=fraccionresta)
menurecta.add_command(label="Ambos puntos",command=ecuacionambos)
menurecta.add_command(label="1 punto y b",command=pb)
menurecta.add_command(label="1 punto y m",command=pm)
menuguardar.add_command(label="GUARDAR",command=file_save)
menuguardar.add_command(label="ABRIR",command=open_file)
barra.add_cascade(label="FRACCIONES",menu=menufracciones)
barra.add_cascade(label="ECUACIONES",menu=menuecuaciones)
barra.add_cascade(label="ECUACIONES DE LA RECTA",menu=menurecta)
barra.add_cascade(label="ARCHIVO",menu=menuguardar)
######INSTANCIA DE LA VENTANA PRINCIPAL, BOTÓN PRIMARIO,TEXTOS Y AREA DE SALIDA DE TEXTO##################################
ventana.config(menu=barra)
label.pack(side=TOP)
entry.pack(side=TOP)
button.pack(side=TOP)
text.pack(side= TOP)
########################################################
text.insert(END, "Resultados : " + '\n')
messagebox.showinfo("WELCOME USER",(str(env_user)))
ventana.mainloop()
