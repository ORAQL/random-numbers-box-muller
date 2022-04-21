#Integrantes
#Kenneth Martinez
#Oscar Quesedo

from openpyxl import Workbook
from math import *
import numpy as np1
import os

book = Workbook()
sheet = book.active
i=1 #Variable para controlar filas en Excel

mixto = [] #contiene todos los valores generados por metodo mixto 
noMixto = [] #contiene todos los valores generados mixto sin validar
multiplicativo = [] #contiene todos los valores generados por metodo multiplicativo
noMultiplicativo = [] #contiene todos los valores generados multiplicativo sin validar

#VALIDACIONES
#validacion de primo
def esPrimo(x):
    for n in range(2, x):
        if x % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

def mMixto(x, a, c, m):

    global i
    i += 2 
    num = 1
    v = 0
    numeroNoValido = True
    stop = x

    pausa = 0

    #validamos X     
    if x < 0:
        print("x es negativo")
        numeroNoValido = False

    # validacion de a
    if numeroNoValido:
        primos = []
        n = m
        for g in range(2, n + 1):
            while n % g == 0:
                primos.append(g)
                n = n / g
            if n == g:
                break
        for g in range(1, len(primos)):
            if (a - 1) % g != 0:
                numeroNoValido = False
                print("a no es valido")
    
    #validacion de m
    for n in range(2, m):
        if m % n == 0:
            print("m No es primo")
            numeroNoValido = False
            
    #validacion de c
    v = float(c%8)
    if v!=5:
        print("c no es un entero impar primo relativo de m 1")
        numeroNoValido = False
    elif v.is_integer()==False:
        print("c no es un entero impar primo relativo de m 2")
        numeroNoValido = False
    elif v%2==0:
        print("c no es un entero impar primo relativo de m 3")
        numeroNoValido = False

    # mostramos los numero aleatorios en el rango de (0 a 1]
    if (numeroNoValido):
        pararCiclo = True
        sheet[f'G{i}'] = 'muixto validado'
        while (pararCiclo):
            a2 = a * x + c
            x = a2 % m
            resp = x / m

            if len(noMixto) > 2:
                if x == pausa:
                    print("---------------", x, "--", pausa)
                    break

            mixto.append(resp) #mixto[]
            print("No: ", num, "x: ", x, "|a: ", a2, "|c: ", c, "|m: ", m, "|Valor aleatorio: ", resp)
            i += 1
            num += 1

            sheet[f'A{i}'] = i
            sheet[f'B{i}'] = x
            sheet[f'C{i}'] = a2
            sheet[f'D{i}'] = c
            sheet[f'E{i}'] = m
            sheet[f'F{i}'] = resp

            if v == 1:
                pausa = x
            v += 1

            if (stop == x):
                print("datos guardados")
                break

        else:
            print("un numero no cumple con lo requerido")

def mMixtoNoComprobado(x, a, c, m):

    global i
    i += 2
    num = 1
    v = 0
    stop = x

    pararCiclo = True

    sheet[f'G{i}'] = 'mixto no validado'

    pausa = 0

    while (pararCiclo):

        a2 = a * x + c
        x = a2 % m
        resp = x / m

        if len(noMixto) > 2:
            if x == pausa:
                print("---------------", x, "--", pausa)
                break

        noMixto.append(resp)
        print("No: ", num, "x: ", x, "|a: ", a2, "|c: ", c, "|m: ", m, "|Valor aleatorio: ", resp)
        i += 1
        num += 1
        sheet[f'A{i}'] = i
        sheet[f'B{i}'] = x
        sheet[f'C{i}'] = a2
        sheet[f'D{i}'] = c
        sheet[f'E{i}'] = m
        sheet[f'F{i}'] = resp

        if v==1:
            pausa=x
        v += 1

        if (stop == x):
            print("datos guardados")
            pararCiclo = False

