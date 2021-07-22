from tkinter import *
import os

#Funcion para obtener
def Obtain(srcS,index):
	File=open(srcS,"r")
	Lines=File.readlines()
	File.close()
	Result=Lines[index].rstrip("\n")
	Result.strip()
	return Result
	pass

#Configuration Window
WConfig=Tk()

WConfig.title("ICOS (Interactive COncept Simplifier) Configuration")
WConfig.iconbitmap('Logo.ico')

srcConfig="Configuration.txt"

def modificar(arch,line,val):
	File=open(arch, "r")
	lines=File.readlines()
	File.close()
	lines[line]=str(val)+"\n"
	File_New=open(arch, "w")
	for l in lines:
		File_New.write(l)
		pass
	File_New.close()
	pass
def Reload():
	Configures =[[Obtain(srcConfig,2),Obtain(srcConfig,3),Obtain(srcConfig,4),Obtain(srcConfig,5),Obtain(srcConfig,6),Obtain(srcConfig,7),Obtain(srcConfig,8)],
			[Obtain(srcConfig,11),Obtain(srcConfig,12),Obtain(srcConfig,13),Obtain(srcConfig,14),Obtain(srcConfig,15),Obtain(srcConfig,16),Obtain(srcConfig,17)],
			[Obtain(srcConfig,20)],[Obtain(srcConfig,23)],[Obtain(srcConfig,26)]]
	FColor= [Configures[1][0],Configures[1][1],Configures[1][2],Configures[1][3],Configures[1][4],Configures[1][5],Configures[1][6]]
	FName=  [Configures[0][0],Configures[0][1],Configures[0][2],Configures[0][3],Configures[0][4],Configures[0][5],Configures[0][6]]
	TxtBack=Configures[2][0]
	SColor=Configures[3][0]
	System=Configures[4][0]#PC or rPi
	pass
def EndConfigure(srcS):
	conf = [[TxtFlange1N,TxtFlange2N,TxtFlange3N,TxtFlange4N,TxtFlange5N,TxtFlange6N,TxtFlange7N],
			[TxtFlange1C,TxtFlange2C,TxtFlange3C,TxtFlange4C,TxtFlange5C,TxtFlange6C,TxtFlange7C],
			[TxtTBack],[TxtSColor],[TxtSystem]]
	#Configures=
	print(conf[0][0])
	modificar(srcS,2,conf[0][0].get())
	modificar(srcS,3,conf[0][1].get())
	modificar(srcS,4,conf[0][2].get())
	modificar(srcS,5,conf[0][3].get())
	modificar(srcS,6,conf[0][4].get())
	modificar(srcS,7,conf[0][5].get())
	modificar(srcS,8,conf[0][6].get())
	modificar(srcS,11,conf[1][0].get())
	modificar(srcS,12,conf[1][1].get())
	modificar(srcS,13,conf[1][2].get())
	modificar(srcS,14,conf[1][3].get())
	modificar(srcS,15,conf[1][4].get())
	modificar(srcS,16,conf[1][5].get())
	modificar(srcS,17,conf[1][6].get())
	modificar(srcS,20,conf[2][0].get())
	modificar(srcS,23,conf[3][0].get())
	modificar(srcS,26,conf[4][0].get())
	Reload()
	WConfig.destroy
	pass


