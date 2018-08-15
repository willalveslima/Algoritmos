#Funcoes especiais e facilidades
# Autor: Willian Alves Lima
# Email: w.alves.lima@gmail.com
# Versao: 0.1
# data: 02/07/2018

from enum import Enum
import random

def gera_lista(numero_elementos, tipo_lista):
    lista = []
    if tipo_lista is tipo_lista.CRESCENTE:
        return list(range(0,numero_elementos))
    elif tipo_lista is tipo_lista.DECRECENTE:
        return list(range((numero_elementos-1), -1,-1))
    elif tipo_lista is tipo_lista.RANDOMICA:
        for i in range(0,numero_elementos):
            lista.append(random.randrange(1000))
        return lista

#class tipo_lista
class tipo_lista(Enum):
    RANDOMICA = 0
    CRESCENTE = 1
    DECRECENTE = -1

#funcao cmp(a,b)
def my_cmp(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1    
#funcao swap
def swap(a,b):
    return [b, a]
#pg 70
def partition(ar,left,right,pivoIndex):
    pivot = ar[pivoIndex]
    
    #move o pivot para fim do array
    #ar[right], ar[pivoIndex] = swap(ar[right], ar[pivoIndex]) 
    
    tmp = ar[right]
    ar[right] = ar[pivoIndex]
    ar[pivoIndex] = tmp
    
    #todos os valores, = pivot sao movidos para a frente do array
    #sendo o pivot inserido apenas apos eles

    store = left
    for idx in range(left,right):
        if my_cmp(ar[idx],pivot) <= 0:
            
            tmp = ar[idx]
            ar[idx] = ar[store]
            ar[store] = tmp
            
                        #ar[idx], ar[store] = swap( ar[idx], ar[store])
            store = store + 1
    
    tmp = ar[right]
    ar[right] = ar[store]
    ar[store] = tmp
    
    #ar[right], ar[store] = swap(ar[right], ar[store])
    return store
