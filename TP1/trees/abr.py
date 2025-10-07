from binarytree import Node
import networkx as nx
import matplotlib.pyplot as plt
from hierarchy_pos import hierarchy_pos, add_edges, in_order

#ABR

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

values = list(map(int, input("Entrez les valeurs séparées par des espaces : ").split()))
root = None
for v in values:
    root = insert(root, v)

print("\nArbre Binaire de Recherche :")
print(root)


print("\nParcours in-ordre :")
in_order(root)
print()

G = nx.DiGraph()
add_edges(G, root)

pos = hierarchy_pos(G, root=root.value)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, arrows=False)
plt.title("Arbre Binaire de Recherche ")
plt.show()

print("Hauteur:", root.height)
print("Taille:", root.size)
print("Équilibré:", root.is_balanced)
