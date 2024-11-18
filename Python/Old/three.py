import matplotlib.pyplot as plt
import networkx as nx
import imageio
import os
from collections import deque

# Breadth-First Search (BFS) to traverse the tree and generate steps for the animation
def bfs_traversal(graph, start):
    visited = {node: False for node in graph.nodes}
    queue = deque([start])
    visited[start] = True
    steps = []  # To store the traversal steps
    
    while queue:
        current_node = queue.popleft()
        steps.append(current_node)  # Store the current node being visited
        
        for neighbor in graph.neighbors(current_node):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                
    return steps

# Function to create and save frames for each step of the BFS traversal
def create_frame(graph, current_node, step, total_steps):
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Draw the graph (tree) with nodes and edges
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', ax=ax, node_size=500, font_size=14, font_weight='bold')
    
    # Highlight the current node being visited in the traversal
    nx.draw_networkx_nodes(graph, pos, nodelist=[current_node], node_color='orange', node_size=700, ax=ax)

    # Title of the step
    ax.set_title(f"Passo {step}/{total_steps} - Visitando o Nó {current_node}", fontsize=16)
    plt.savefig(f"frames/frame_{step}.png")
    plt.close()

# Create a hierarchical tree structure as a graph
graph = nx.Graph()
graph.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('C', 'G'),
    ('F', 'H'),
    ('F', 'I')
])

# Directory to store frames
frames_dir = 'frames'
os.makedirs(frames_dir, exist_ok=True)

# Run BFS traversal and get the order of nodes visited
steps = bfs_traversal(graph, 'A')

# Generate frames for each step
total_steps = len(steps)
for step, current_node in enumerate(steps, start=1):
    create_frame(graph, current_node, step, total_steps)

# Collect the images and save them as a looping GIF
images = []
for i in range(1, total_steps + 1):
    images.append(imageio.imread(f"frames/frame_{i}.png"))

# Save the gif with moderate speed (1 second per frame) and loop forever
imageio.mimsave('hierarchical_traversal.gif', images, duration=1500, loop=0)

# Clean up frame files
for i in range(1, total_steps + 1):
    os.remove(f"frames/frame_{i}.png")

print("Looping GIF animation created: hierarchical_traversal_bfs.gif")
