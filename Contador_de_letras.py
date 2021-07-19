# -*- coding: utf-8 -*-
"""
Contador de letras

Este programa toma una cadena de caracteres como entrada y genera un diccionario
con el número de veces que aparece cada letra en la cadena.

@author: JCGS
"""

text = input('Ingresa una cadena de caracteres :')
dict = {}
lista = list(text)
diccio = dict.fromkeys(lista)

for i in text:
    contar = lista.count(i)
    diccio[i] = contar
print(diccio)