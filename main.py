import mss
import numpy as np
import imageio

# Video settings
filename = "/Users/arman/Downloads/output.mp4"
fps = 30
frames = []

with mss.mss() as sct:
    monitor = sct.monitors[1]  # Capture the main screen

    try:
        while True:
            img = sct.grab(monitor)  # Capture screenshot
            frame = np.array(img)  # Convert to NumPy array
            frames.append(frame)  # Store frame

    except KeyboardInterrupt:  # Stop recording with Ctrl+C
        print("Recording stopped. Saving video...")
        imageio.mimsave(filename, frames, fps=fps)
        print(f"Saved recording as {filename}")