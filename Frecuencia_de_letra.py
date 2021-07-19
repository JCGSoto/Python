# -*- coding: utf-8 -*-
"""
Frecuencia de letra

Este programa emite la frecuencia de una letra en un texto
como pocertanje entero
@author: JCGS
"""

text = input('Ingrese un texto: ')
letter = input('Ingrese una letra: ')

a = text.count(letter)
c = len(text)

if a > 0:
    b = (a/c)*(100)
    
print(int(b),'{}'.format('%'))


