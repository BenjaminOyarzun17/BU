import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import statistics
from scipy.optimize import curve_fit

a51 = pd.read_csv("5.1.csv",sep=';',header=0, decimal=",")  
a52 = pd.read_csv('5.2.csv',sep=';',header=0, decimal=",")     
a53 = pd.read_csv('5.3.csv',sep=';',header=0, decimal=",")     
a61 = pd.read_csv('6.1.csv',sep=';',header=0, decimal=",")   
a62 = pd.read_csv('6.2.csv',sep=';',header=0, decimal=",")   
a63 = pd.read_csv('6.3.csv',sep=';',header=0, decimal=",")    
a71 = pd.read_csv('7.1.csv',sep=';',header=0, decimal=",")  
a72 = pd.read_csv('7.2.csv',sep=';',header=0, decimal=",")   
a73 = pd.read_csv('7.3.csv',sep=';',header=0, decimal=",")   
a81 = pd.read_csv('8.1.csv',sep=';',header=0, decimal=",")   
a82 = pd.read_csv('8.2.csv',sep=';',header=0, decimal=",")     
a83 = pd.read_csv('8.3.csv',sep=';',header=0, decimal=",")
a91 = pd.read_csv('9.1.csv',sep=';',header=0, decimal=",")
a92 = pd.read_csv('9.2.csv',sep=';',header=0, decimal=",")
a93 = pd.read_csv('9.3EDITAR.csv',sep=';',header=0, decimal=",")
a101 = pd.read_csv('10.1.csv',sep=';',header=0, decimal=",")
a102 = pd.read_csv('10.2.csv',sep=';',header=0, decimal=",")
a103 = pd.read_csv('10.3.csv',sep=';',header=0, decimal=",")
a111 = pd.read_csv('11.1.csv',sep=';',header=0, decimal=",")
a112 = pd.read_csv('11.2.csv',sep=';',header=0, decimal=",")
a113 = pd.read_csv('11.3.csv',sep=';',header=0, decimal=",")
a121 = pd.read_csv('12.1.csv',sep=';',header=0, decimal=",")
a122 = pd.read_csv('12.2.csv',sep=';',header=0, decimal=",")
a123 = pd.read_csv('12.3.csv',sep=';',header=0, decimal=",")



datos = [a51,a52,a53,a61,a62,a63,a71,a72,a73,a81,a82,a83,a91,a92,a93,a101,a102,a103,a111,a112,a113,a121,a122,a123]
for i in datos:
    i.columns =  ['tiempo','v1']  
    

    
    
columnaTiempo = a51['tiempo']    
columnaTiempo = columnaTiempo.to_frame()
    
    
a101 = a101[a101.tiempo%5==0]
a122 = a122[a122.tiempo%5==0]
a101 = a101.reset_index(drop= True)

a122= a122.reset_index(drop= True)

ph5=a51
ph5.insert(2,'v2',a52.v1)
ph5.insert(3,'v3',a53.v1)
 

ph5= ph5.drop(columns = 'tiempo')
ph5['promedio']= ph5.mean(axis = 1)
ph5['desv']= ph5.drop(columns = 'promedio').std(axis =1)

print(ph5.head())


ph6=a61
ph6.insert(2,'v2',a62.v1)
ph6.insert(3,'v3',a63.v1)
#print(ph5.head())
ph6= ph6.drop(columns = 'tiempo')
ph6['promedio']= ph6.mean(axis = 1)
ph6['desv']= ph6.drop(columns = 'promedio').std(axis =1) 

ph7=a71
ph7.insert(2,'v2',a72.v1)
ph7.insert(3,'v3',a73.v1)
#print(ph5.head())
ph7= ph7.drop(columns = 'tiempo')
ph7['promedio']= ph7.mean(axis = 1)
ph7['desv']= ph7.drop(columns = 'promedio').std(axis =1)

ph8=a81
ph8.insert(2,'v2',a82.v1)
ph8.insert(3,'v3',a83.v1)
#print(ph5.head())
ph8= ph8.drop(columns = 'tiempo')
ph8['promedio']= ph8.mean(axis = 1)
ph8['desv']= ph8.drop(columns = 'promedio').std(axis =1)

ph9=a91
ph9.insert(2,'v2',a92.v1)
ph9.insert(3,'v3',a93.v1)
#print(ph5.head())
ph9= ph9.drop(columns = 'tiempo')
ph9['promedio']= ph9.mean(axis = 1)
ph9['desv']= ph9.drop(columns = 'promedio').std(axis =1)


ph10=a101
ph10.insert(2,'v2',a102.v1)
ph10.insert(3,'v3',a103.v1)
#print(ph5.head())
ph10= ph10.drop(columns = 'tiempo')
ph10['promedio']= ph10.mean(axis = 1)
ph10['desv']= ph10.drop(columns = 'promedio').std(axis =1)


ph11=a111
ph11.insert(2,'v2',a112.v1)
ph11.insert(3,'v3',a113.v1)
#print(ph5.head())
ph11= ph11.drop(columns = 'tiempo')
ph11['promedio']= ph11.mean(axis = 1)
ph11['desv']= ph11.drop(columns = 'promedio').std(axis =1)


ph12=a121
ph12.insert(2,'v2',a122.v1)
ph12.insert(3,'v3',a123.v1)
#print(ph5.head())
ph12= ph12.drop(columns = 'tiempo')
ph12['promedio']= ph12.mean(axis = 1)
ph12['desv']= ph12.drop(columns = 'promedio').std(axis =1)


ph5.insert(5, 'tiempo', columnaTiempo.tiempo)
ph6.insert(5, 'tiempo', columnaTiempo.tiempo)
ph7.insert(5, 'tiempo', columnaTiempo.tiempo)
ph8.insert(5, 'tiempo', columnaTiempo.tiempo)
ph9.insert(5, 'tiempo', columnaTiempo.tiempo)
ph10.insert(5, 'tiempo', columnaTiempo.tiempo)
ph11.insert(5, 'tiempo', columnaTiempo.tiempo)
ph12.insert(5, 'tiempo', columnaTiempo.tiempo)


def graf2(ph, num):
    n= len(ph8.tiempo)
    data[f'ph{num}']= ph.promedio
    

def mostrarGrafs(lista):
    j=5
    for i in lista:
        print(j) 
        graf2(i,j)
        j+=1


def obtenerVelocidadPromedio(dfRegresiones,listaVelocidades):
    j = 5
    for i in range(7):
        listaVelocidades.append((f'ph{j}', (dfRegresiones.iloc[120][i]-dfRegresiones.iloc[0][i])/600))
        
        j+=1
    return listaVelocidades        
        
    
        


listapH=[ph5,ph6,ph7,ph8,ph9,ph10,ph11]
listaVelocidades=[]
data={}





mostrarGrafs(listapH)  
miPh= pd.DataFrame(data=data)
print(miPh.head())

listaVelocidades = obtenerVelocidadPromedio(miPh, listaVelocidades)

phs = []
velocidades = []
for i in range(7):
    phs.append(listaVelocidades[i][0])
    velocidades.append(listaVelocidades[i][1])

print(listaVelocidades)


fig, ax = plt.subplots()
ax.plot(phs, velocidades)
ax.set_xlabel(f'Zeit (Sek)')
ax.set_ylabel('Reaktionsgeschwindigkeit (kPa/Sek)')
ax.set_title(f'durchschnittliche Reaktionsgeschwindigket pro pH Wert')

