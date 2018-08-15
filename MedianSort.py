#----------------------------------------------------
# Median Sort                            
# Implementaçao em Python do Algoritmo Median Sort 
# Presente no livro Algoritmos  O Guia Essencial
# de Heineman, Pollice e Selkow
# Versao 0.1 
# Data 16/07/2018
#-----------------------------------------------------
from util import swap
from util import my_cmp
from util import partition
import BFPRT

def sort(A):
    medianSort(A,0,len(A)-1)


def medianSort(A, left, right):
    if left < right:
        #find media value A[me] in A[left,rigth]
        
        mid = (right - left +1)//2
        
        me = selectKth(A,mid+1,left,right)
        
        medianSort(A,left, left + mid -1)
        medianSort(A,left + mid + 1, right )

#-------------------------
def selectKth(ar,k,left,right):
    idx = selectPivotIndex(ar,left,right)
    pivoIndex = partition(ar, left, right, idx)
    if (left + k - 1) == pivoIndex:
        return pivoIndex

    if left + k - 1 < pivoIndex:
        return selectKth(ar, k, left, pivoIndex-1)
    else:
        return selectKth(ar, k - (pivoIndex - left+1), pivoIndex + 1, right)

def selectPivotIndex(ar,left,right):
    return BFPRT.selectMedian(ar,left,right)
