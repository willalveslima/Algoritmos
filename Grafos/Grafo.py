#fonte: https://github.com/Squiercg/recologia/blob/master/python/grafos/grafos.py
import matplotlib.pyplot as plt
import networkx as nx

class Graph:

	#Contrutor para grafo vazio ou com um argumento, o numero de vertices
	def __init__(self,V=None):

		if V is not None:
			self.V=V
			self.E=0
			self.adj_Lista()
			
		else:
			self.V=int(input())
			self.E=0
			self.adj_Lista()		

			e=int(input())

			for i in range(e):
				entrada = input()
				entrada = entrada.split(' ')
				v=int(entrada[0])
				w=int(entrada[1])
				self.addEdge(v,w)
	
	#Funcao que cria a lista de adjacencia, usada no construtor
	def adj_Lista(self):
		self.adj=[]
		for _ in range(self.V):
			self.adj.append([])

	#Retorna o numero de vertices
	def vertices(self):
		return self.V
	#retorna o numero de arestas
	def arestas(self):
		return self.E

	#metodo para adicionar arestas
	def addEdge(self,v,w):
		self.adj[v].append(w)
		self.E+=1

	#representando como string
	def __str__(self):
		string= str(self.V) + " vertices e " + str(self.E) + " arestas"
		return string

	#imprimindo arestas
	def imprime_arestas(self):
		v=0
		n=0
		i=0

		while v < self.V:
			n = len(self.adj[v])
			if n>0:
				while i < n:
					print(v,self.adj[v][i])
					i+=1
			v+=1
			i=0

	#grau de V
	def grau_de_v(self,v):
		return len(self.adj[v])

	#maior grau
	def maior_grau(self):
		lista = []
		for i in range(self.V):
			lista.append(self.grau_de_v(i))
		return max(lista)

	#grau medio
	def grau_medio(self):
		return 2*self.E/float(self.V)

	#conta auto-loops
	def numero_auto_loops(self):
		pass

	#o grafo e conectado
	def connected(self):
		self.visitado = [False]*self.V
		self.count=0

		self.dfs(0)

		if self.count == self.V:
			return "Conectado"
		else:
			return "Nao conectado"

	#deep first searsh para a funcao conectado
	def dfs(self, origem):
		self.visitado[origem] = True
		self.count+=1

		for i in self.adj[origem]:
			if self.visitado[i] == False:
				self.dfs(i)

	def plot(self):
		g = nx.Graph()
		#g = nx.house_graph()
		 
		for i in range(self.V):
			g.add_node(i)


		v=0
		n=0
		i=0

		while v < self.V:
			n = len(self.adj[v])
			if n>0:
				while i < n:
					g.add_edge(v,self.adj[v][i])
					i+=1
			v+=1
			i=0
		pos = nx.spring_layout(g)
		nx.draw_networkx_nodes(g, pos, node_size=700)
		nx.draw_networkx_edges(g, pos, width=6)
		nx.draw_networkx_labels(g, pos, font_size=20, font_family='sans-serif')
		plt.axis('off')
		plt.show()
		#layout = g.layout("kk")
		#igraph.plot(g, layout = layout,vertex_label=range(self.V),vertex_size=30)
