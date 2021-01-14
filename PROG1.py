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



coef5 = np.polyfit(ph5.tiempo, ph5.promedio, 1)
poly1d_fn = np.poly1d(coef5) 

fig, ax = plt.subplots()
ax.plot(ph5.tiempo, ph5.promedio, label = 'Durchschnitt')
ax.errorbar(ph5.tiempo,ph5.promedio,ph5.desv)

ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.legend()
ax.set_title('ph 5')

coef5 = np.polyfit(ph5.tiempo, ph5.promedio, 1)
poly1d_fn = np.poly1d(coef5) 

fig, ax = plt.subplots()
ax.plot(ph5.tiempo, ph5.v1, label = 'Versuch 1')
ax.plot(ph5.tiempo, ph5.v2, label = 'Versuch 2')
ax.plot(ph5.tiempo, ph5.v3, label = 'Versuch 3')
ax.plot(ph5.tiempo, ph5.promedio, label = 'Durchschnitt')
ax.plot(ph5.tiempo, poly1d_fn(ph5.tiempo), label ='regresion')



ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.legend()
ax.set_title('ph 5')


coef6 = np.polyfit(ph6.tiempo, ph6.promedio, 1)
poly1d_fn = np.poly1d(coef6) 

fig, ax = plt.subplots()

ax.plot(ph6.tiempo, ph6.promedio, label = 'Durchschnitt')
ax.errorbar(ph6.tiempo,ph6.promedio,ph6.desv)

ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.legend()
ax.set_title('ph 6')

coef6 = np.polyfit(ph6.tiempo, ph6.promedio, 1)
poly1d_fn = np.poly1d(coef6) 

fig, ax = plt.subplots()
ax.plot(ph6.tiempo, ph6.v1, label = 'Versuch 1')
ax.plot(ph6.tiempo, ph6.v2, label = 'Versuch 2')
ax.plot(ph6.tiempo, ph6.v3, label = 'Versuch 3')
ax.plot(ph6.tiempo, ph6.promedio, label = 'Durchschnitt')
ax.plot(ph6.tiempo, poly1d_fn(ph6.tiempo), label ='regresion')

ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.legend()
ax.set_title('ph 6')


coef7 = np.polyfit(ph7.tiempo, ph7.promedio, 1)
poly1d_fn = np.poly1d(coef7) 

fig, ax = plt.subplots()

ax.plot(ph7.tiempo, ph7.promedio, label = 'Durchschnitt')
ax.errorbar(ph7.tiempo,ph7.promedio,ph7.desv)


ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.set_title('ph 7')
ax.legend()


coef7 = np.polyfit(ph7.tiempo, ph7.promedio, 1)
poly1d_fn = np.poly1d(coef7) 

fig, ax = plt.subplots()
ax.plot(ph7.tiempo, ph7.v1, label = 'Versuch 1')
ax.plot(ph7.tiempo, ph7.v2, label = 'Versuch 2')
ax.plot(ph7.tiempo, ph7.v3, label = 'Versuch 3')
ax.plot(ph7.tiempo, ph7.promedio, label = 'Durchschnitt')

ax.plot(ph7.tiempo, poly1d_fn(ph7.tiempo), label ='regresion')

ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.set_title('ph 7')
ax.legend()


coef8 = np.polyfit(ph8.tiempo, ph8.promedio, 1)
poly1d_fn = np.poly1d(coef8) 

fig, ax = plt.subplots()

ax.plot(ph8.tiempo, ph8.promedio, label = 'Durchschnitt')
ax.errorbar(ph8.tiempo,ph8.promedio,ph8.desv)


ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.set_title('ph 8')
ax.legend()
coef8 = np.polyfit(ph8.tiempo, ph8.promedio, 1)
poly1d_fn = np.poly1d(coef8) 

fig, ax = plt.subplots()
ax.plot(ph8.tiempo, ph8.v1, label = 'Versuch 1')
ax.plot(ph8.tiempo, ph8.v2, label = 'Versuch 2')
ax.plot(ph8.tiempo, ph8.v3, label = 'Versuch 3')
ax.plot(ph8.tiempo, ph8.promedio, label = 'Durchschnitt')

ax.plot(ph8.tiempo, poly1d_fn(ph8.tiempo), label ='regresion')

ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.set_title('ph 8')
ax.legend()



coef9 = np.polyfit(ph9.tiempo, ph9.promedio, 1)
poly1d_fn = np.poly1d(coef9) 

fig, ax = plt.subplots()

