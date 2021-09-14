# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:21:12 2020

@author: Cesar Ricardo
"""

import math
import numpy as np
from matplotlib import pyplot as plt

#Busca la componente mas grande de los puntos 
def Escala_Grafica(A,n):
    maximo=[]
    for i in range(n):
        for j in range(2):
            maximo.append(A[i][j])
    maxcs=sorted(maximo)    
    escala=maxcs[len(maxcs)-1]    
    
    return escala

    

def Encontrar_Punto_Maximo(z,Puntos_Extremo,numPuntos_Extremo):
    Z=[]
    aux1=[]
    if numPuntos_Extremo==0:
        return False,0
    for i in range(numPuntos_Extremo):
        aux=[]
        Z.append((z[0]*Puntos_Extremo[i][0])+(z[1]*Puntos_Extremo[i][1]))
        aux.append(i)
        aux.append(Z[i])
        aux1.append(aux)    
       
    cs = sorted(Z)
    for i in range(numPuntos_Extremo):
        if cs[numPuntos_Extremo-1] == aux1[i][1]:
            
            break
    print(cs[numPuntos_Extremo-1])
    
    return cs[numPuntos_Extremo-1],aux1[i][0];

def Encontrar_Punto_Minimo(z,Puntos_Extremo,numPuntos_Extremo):
    Z=[]
    aux1=[]
    if numPuntos_Extremo==0:
        return False,0
    for i in range(numPuntos_Extremo):
        aux=[]
        Z.append((z[0]*Puntos_Extremo[i][0])+(z[1]*Puntos_Extremo[i][1]))
        aux.append(i)
        aux.append(Z[i])
        aux1.append(aux)
       
    cs = sorted(Z)
    for i in range(numPuntos_Extremo):
        if cs[0] == aux1[i][1]:
            break
    
    return cs[0],i
    
def Encontrar_Puntos(m,b,n):
    Puntos=[]
    numPuntos=0
    for i in range(n):
        if math.isinf(m[i]):
            
            for j in range(n):
                if m[i]!=m[j]:
                    if Puntos.count([b[i],(b[i]*m[j])+b[j]])==0 & math.isnan((b[i]*m[j])+b[j]) == False:
                        Puntos.append([b[i],(b[i]*m[j])+b[j]])
                        numPuntos=numPuntos+1
        else:
            for j in range(n-i-1):
                if m[i]!=m[j+i] :
                    Punto_x =(b[j+i]-b[i])/(m[i]-m[j+i])
                    Punto_y = (Punto_x*m[j+i])+b[j+i]
                    
                    if Puntos.count([b[i],(b[i]*m[j])+b[j]])==0:
                        print(math.isnan(Punto_y))
                        Puntos.append([Punto_x,Punto_y])
                        numPuntos=numPuntos+1      
    return Puntos,numPuntos

def Encontrar_Puntos_Extremo(Puntos, a1,a2, c, numPuntos, n):
    puntos_Extremos=[]
    numPuntos_Extremos=0
    cont=0
    for i in range(numPuntos):
        cont=0
        for j in range(n):
            if Puntos[i][0] < -0 or Puntos[i][1] < -0 or math.isnan(Puntos[i][0]) or math.isnan(Puntos[i][1]):
                cont=cont+1
            else:
                if (a1[j]*Puntos[i][0])+(a2[j]*Puntos[i][1]) > c[j]:
                    cont=cont+1
        if cont==0:
            puntos_Extremos.append(Puntos[i])
            numPuntos_Extremos=numPuntos_Extremos+1
    puntos_Extremos.sort()            
    return puntos_Extremos,numPuntos_Extremos
   
def Metodo_Grafico(a,C,n,minimizar,z):

    m=[]
    b=[]
    y=[]
    A=[]
    a1=[]
    a2=[]
    c=[]
    for i in range(n):
        a1.append(a[i][0])
        a2.append(a[i][1])
        c.append(C[i])
    a1.append(0)
    a2.append(1)
    a1.append(0)
    a2.append(0)
    c.append(0)
    c.append(0)   
    for i in range(n+2):
        if a2[i] == 0:
            m.append(math.inf) 
            b.append( c[i])
            aux=[m[0],b[0]]
            A.append(aux)
        else:
            m.append(-a1[i]/a2[i]) 
            b.append(c[i]/a2[i])
            aux=[m[i],b[i]]
            A.append(aux)
            
    for i in range(n+2):
        x = np.linspace(0, Escala_Grafica(A,n), 100)#Arreglar Escala
        if(math.isinf(m[i])):
            y.append(m[i]*x)
        else:
            y.append(m[i]*x+b[i]) 
    Puntos, numPuntos=Encontrar_Puntos(m,b, n+2)
    fig, ax = plt.subplots() 
    for i in range(n+2):
        x = np.linspace(0,Escala_Grafica(A,n), 100)
        if a2[i]==0 :
            plt.axvline(x = b[i])
        else:
            plt.plot(x, y[i])
    
    plt.axvline(x = 0, color = "black")
    plt.axhline(y = 0, color = "black")
    for i in range(numPuntos):
        print(i,"Punto dibujado: ", Puntos[i])
        plt.plot(Puntos[i][0],Puntos[i][1],"yo")     
        
    Puntos_Extremo, numPuntos_Extremo = Encontrar_Puntos_Extremo(Puntos, a1,a2, c, numPuntos, n)
    print("Numero de puntos extremo: ", numPuntos_Extremo)
    xExtremos = []
    yExtremos = []
    for i in range(numPuntos_Extremo):
        xExtremos.append(Puntos_Extremo[i][0])
        yExtremos.append(Puntos_Extremo[i][1])
        plt.plot(Puntos_Extremo[i][0],Puntos_Extremo[i][1],"ro")
        
    ax.fill(xExtremos, yExtremos, facecolor='green')
    plt.ylim(0,Escala_Grafica(A,n))
    plt.xlim(0,Escala_Grafica(A,n))
    ax.set_facecolor('white')
    plt.grid()
    
    if minimizar==2:
        Funcion_Objetivo,Punto_Optiimo=Encontrar_Punto_Minimo(z, Puntos_Extremo, numPuntos_Extremo)
    else:
        Funcion_Objetivo,Punto_Optiimo=Encontrar_Punto_Maximo(z, Puntos_Extremo, numPuntos_Extremo)    
    
    if Funcion_Objetivo == False:
        return False,0
    plt.plot(Puntos_Extremo[Punto_Optiimo][0],Puntos_Extremo[Punto_Optiimo][1],"co")
    plt.text(Puntos_Extremo[Punto_Optiimo][0],Puntos_Extremo[Punto_Optiimo][1],"  Punto optimo")
    plt.title("Metodo Grafica")
    print("El punto optimo es:",Puntos_Extremo[Punto_Optiimo])
    print("El valor en el punto Optimo es:", Funcion_Objetivo )
    
   
    x = np.linspace(0,Escala_Grafica(A,n), 100)
    y=(-z[0]/z[1])*x+(Funcion_Objetivo/z[1])
    plt.plot(x,y, "--")    
    plt.savefig('foo.png')
    
    return Puntos_Extremo[Punto_Optiimo],Funcion_Objetivo

input
#a=np.array([[-1,-1],[2,-3],[1,2],[-3,1],[1,0],[0,-1]])#2xn
#c=np.array([-8,0,30,0,-10,-9])#1xn
#n=6;# numero de Restricciones
#minimizar=True;#Si es minimo = true, si es maximo = false
#z=[3,8]#Funcion Ob  jetivo

a=np.array([[6,4],[1,2],[-1,1],[0,1]])#2xn
c=np.array([24,6,1,2])#1xn
n=4;# numero de Restricciones
minimizar=False;#Si es minimo = true, si es maximo = false
z=[5,4]#Funcion Ob  jetivo

#a=np.array([[-1,-1],[0.2,-0.3],[1,0.01]])#2xn
#c=np.array([-800,0,0])#1xn
#n=3;# numero de Restricciones
#minimizar=False;#Si es minimo = true, si es maximo = false
#z=[0.3,0.9]#Funcion Ob  jetivo

#Output
#Punto Optimo [x,y]
#Valor de Z en punto Optimo
Punto_Optimo, Valor_Punto_Optimo = Metodo_Grafico(a, c, n, minimizar, z)