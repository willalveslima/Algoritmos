import time
import timeit
import random
import util

'''
lista = []
for i in range(0,10):
    lista.append(random.randrange(1000))    
inicio = time.time()
InsertionSort.sort(lista)
fim = time.time()
print(fim - inicio)
'''
algoritmos =['InsertionSort','MedianSort','qSort','HeapSort']
repeticoes = 100
print('Teste dos Algorítmos: listas com 100 elementos e ',repeticoes,' repeticoes:')
for tipo in util.tipo_lista:
    print(tipo)
    for algoritmo in algoritmos:
        stmt = algoritmo +'.sort(lista)' 
        setup4 = '''
import {_algoritmo}
from util import gera_lista 
from util import tipo_lista
lista = gera_lista(100,{tipo_lista})
'''.format(_algoritmo=algoritmo,tipo_lista=tipo)
        print('{0:15} : {1}'.format(algoritmo,timeit.timeit(stmt,setup4, number=repeticoes )))          
    print('-'*50)
#olá