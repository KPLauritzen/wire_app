import pickle

import networkx as nx

def load_graph():
    with open("movie_graph.pkl", "rb") as f:
        G = pickle.load(f)
    return G

def get_connection(G, root, target, max_collabs_print=5, is_multigraph=False):
    path = nx.algorithms.shortest_path(G, root, target)
    path_str = " -> ".join(path)
    print(path_str)
    if is_multigraph:
        print("---\nDetails:")
        for start, end in zip(path, path[1:]):
            collabs = G.get_edge_data(start, end)
            collabs_str = ", ".join([work["work"] for work in collabs.values()])
            if len(collabs) > max_collabs_print:
                collabs_str += "..."
            print(f"{start} -> {end}: {len(collabs)} collaboration(s)")
            print(collabs_str)
    return path_str