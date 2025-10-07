from binarytree import build
import networkx as nx
import matplotlib.pyplot as plt
from hierarchy_pos import hierarchy_pos, add_edges, in_order 

#AVL

values = list(map(int, input("Entrez les valeurs séparées par des espaces : ").split()))

root = build(values)

print("\nArbre AVL :")
print(root)

print("Hauteur :", root.height)
print("Taille :", root.size)

print("\nParcours In-ordre (AVL) :")
in_order(root)
print()

G = nx.DiGraph()
add_edges(G, root)

pos = hierarchy_pos(G, root=root.value)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=800, arrows=False)
plt.title("Arbre AVL ")
plt.show()
