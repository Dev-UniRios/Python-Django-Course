import matplotlib.pyplot as plt
import networkx as nx
import imageio
import os

# Dijkstra's algorithm implementation to generate steps for the animation
def dijkstra(graph, start):
    # Initialize dictionaries for distances and previous nodes
    distances = {node: float('infinity') for node in graph.nodes}
    previous_nodes = {node: None for node in graph.nodes}
    distances[start] = 0
    nodes = list(graph.nodes)
    
    steps = []  # List to store the steps for the animation

    while nodes:
        # Select the node with the smallest distance
        current_node = min(nodes, key=lambda node: distances[node])
        nodes.remove(current_node)

        # Store the current step (node being visited and its neighbors)
        steps.append((current_node, dict(distances)))

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            alternative_route = distances[current_node] + weight
            
            # If a shorter path is found, update the distance and previous node
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_nodes[neighbor] = current_node
    
    return steps, distances

# Create a frame for the current step of Dijkstra's algorithm
def create_frame(graph, distances, current_node, step, total_steps):
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Draw the graph with nodes and edges
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', ax=ax, node_size=500, font_size=14, font_weight='bold')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, ax=ax)
    
    # Highlight the current node being processed
    nx.draw_networkx_nodes(graph, pos, nodelist=[current_node], node_color='orange', node_size=700, ax=ax)

    # Annotate the distances
    for node, distance in distances.items():
        ax.text(pos[node][0], pos[node][1] + 0.1, s=f"{distance}", bbox=dict(facecolor='white', alpha=0.8), horizontalalignment='center')

    # Title of the step
    ax.set_title(f"Passo {step}/{total_steps} - Visitando o Nó {current_node}", fontsize=16)
    plt.savefig(f"frames/frame_{step}.png")
    plt.close()

# Create a graph for the Dijkstra example
graph = nx.DiGraph()
graph.add_weighted_edges_from([
    ('A', 'B', 1), 
    ('A', 'C', 4), 
    ('B', 'C', 2), 
    ('B', 'D', 5), 
    ('C', 'D', 1), 
    ('D', 'E', 3),
    ('C', 'E', 3),
])

# Directory to store frames
frames_dir = 'frames'
os.makedirs(frames_dir, exist_ok=True)

# Run Dijkstra's algorithm and get the steps
steps, final_distances = dijkstra(graph, 'A')

# Generate frames for each step
step = 1
for current_node, distances in steps:
    create_frame(graph, distances, current_node, step, len(steps))
    step += 1

# Collect the images and save them as a looping GIF
images = []
for i in range(1, step):
    images.append(imageio.imread(f"frames/frame_{i}.png"))

# Save the gif with moderate speed (1 second per frame) and loop forever
imageio.mimsave('dijkstra_animation.gif', images, duration=1500, loop=0)

# Clean up frame files
for i in range(1, step):
    os.remove(f"frames/frame_{i}.png")

print("Looping GIF animation created: dijkstra_animation.gif")
