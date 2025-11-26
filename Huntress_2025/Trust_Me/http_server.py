#!/bin/python3
import http.server
import socketserver
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog


def main ():
    # Main Window
    root = tk.Tk()

    # Hide Main Window
    root.withdraw()

    # Set the file you want to serve
    filetypes = (
        ('Text Files', '*.txt'),
        ('All Files', '*.*')
    )
    file_to_serve = askopenfilename(title='Open Files',filetypes=filetypes)

    # Specify the port you want to use
    port = simpledialog.askinteger("Input Port Number", "Input port number to use:", initialvalue=7777)

    # Define a custom request handler to disable logging
    class SilentHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            pass

    # Create the server
    with socketserver.TCPServer(("", port), SilentHandler) as httpd:
        print(f"Serving {file_to_serve} at http://localhost:{port}")
        # Set the working directory to the folder containing the file
        httpd.directory = file_to_serve[:file_to_serve.rfind('/')]
        # Open the file and serve it
        httpd.serve_forever()
        
    root.destory()

main()