#Labels Flanges
LFlanges=Label(WConfig, text="Pestañas").grid(column=0,row=0)
LFlange1=Label(WConfig, text="Pestaña 1").grid(column=1,row=1)
LFlange1N=Label(WConfig, text="Nombre").grid(column=1,row=2)
LFlange1C=Label(WConfig, text="Color").grid(column=1,row=3)
LFlange2=Label(WConfig, text="Pestaña 2").grid(column=1,row=4)
LFlange2N=Label(WConfig, text="Nombre").grid(column=1,row=5)
LFlange2C=Label(WConfig, text="Color").grid(column=1,row=6)
LFlange3=Label(WConfig, text="Pestaña 3").grid(column=1,row=7)
LFlange3N=Label(WConfig, text="Nombre").grid(column=1,row=8)
LFlange3C=Label(WConfig, text="Color").grid(column=1,row=9)
LFlange4=Label(WConfig, text="Pestaña 4").grid(column=1,row=10)
LFlange4N=Label(WConfig, text="Nombre").grid(column=1,row=11)
LFlange4C=Label(WConfig, text="Color").grid(column=1,row=12)
LFlange5=Label(WConfig, text="Pestaña 5").grid(column=1,row=13)
LFlange5N=Label(WConfig, text="Nombre").grid(column=1,row=14)
LFlange5C=Label(WConfig, text="Color").grid(column=1,row=15)
LFlange6=Label(WConfig, text="Pestaña 6").grid(column=1,row=16)
LFlange6N=Label(WConfig, text="Nombre").grid(column=1,row=17)
LFlange6C=Label(WConfig, text="Color").grid(column=1,row=18)
LFlange7=Label(WConfig, text="Pestaña 7").grid(column=1,row=19)
LFlange7N=Label(WConfig, text="Nombre").grid(column=1,row=20)
LFlange7C=Label(WConfig, text="Color").grid(column=1,row=21)
#TextBoxes Flanges
TxtFlange1N=Entry(WConfig);TxtFlange1N.grid(column=2,row=2);TxtFlange1N.insert(0,Obtain(srcConfig,2))
TxtFlange2N=Entry(WConfig);TxtFlange2N.grid(column=2,row=5);TxtFlange2N.insert(0,Obtain(srcConfig,3))
TxtFlange3N=Entry(WConfig);TxtFlange3N.grid(column=2,row=8);TxtFlange3N.insert(0,Obtain(srcConfig,4))
TxtFlange4N=Entry(WConfig);TxtFlange4N.grid(column=2,row=11);TxtFlange4N.insert(0,Obtain(srcConfig,5))
TxtFlange5N=Entry(WConfig);TxtFlange5N.grid(column=2,row=14);TxtFlange5N.insert(0,Obtain(srcConfig,6))
TxtFlange6N=Entry(WConfig);TxtFlange6N.grid(column=2,row=17);TxtFlange6N.insert(0,Obtain(srcConfig,7))
TxtFlange7N=Entry(WConfig);TxtFlange7N.grid(column=2,row=20);TxtFlange7N.insert(0,Obtain(srcConfig,8))
TxtFlange1C=Entry(WConfig);TxtFlange1C.grid(column=2,row=3);TxtFlange1C.insert(0,Obtain(srcConfig,11))
TxtFlange2C=Entry(WConfig);TxtFlange2C.grid(column=2,row=6);TxtFlange2C.insert(0,Obtain(srcConfig,12))
TxtFlange3C=Entry(WConfig);TxtFlange3C.grid(column=2,row=9);TxtFlange3C.insert(0,Obtain(srcConfig,13))
TxtFlange4C=Entry(WConfig);TxtFlange4C.grid(column=2,row=12);TxtFlange4C.insert(0,Obtain(srcConfig,14))
TxtFlange5C=Entry(WConfig);TxtFlange5C.grid(column=2,row=15);TxtFlange5C.insert(0,Obtain(srcConfig,15))
TxtFlange6C=Entry(WConfig);TxtFlange6C.grid(column=2,row=18);TxtFlange6C.insert(0,Obtain(srcConfig,16))
TxtFlange7C=Entry(WConfig);TxtFlange7C.grid(column=2,row=21);TxtFlange7C.insert(0,Obtain(srcConfig,17))
#Blanco
Space1=Label(WConfig, text=" ").grid(column=0,row=22)
#Text Back
LTBack=Label(WConfig, text="Fondo del Texto").grid(column=0,row=23)
TxtTBack=Entry(WConfig);TxtTBack.grid(column=1,row=24);TxtTBack.insert(0,Obtain(srcConfig,20))
#Blanco
Space2=Label(WConfig, text=" ").grid(column=0,row=25)
#Source Color
LSColor=Label(WConfig, text="Color").grid(column=0,row=26)
TxtSColor=Entry(WConfig);TxtSColor.grid(column=1,row=27);TxtSColor.insert(0,Obtain(srcConfig,23))
#Blanco
Space3=Label(WConfig, text=" ").grid(column=0,row=28)
#System
LSystem=Label(WConfig, text="Color").grid(column=0,row=29)
TxtSystem=Entry(WConfig);TxtSystem.grid(column=1,row=30);TxtSystem.insert(0,Obtain(srcConfig,26))
#Blanco
Space4=Label(WConfig, text=" ").grid(column=0,row=31)
#Boton Final
EndConfiguration=Button(WConfig,text="Terminar",command=lambda:EndConfigure(srcConfig)).grid(column=3,row=32)

WConfig.mainloop();