def mMultiplicativo(x, a, c, m):

    global i
    i += 2
    num = 1
    v = 0
    numeroNoValido = True
    stop = x

    pausa = 0

    #valodando semilla, si es primo relativo 
    count = 0
    ñ = []
    z = []
    
    for i in range(1, x+1):
        if(x%i == 0):
            ñ.append(i)
            print(i)
    
    for j in range(1, m+1):
        if(m%j == 0):
            z.append(j)
            print(j)
    
    for k in range(len(ñ)):
        for h in range(len(z)):
            if (ñ[k] == z[h]):
                count += 1
            if (count >= 2):
                print("La semilla no es primo relativo de m.")
                #numNull = False
                break

    # entra a validar
    else:
        # validacion de que si m es o no primo
        for g in range(2, m):
            if m % g == 0:
                numeroNoValido = False
                print("m no es primo")
                break

    # mostramos los numero aleatorios en el rango de (0 a 1]
    if numeroNoValido:
        pararCiclo = True
        sheet[f'G{i}'] = 'multiplicativo validado'
        while (pararCiclo):
            a2 = a * x
            x = a2 % m
            resp = x / m
            multiplicativo.append(resp)
            print("No: ", num, "x: ", x, "|a: ", a2, "|m: ", m, "|Valor aleatorio: ", resp)
            i += 1
            num += 1

            if len(noMixto) > 2:
                if x == pausa:
                    print("---------------", x, "--", pausa)
                    break

            sheet[f'A{i}'] = i
            sheet[f'B{i}'] = x
            sheet[f'C{i}'] = a2
            sheet[f'D{i}'] = m
            sheet[f'E{i}'] = resp

            if v == 1:
                pausa = x
            v += 1

            if (stop == x):
                print("datos guardados")
                pararCiclo = False
    else:
        print("un numero no cumple con lo requerido")

def mMultiplicativoNoComprobado(x, a, c, m):

    global i
    i += 2
    num = 1
    v = 0
    stop=x

    pausa = 0

    pararCiclo = True

    sheet[f'G{i}']='multiplicativo no validado nuevo'

    while(pararCiclo):
        a2 = a*x
        x = a2 % m
        resp = x/m
        noMultiplicativo.append(resp)
        print("No: ", num,"x: ", x, "|a: ", a2, "|m: ", m, "|Valor aleatorio: ", resp)
        i += 1
        num += 1

        if len(noMixto) > 2:
            if x == pausa:
                print("---------------", x, "--", pausa)
                break

        sheet[f'A{i}']= i
        sheet[f'B{i}']= x
        sheet[f'C{i}']= a2
        sheet[f'D{i}']= m
        sheet[f'E{i}']= resp

        if v==1:
            pausa=x
        v += 1

        if(stop==x):
            print("datos guardados")
            pararCiclo = False

#DISTRIBUCIONES
#---------------------------------------------variables aleatorias uniformes--------------------------------------------------------------

#NUMA seran los numeros aleatorios que se van a escoger para hacer el ejercicio
def VAU_Exponencial(NUMA, l):
    #se captura el valor de lamda 
    lamda = l

    if(NUMA == 1):
        global mixto
        metodo = mixto
    elif(NUMA == 2):
        global noMixto
        metodo = noMixto
    elif(NUMA == 3):
        global multiplicativo
        metodo = multiplicativo
    elif(NUMA == 4):
        global noMultiplicativo
        metodo = noMultiplicativo

    V_expo = []

    for i in range(len(metodo)):
        valor = abs(lamda*log(metodo[i]))
        V_expo.append(valor)

    print("EXPONENCIAL")
    print(V_expo)

    V_expo_i =[]
    for i in range(len(V_expo)):
        inversa = (log(1-metodo[i]))/(-lamda)
        V_expo_i.append(inversa)

    print("EXPONENCIAL INVERSA")
    print(V_expo_i)
    
    print("-----------------------------------------\n\n")
    
def VAU_Poison(NUMA, l, x):
    #se captura el valor de lamda 
    lamda = l #media
    var_x = x

    if(NUMA == 1):
        global mixto
        metodo = mixto
    elif(NUMA == 2):
        global noMixto
        metodo = noMixto
    elif(NUMA == 3):
        global multiplicativo
        metodo = multiplicativo
    elif(NUMA == 4):
        global noMultiplicativo
        metodo = noMultiplicativo

    Valores_x = []
    poison = 0
    for i in range(var_x):
        poison = poison + ((exp(1)**-lamda)*(lamda**i))/(factorial(i))
        Valores_x.append(poison)
    print("VALORES DE X: ", Valores_x)

    #comparacion de valores
    V_poison = []
    for i in range(len(metodo)):
        for b in range(var_x):
            if metodo[i] < Valores_x[b]:
                V_poison.append(b)
                break
    print("DSITRIBUCION DE POISON: \n", V_poison)

