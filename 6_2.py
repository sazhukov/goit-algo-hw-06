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

# Пошук в ширину (BFS)
def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors = list(graph[node])
            for neighbor in neighbors:
                queue.append(neighbor)
    return visited

# Пошук в глибину (DFS)
def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            neighbors = list(graph[node])
            for neighbor in neighbors:
                stack.append(neighbor)
    return visited

# Використання BFS та DFS
bfs_result = bfs(G, "Alice")
dfs_result = dfs(G, "Alice")

print(f"Результат пошуку в ширину (BFS) з 'Alice': {bfs_result}")
print(f"Результат пошуку в глибину (DFS) з 'Alice': {dfs_result}")

# Візуалізація графа
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True, node_size=700, node_color='lightgreen', font_size=10, font_color='black', font_weight='bold')
plt.title("Соціальна мережа")
plt.show()