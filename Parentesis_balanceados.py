# -*- coding: utf-8 -*-
"""
Parentesis balanceados

Los paréntesis están equilibrados, si todos los paréntesis de apertura tienen
sus correspondientes paréntesis de cierre. Este programa devuelve "True", si los
paréntesis en la expresión dada están equilibrados, y False si no.

@author: JCGS
"""
def balanced(expression):
    coun = 0
    for i in expression:
        if i == '(':
            coun += 1
        if i == ')':
            coun -= 1
        if coun < 0:
            return False
    if coun == 0:
        return True
    else:
        return False


print(balanced(input('Ingresa la expresión a evaluar :')))