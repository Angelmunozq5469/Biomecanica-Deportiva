from csv import excel
from operator import index
from pickle import FALSE, TRUE
from statistics import geometric_mean
from turtle import window_height
from unittest import result
import PySimpleGUI as py
import pandas as pd
import _tkinter as tk


py.theme("DarkTeal9")

Excel="datosbiomecanicos.xlsx"
df=pd.read_excel("datosbiomecanicos.xlsx")


vista=[
    [py.Text("INGRESE LA INFORMACION REQUERIDA ")],
    [py.Text("ID",size=(15,1)),py.InputText(key="ID")],
    [(py.Text("MASA TOTAL",size=(15,1)),py.InputText(key="MASA TOTAL"))],
    [py.Text("ACELERACION",size=(15,1)),py.InputText(key="ACELERACION")],
    [py.Text("VELOCIDAD",size=(15,1)),py.InputText(key="VELOCIDAD")],
    [py.Text("UBICACION",size=(15,1)),py.InputText(key="UBICACION")],
    [py.Text("UNIDADES",size=(15,1)),py.InputText(key="UNIDADES")],
    [py.Submit("Guardar"),py.Exit("Salir"),py.Button("Limpiar"),py.Button("Calcular"),py.Button("Resultado")]
]
ventana= py.Window("Biomecanica",vista)

##################FUNCIONES############################################

def guardar():

    df_GUARDAR=df.append(values,ignore_index=True)
    df_GUARDAR.to_excel(Excel, index=False)


def limpiar():
    for key in values:
        ventana[key]("")
    return None


def Calcular():

    Excel="datosbiomecanicos.xlsx"
    df=pd.read_excel("datosbiomecanicos.xlsx")

    df.set_index("ID",inplace=True)

    form=py.FlexForm("Math")

    layout = [ [py.Txt("Ingrese el ID: ")],
           [py.In(size=(8,1), key="Ind")],
           [py.Submit(),py.Exit("Cancelar")]]

    form.layout(layout)
    button,values=form.read()
    Ind=int(values["Ind"])
   
    aux=df["MASA TOTAL"]
    aux2=aux[Ind]
    valorfila1=float(aux2)
    
    aux1=df["ACELERACION"]
    aux3=aux1[Ind]
    valorfila2=float(aux3)
    
    aux4=df["VELOCIDAD"]
    aux5=aux4[Ind]
    valorfila3=float(aux5)
    
    
    resultado=(valorfila1*(0.157)*valorfila2*valorfila3)
    df.loc[Ind,"RESULTADO"]=resultado
    df.to_excel(Excel)
    

def verresultado():

    Excel="datosbiomecanicos.xlsx"
    df=pd.read_excel("datosbiomecanicos.xlsx")

    df.set_index("ID",inplace=True)

    informacion_indices=df[["RESULTADO","UBICACION","UNIDADES"]]
    py.popup_scrolled(informacion_indices)
    

while True:
    evento, values = ventana.read()
    if evento == py.WIN_CLOSED or evento== "Salir":
        break

    elif evento == "Limpiar":
        limpiar()


    elif evento == "Guardar":
        guardar()
        py.popup("Se Guardo Correctamente")
        
    elif evento=="Calcular":
         Calcular()
         py.popup("Se Guardo Correctamente el resultado")
         
    elif evento=="Resultado":
        verresultado()
        
    elif evento=="Limpiar":
        limpiar()
        

ventana.close()

