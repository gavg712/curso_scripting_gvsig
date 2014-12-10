from gvsig import *
from commonsdialog import *

def main(*args):
    #Remove this lines and add here your code
    msgbox("Bievenido a gvSig","Titulo: Welcome to gvSIG",1)
    cnt = confirmDialog('Desea continuar en gvSIG?','Primeros pasos',1,2)
    if cnt == 0 : print 'hola', inputbox("Para continuar introduce tu nombre","Nombre",3,"Sr. "), 'es un gusto poder continuar'
    elif cnt == 1 : msgbox("Lamento que no quieras continuar","Titulo: Despedida",1)
    elif cnt == 2 : print "Has cancelado el proceso"
    
