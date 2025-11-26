import base64
import zlib
import tkinter as tk
from tkinter.filedialog import askopenfilename


# Main Window
root = tk.Tk()

# Hide Main Window
root.withdraw()

filetypes = (
    ('Text Files', '*.txt'),
    ('All Files', '*.*')
)
deflate_file = askopenfilename(title='Open Files',filetypes=filetypes)


with open(deflate_file, "r") as f:
	data = f.read().strip()
	
decoded = zlib.decompress(base64.b64decode(data))
print(decoded.decode(errors="replace"))
