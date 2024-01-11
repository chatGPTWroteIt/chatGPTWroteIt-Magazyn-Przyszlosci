import igraph as ig

g = ig.Graph()

g.add_vertex("Hello")
g.add_vertex("Hel")

g.add_edge("Hello","Hel")

a = 545
b = str(a)
print (b)
print(g)