ax.plot(ph9.tiempo, ph9.promedio, label = 'Durchschnitt')
ax.errorbar(ph9.tiempo,ph9.promedio,ph9.desv)

ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.set_title('ph 9')
ax.legend()
coef9 = np.polyfit(ph9.tiempo, ph9.promedio, 1)
poly1d_fn = np.poly1d(coef9) 

fig, ax = plt.subplots()
ax.plot(ph9.tiempo, ph9.v1, label = 'Versuch 1')
ax.plot(ph9.tiempo, ph9.v2, label = 'Versuch 2')
ax.plot(ph9.tiempo, ph9.v3, label = 'Versuch 3')
ax.plot(ph9.tiempo, ph9.promedio, label = 'Durchschnitt')
ax.plot(ph9.tiempo, poly1d_fn(ph9.tiempo), label ='regresion')

ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.set_title('ph 9')
ax.legend()



coef10 = np.polyfit(ph10.tiempo, ph10.promedio, 1)
poly1d_fn = np.poly1d(coef10) 


fig, ax = plt.subplots()

ax.plot(ph10.tiempo, ph10.promedio, label = 'Durchschnitt')
ax.errorbar(ph10.tiempo,ph10.promedio,ph10.desv)

ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.set_title('ph 10')
ax.legend()
coef10 = np.polyfit(ph10.tiempo, ph10.promedio, 1)
poly1d_fn = np.poly1d(coef10) 


fig, ax = plt.subplots()
ax.plot(ph10.tiempo, ph10.v1, label = 'Versuch 1')
ax.plot(ph10.tiempo, ph10.v2, label = 'Versuch 2')
ax.plot(ph10.tiempo, ph10.v3, label = 'Versuch 3')
ax.plot(ph10.tiempo, ph10.promedio, label = 'Durchschnitt')
ax.plot(ph10.tiempo, poly1d_fn(ph10.tiempo), label ='regresion')

ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.set_title('ph 10')
ax.legend()




coef = np.polyfit(ph11.tiempo, ph11.promedio, 1)
poly1d_fn = np.poly1d(coef) 

fig, ax = plt.subplots()

ax.plot(ph11.tiempo, ph11.promedio, label = 'Durchschnitt')
#ax.scatter(ph11.tiempo,pred)
ax.errorbar(ph11.tiempo,ph11.promedio,ph11.desv)

ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.set_title('ph 11')
ax.legend()

coef = np.polyfit(ph11.tiempo, ph11.promedio, 1)
poly1d_fn = np.poly1d(coef) 

fig, ax = plt.subplots()
ax.plot(ph11.tiempo, ph11.v1, label = 'Versuch 1')
ax.plot(ph11.tiempo, ph11.v2, label = 'Versuch 2')
ax.plot(ph11.tiempo, ph11.v3, label = 'Versuch 3')
ax.plot(ph11.tiempo, ph11.promedio, label = 'Durchschnitt')
ax.plot(ph11.tiempo, poly1d_fn(ph11.tiempo), label ='regresion')
#ax.scatter(ph11.tiempo,pred)

ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')
ax.set_title('ph 11')
ax.legend()



coef12 = np.polyfit(ph12.tiempo, ph12.promedio, 1)
poly1d_fn = np.poly1d(coef12) 

fig, ax = plt.subplots()

ax.plot(ph12.tiempo, ph12.promedio, label = 'Durchschnitt')
ax.errorbar(ph12.tiempo,ph12.promedio,ph12.desv)

ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')

ax.set_title('ph 12')
ax.legend()


coef12 = np.polyfit(ph12.tiempo, ph12.promedio, 1)
poly1d_fn = np.poly1d(coef12) 

fig, ax = plt.subplots()
ax.plot(ph12.tiempo, ph12.v1, label = 'Versuch 1')
ax.plot(ph12.tiempo, ph12.v2, label = 'Versuch 2')
ax.plot(ph12.tiempo, ph12.v3, label = 'Versuch 3')
ax.plot(ph12.tiempo, ph12.promedio, label = 'Durchschnitt')
ax.plot(ph12.tiempo, poly1d_fn(ph12.tiempo), label ='regresion')

ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Druck (kPa)')

ax.set_title('ph 12')
ax.legend()


pendientes = [[coef12[0],'ph12'],[coef[0],'ph11'],[coef10[0],'ph10'],
              [coef9[0],'ph9'],[coef8[0],'ph8'],[coef7[0],'ph7'],
              [coef6[0],'ph6'],[coef5[0],'ph5']]

