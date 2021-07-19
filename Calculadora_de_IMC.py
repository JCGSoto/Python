# -*- coding: utf-8 -*-
"""
Calculadora de IMC

Este programa toma el peso y la altura de una persona como entrada y genera
la categoría de IMC correspondiente.

@author: JCGS
"""
peso = int(input('Ingrese su peso(Kg) :'))
altura = float(input('Ingrese su altura(m):'))
al = (altura**2)
form = (peso / al)
if form <= 18.5:
    print('Peso insuficiente')
elif form >= 18.5 and form < 25:
    print('Normal')
elif form >= 25 and form < 30:
    print('Sobrepeso')
elif form >= 30:
    print('Obesidad')
else:
    print('error')
    
