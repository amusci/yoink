import tkinter as tk
import customtkinter as ctk
from pytube import YouTube

# System Settings

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# App Frame

app = ctk.CTk()
app.geometry("1080x600")
app.title("yoink")

# UI Elements

title = ctk.CTkLabel(app, text="Insert A Youtube Link")
title.pack(padx=10, pady=10)

# Link Input

url = tk.StringVar()
link = ctk.CTkEntry(app, width=350, height=40)
link.pack(padx=10, pady=10)

# Main Loop

app.mainloop()