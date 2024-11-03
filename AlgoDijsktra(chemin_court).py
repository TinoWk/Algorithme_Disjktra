"""
Membres du groupes:
ADJINOU Kodjo Paul Vahana LF-GE S4
ATIGOSSOU Mensah Ephraïm LF-GE S4
WOWUI Kossi Martin LF-GE S4

"""

#Définition d'une classe perrmettant la lecture du graphe
class Graph:
    def __init__(self, num_vertices):
        # Initialisation du graphe avec un certain nombre de sommets
        self.num_vertices = num_vertices
        # Création d'une liste d'adjacence vide pour chaque sommet
        self.adj_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, u, v, weight):
        # Ajout d'une arête entre les sommets u et v avec le poids spécifié
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))
    
    def __repr__(self):
        # Représentation du graphe sous forme de chaîne de caractères pour l'affichage
        result = ""
        for i in range(self.num_vertices):
            result += f"{i}: {self.adj_list[i]}\n"
        return result

# Lecture d'un graphe à partir d'un fichier .txt
def read_graph_from_file(file_path):
    
    with open(file_path, 'r') as file:
        # Lecture du nombre de sommets
        num_vertices = int(file.readline().strip())
        # Création d'une instance de la classe Graph
        graph = Graph(num_vertices)
        
        for line in file:
            # Arrêtons la lecture si la ligne contient "-1"
            if line.strip() == "-1":
                break
            # Lecture des sommets et du poids de l'arête
            u, v, weight = map(int, line.split())
            # Ajout de l'arête au graphe
            graph.add_edge(u, v, weight)
    
    return graph

# Implémentation de l'algorithme de Dijkstra pour trouver les plus courts chemins

def dijkstra(graph, start_vertex):

    num_vertices = graph.num_vertices
    # Initialisation des distances à l'infini
    distances = [float('inf')] * num_vertices
    # Initialisation des prédécesseurs à None
    predecessors = [None] * num_vertices
    # La distance au sommet de départ est zéro
    distances[start_vertex] = 0

    # Ensemble des sommets non visités
    unvisited = set(range(num_vertices))

# Trouvons le sommet non visité avec la distance minimale
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        current_distance = distances[current_vertex]

        # Marquons le sommet actuel comme visité
        unvisited.remove(current_vertex)

        # Mise à jour des distances et des prédécesseurs pour chaque voisin
        for neighbor, weight in graph.adj_list[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex

                # Affichage des valuations provisoires et des prédécesseurs à chaque itération
                print("Valuations provisoires:", distances)
                print("Prédécesseurs:", predecessors)

    return distances, predecessors

def print_shortest_paths(distances, predecessors, start_vertex):
    # Affichage des plus courts chemins à partir du sommet de départ
    for vertex in range(len(distances)):
        path = []
        current_vertex = vertex
        #Construction du chemin à partir des prédecesseurs
        while current_vertex is not None:
            path.insert(0, current_vertex)
            current_vertex = predecessors[current_vertex]

        # Affichage du chemin et de la distance totale
        print(f"Chemin le plus court de {start_vertex} à {vertex}: {' -> '.join(map(str, path))} (distance: {distances[vertex]})")

# Exemple d'utilisation
file_path = 'graphe.txt'  
graph = read_graph_from_file(file_path)
print(graph)

# Demande à l'utilisateur d'entrer le sommet de départ
while True:
    try:
        start_vertex = int(input("Entrez le sommet de départ: "))
        if start_vertex < 0 or start_vertex >= graph.num_vertices:
            raise ValueError("Le sommet de départ doit être compris entre 0 et " + str(graph.num_vertices - 1))
        break
    except ValueError as e:
        print(e)

# Exécution de l'algorithme de Dijkstra
distances, predecessors = dijkstra(graph, start_vertex)

# Affichage des chemins les plus courts
print_shortest_paths(distances, predecessors, start_vertex)
