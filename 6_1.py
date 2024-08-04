import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (людей). Граф імітуватиме соціальну мережу
people = ["Alice", "Bob", "Charlie", "Diana", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack"]
G.add_nodes_from(people)

# Додавання ребер (зв'язків між людьми)
connections = [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Diana"), ("Charlie", "Eva"), ("Diana", "Frank"), 
               ("Eva", "Grace"), ("Frank", "Henry"), ("Grace", "Ivy"), ("Henry", "Jack"), ("Jack", "Alice"),
               ("Charlie", "Frank"), ("Diana", "Eva"), ("Grace", "Henry")]
G.add_edges_from(connections)

# Візуалізація графа
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True, node_size=700, node_color='lightgreen', font_size=10, font_color='black', font_weight='bold')
plt.title("Соціальна мережа")
plt.show()

# Кількість вершин
num_nodes = G.number_of_nodes()

# Кількість ребер
num_edges = G.number_of_edges()

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")

# Вивести ступені вершин
degrees = dict(G.degree())
print("Ступені вершин:")
for person, degree in degrees.items():
    print(f"{person}: {degree}")