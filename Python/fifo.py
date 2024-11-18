import matplotlib.pyplot as plt
import imageio
import os

# Function to create and save frames
def create_frame(queue, operation, step):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 5)
    ax.set_title(f"FIFO - Passo {step}: {operation}")
    
    # Draw the queue with rectangles representing elements
    for i, item in enumerate(queue):
        ax.add_patch(plt.Rectangle((0.3, i), 0.4, 0.8, fill=True, color='lightgreen'))
        ax.text(0.5, i + 0.4, item, horizontalalignment='center', verticalalignment='center', fontsize=12)
    
    ax.axis('off')
    plt.savefig(f"frames/frame_{step}.png")
    plt.close()

# Create a sequence of operations (enqueue and dequeue)
queue = []
operations = [
    ("Enfileirar A", "A"), 
    ("Enfileirar B", "B"),
    ("Enfileirar C", "C"),
    ("Enfileirar D", "D"),
    ("Desenfileirar A", None),
    ("Desenfileirar B", None),
    ("Desenfileirar C", None),
    ("Desenfileirar D", None)
]

# Directory to store frames
frames_dir = 'frames'
os.makedirs(frames_dir, exist_ok=True)

# Generate the frames for each step
step = 1
for operation, value in operations:
    if "Enfileirar" in operation:
        queue.append(value)
    elif "Desenfileirar" in operation:
        queue.pop(0)  # Remove the first element (FIFO behavior)

    # Create a frame for the current state
    create_frame(queue, operation, step)
    step += 1

# Collect the images and save them as a looping GIF
images = []
for i in range(1, step):
    images.append(imageio.imread(f"frames/frame_{i}.png"))

# Save the gif with moderate speed (1 second per frame) and loop forever
imageio.mimsave('fifo_animation.gif', images, duration=800, loop=0)  # 'loop=0' makes the GIF loop indefinitely

# Clean up frame files
for i in range(1, step):
    os.remove(f"frames/frame_{i}.png")

print("Looping GIF animation created: fifo_animation.gif")
