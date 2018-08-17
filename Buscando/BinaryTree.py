class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None
        self.no_pai = None
    
    def add(self,valor):
        if valor <= self.valor:
            if self.left is None:
                self.left = Node(valor)
                self.left.no_pai = self
            else:
                self.left.add(valor)
        else:
            if self.right is None:
                self.right = Node(valor)
                self.right.no_pai = self
            else:
                self.right.add(valor)
    def exibir(self):
        
        print( str(self.valor)+' ')
        
        if self.left is not None:
            self.left.exibir()
        if self.right is not None:
            self.right.exibir() 

    def search(self,valor):
        p = self
        while p != None:
            if valor == p.valor:
                return True
            elif valor < p.valor:
                p = p.left
            else:
                p = p.right
        return False

def buildTree(A):
    tree = Node(A[0])
    for i in range(1,len(A)):
        tree.add(A[i])
    return tree



