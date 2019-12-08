import pandas as pd
from math import *
import prettytable as ptt 
import numpy as np 
import matplotlib.pyplot as plt 
from prettytable import PrettyTable
Datos=pd.read_excel('DATOSDUDOSOS.xlsx')
Kn=2.279 		#>>>>>> KN (Nivel de significancia para la distribción)
def logaritmo(num):
	return log10(num)
Datos['LOGARITMO']=Datos['DATOS'].apply(logaritmo)
Cant_dat=Datos.shape
lista=[] 
datos=[]
anios=[]
for i in range(Cant_dat[0]):
	lista.append(Datos['LOGARITMO'][i])
	datos.append(Datos['DATOS'][i])
	anios.append(Datos['AÑO'][i])
lista=np.array(lista)
prom=sum(lista)/Cant_dat[0] 
cuadrados=[]
for i in range(Cant_dat[0]):
	r=(Datos['LOGARITMO'][i]-prom)**2
	cuadrados.append(r)
desv=(sum(cuadrados)/Cant_dat[0])**0.5
YH = prom + Kn*desv
QH = 10**YH
YL = prom - Kn*desv
QL = 10**YL
Datos['CONDICIÓN']=''
for i in range(Cant_dat[0]):
	if datos[i]>QH:
		Datos['CONDICIÓN'][i]='DATO DUDOSO MAYOR'
	if datos[i]<QL:
		Datos['CONDICIÓN'][i]='DATO DUDOSO MENOR'
Cond=[]
for i in range(Cant_dat[0]):
	Cond.append(Datos['CONDICIÓN'][i])
#=============== Resultado de caudales ===============#
print("Kn (",len(Datos),") datos:",Kn)
print("==================================")
print("Umbral MÁXIMO de Precip: ",round(QH,3))
print("Umbral MÍNIMO de Precip: ",round(QL,3))
#==================RESULTADO EN TABLA===============#
Table=PrettyTable(['Año','Precip.','CONDICIÓN'])
for i in range(len(Datos)):
    Table.add_row([anios[i],datos[i],Cond[i]])
print(Table)
#=============   Grafico de Datos ==================#
plt.plot(anios,datos,'b',label='Precipitación')
plt.plot(anios,datos,"og")
plt.plot([anios[0],anios[-1]],[QH,QH],'r--',label='Umbral Superior')
plt.plot([anios[0],anios[-1]],[QL,QL],'g--',label='Umbral Inferior')
plt.title("ANÁLISIS DE DATOS DUDOSOS °°°DAMIAN°°°")
plt.xlabel("Años")
plt.ylabel("Datos")
plt.legend()
plt.grid(True)
plt.show()

guard = pd.ExcelWriter('DATOSDUDOSOS.xlsx')
Datos.to_excel(guard,'DAT_DUD',index=False)
guard.save()
