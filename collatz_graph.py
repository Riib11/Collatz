import networkx as nx
import matplotlib.pyplot as plt
import collatz_calculator

G = nx.DiGraph()

collatz_calculator.generate_tree(1,30)

for k,v in collatz_calculator.tree.items():
    for i in v:
        G.add_edge(i,k)

nx.draw_spectral(G,with_labels=True)


plt.show()