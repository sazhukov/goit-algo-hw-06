import heapq

import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (людей)
people = ["Alice", "Bob", "Charlie", "Diana", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack"]
G.add_nodes_from(people)

# Додавання ребер (зв'язків між людьми) з вагами
connections = [("Alice", "Bob", 1), ("Alice", "Charlie", 2), ("Bob", "Diana", 1), ("Charlie", "Eva", 3),
               ("Diana", "Frank", 4), ("Eva", "Grace", 2), ("Frank", "Henry", 1), ("Grace", "Ivy", 2),
               ("Henry", "Jack", 3), ("Jack", "Alice", 1), ("Charlie", "Frank", 2), ("Diana", "Eva", 1),
               ("Grace", "Henry", 2)]
G.add_weighted_edges_from(connections)

# Реалізація алгоритму Дейкстри (є в матеріалах з поясненнями)
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]
    while pq:
        print("pq: ", pq)
        print("sp:", shortest_paths)
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths

# Алгоритм Дейкстри для найкоротших шляхів
def dijkstra_all_pairs_shortest_paths(graph):
    all_pairs_shortest_paths = {}
    for node in graph.nodes:
        shortest_paths = dijkstra(graph, node)
        all_pairs_shortest_paths[node] = shortest_paths
    return all_pairs_shortest_paths

# Знайти найкоротший шлях між всіма вершинами
shortest_paths = dijkstra_all_pairs_shortest_paths(G)

print("Найкоротші шляхи між всіма вершинами (алгоритм Дейкстри):")
for source, paths in shortest_paths.items():
    for target, distance in paths.items():
        print(f"Від {source} до {target}: {distance}")

# Приклад: найкоротший шлях від Alice до інших вершин
source_node = "Alice"
shortest_paths_from_source = nx.single_source_dijkstra_path_length(G, source_node, weight='weight')
print(f"Найкоротші шляхи від {source_node}:")
for target, distance in shortest_paths_from_source.items():
    print(f"До {target}: {distance}")

# Візуалізація графа з вагами ребер
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightgreen', font_size=10, font_color='black', font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Соціальна мережа з вагами ребер")
plt.show()

