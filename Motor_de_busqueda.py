# -*- coding: utf-8 -*-
"""
Motor de búsqueda

La función search() devuelve "Word found" si la palabra está
presente en el texto, o "Word not found", si no es así.

@author: JCGS
"""

text = input('Ingresa un texto (puede ser un párrafo) :')
word = input('Ingresa la palabra que deseas buscar :')
a = text.find(word)
def search(text,word):
    if a >= 0:
        print('Word found')
        return
    else:
        print('Word not found')
        return
    return 
search(text,word)