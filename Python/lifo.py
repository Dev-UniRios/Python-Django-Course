import matplotlib.pyplot as plt
import imageio
import os

# Function to create and save frames
def create_frame(stack, operation, step):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 5)
    ax.set_title(f"LIFO - Passo {step}: {operation}")
    
    # Draw the stack with rectangles representing elements
    for i, item in enumerate(stack):
        ax.add_patch(plt.Rectangle((0.3, i), 0.4, 0.8, fill=True, color='lightblue'))
        ax.text(0.5, i + 0.4, item, horizontalalignment='center', verticalalignment='center', fontsize=12)
    
    ax.axis('off')
    plt.savefig(f"frame_{step}.png")
    plt.close()

# Create a sequence of operations (push and pop)
stack = []
operations = [
    ("Empurrar A", "A"), 
    ("Empurrar B", "B"),
    ("Empurrar C", "C"),
    ("Empurrar D", "D"),
    ("Estourar D", None),
    ("Estourar C", None),
    ("Estourar B", None),
    ("Estourar A", None)
]

# Directory to store frames
frames_dir = 'frames'
os.makedirs(frames_dir, exist_ok=True)

# Generate the frames for each step
step = 1
for operation, value in operations:
    if "Empurrar" in operation:
        stack.append(value)
    elif "Estourar" in operation:
        stack.pop()

    # Create a frame for the current state
    create_frame(stack, operation, step)
    step += 1

# Collect the images and save them as a GIF
images = []
for i in range(1, step):
    images.append(imageio.imread(f"frame_{i}.png"))

# Save the gif with a very slow speed (10 seconds per frame)
imageio.mimsave('lifo_animation.gif', images, duration=800, loop=0)  # 10 seconds per frame

# Clean up frame files
for i in range(1, step):
    os.remove(f"frame_{i}.png")

print("Very slow GIF animation created: lifo_animation.gif")
