import time
import timeit
import random
import util

algoritmos =['SequencialSearch','BinarySearch']
repeticoes = 1000
tamanho = 100
print('Teste dos Algorítmos: listas com ',tamanho,' elementos e ',repeticoes,' repeticoes:')
for algoritmo in algoritmos:
    stmt = algoritmo +'.Search(lista,valor)' 
    setup = '''
import {_algoritmo}
from util import gera_lista 
from util import tipo_lista
import random
lista = gera_lista({_tamanho},tipo_lista.CRESCENTE)
valor = lista[random.randrange({_tamanho})]
'''.format(_algoritmo=algoritmo,_tamanho=tamanho)
    print('{0:15} : {1}'.format(algoritmo,timeit.timeit(stmt,setup, number=repeticoes )))          
    print('-'*50)
#----------------------
stmt2 = 'tree.search(valor)' 
setup2 = '''
import BinaryTree
from util import gera_lista 
from util import tipo_lista
import random
lista = gera_lista(100,tipo_lista.CRESCENTE)
valor = lista[random.randrange(100)]
tree = BinaryTree.buildTree(lista)
'''
print('{0:15} : {1}'.format('BinaryTree',timeit.timeit(stmt2,setup2, number=repeticoes )))