#NUMA seran los numeros aleatorios que se van a escoger para hacer el ejercicio
def VAU_Normal(NUMA, n, o):

    if(NUMA == 1):
        global mixto
        metodo = mixto
    elif(NUMA == 2):
        global noMixto
        metodo = noMixto
    elif(NUMA == 3):
        global multiplicativo
        metodo = multiplicativo
    elif(NUMA == 4):
        global noMultiplicativo
        metodo = noMultiplicativo

    niu = n
    opsilon = o
    #generamos la variable aleatoria
    V_nor = []
    for i in range(2, len(metodo)):
        if i+1>len(metodo):
            break
        variable1 = (sqrt(-2*np.log(metodo[i-1])))*(np.cos(2*np.pi*metodo[i]))
        V_nor.append(variable1)
        variable2 = (sqrt(-2*np.log(metodo[i-1])))*(np.sin(2*np.pi*metodo[i]))
        V_nor.append(variable2)
    print(V_nor)
    for i in range(len(metodo)):
        V_nor[i] = niu+opsilon*V_nor[i]
    print("DISTRIBUCION NORMAL: \n")
    print(V_nor)
    
    print("DISTRIBUCION NORMAL INVERSA: ")
    V_nor_i =[]
    for i in range(len(V_nor)):
        inversa = log(1-metodo[i])**2
        V_nor_i.append(inversa)
    print(V_nor_i)

#---------------------------------------------------------------main-----------------------------------------------------------------------
condicion = True
condicion2 = True
while condicion:
    print(mixto)
    print(noMixto)
    print(multiplicativo)
    print(noMultiplicativo)
    print("---------------------------")
    num1 = int(input("1. ingresar datos para obtener numeros pseudoaleatorios \n2. Realizar distribucion \n3. salir \ningresar: "))
    if (num1 == 1):
        print("-------------------------------------------------------")
        var1 = int(input("   1. metodo mixto \n   2. metodo mixto no validado  \n   3. metodo multiplicativo \n   4. metodo multiplicativo no validado \n :"))
        while condicion2:
            x = float(input("digite valor de (x): "))
            a = float(input("digite valor de (a): "))
            c = float(input("digite valor de (c): "))
            m = float(input("digite valor de (m): "))

            #metodos
            switch_metodo = {
                1: mMixto,
                2: mMixtoNoComprobado,
                3: mMultiplicativo,
                4: mMultiplicativoNoComprobado
            }

            #llamo a la var1 y le paso por parametros los valores de x, a, c, m.
            if x.is_integer()==False or a.is_integer()==False or c.is_integer()==False or m.is_integer()==False:
                print("algun valor digitado no es entero")

            elif m<=x or m<=a or m<=c:
                print("algun valor digitado es mayor a M ")

            elif x<=0 or a<=0 or c<=0 or m<=0:
                print("algun valor es igual o menor a cero (negativo)")

            else:
                x = int(x)
                a = int(a)
                c = int(c)
                m = int(m)
                switch_metodo.get(var1)(x, a, c, m)
                break
    
    elif (num1 == 2):
        print("------------------DISTRIBUCIONES-----------------")
        var4 = int(input("Seleccione Distribucion: \n1. Exponencial \n2. Poison \n3. Normal \n seleccion: "))
        var5 = int(input("Elija su metodo\n   1. mixto\n   2. mixto no comprobado\n   3. multiplicativo\n   4. multiplicativo no comporbado \n: "))
        if (var4>=1 or var4<=3):
            switch_Distribucion = {
                1: VAU_Exponencial,
                2: VAU_Poison,
                3: VAU_Normal
            }
            if var4 == 1:
                lamda1 = float(input("Digite el valor de lamda: "))
                switch_Distribucion.get(var4)(var5, lamda1)
            elif var4 == 2:
                lamda2 = float(input("Digite el valor de lamda: "))
                x1 = int(input("valor de x: "))
                switch_Distribucion.get(var4)(var5, lamda2, x1)
            elif var4 == 3:
                niu = float(input("niu: "))
                opsilon = float(input("opsilon: "))
                switch_Distribucion.get(var4)(var5, niu, opsilon)
        else:
            print("numero fuera de rando")

    elif (num1 == 3):
        book.save('EJERCICIO DISTRIBUCIONES.XLSX')
        print("se ha generado el documnto excel en la \ncarpeta donde se encuentra el programa")
        break

    else:
        print("un numero digitado no esta en el rango")
    
