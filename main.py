import tkinter as tk
import customtkinter as ctk
import yt_dlp
import os
from tkinter import filedialog

def browse_folder():
    # Open folder dialog to select download directory
    folder = filedialog.askdirectory(title="Select Download Folder")
    if folder:
        path_var.set(folder)

def start_download():
    # Function to download videos from different platforms
    platform = platform_var.get()
    link = link_entry.get()
    download_path = path_var.get()
   
    if not link:
        print("Please enter a valid link.")
        status_label.configure(text="Please enter a valid link!", text_color="red")
        return
    
    if not download_path:
        print("Please select a download folder.")
        status_label.configure(text="Please select a download folder!", text_color="red")
        return
   
    # Clear any previous status message
    status_label.configure(text="")
   
    # Create platform subfolder
    platform_folder = os.path.join(download_path, platform)
    
    # Create download directory if it doesn't exist
    if not os.path.exists(platform_folder):
        os.makedirs(platform_folder)
   
    try:
        download_options = {
            'outtmpl': os.path.join(platform_folder, '%(title)s.%(ext)s')
            
            
        }
        
        with yt_dlp.YoutubeDL(download_options) as ydl:
            ydl.download([link])
            
            print(f"Download Complete! Saved to: {platform_folder}")
            # Show success message
            status_label.configure(text=f"Download Complete! Saved to: {platform_folder}", text_color="green")
    except Exception as e:
        print(f"Error: {e}")
        # Show failure message
        status_label.configure(text=f"UNSUCCESSFUL DOWNLOAD: {e}", text_color="red")

# System Settings
ctk.set_appearance_mode("System")

# App Frame
app = ctk.CTk()
app.geometry("600x550")
app.title("yoink")
app.configure(fg_color='#0D1321')

# Title
title_label = ctk.CTkLabel(app, text="yoink video downloader", font=("Arial", 24, "bold"))
title_label.pack(padx=10, pady=30)

# Platform Selection
platform_label = ctk.CTkLabel(app, text="Select Platform:")
platform_label.pack(padx=10, pady=10)

platform_var = tk.StringVar(value="YouTube")
platform_dropdown = ctk.CTkComboBox(app,
                                   values=["YouTube", "X", "Newgrounds"],
                                   variable=platform_var,
                                   width=200,
                                   height=32,
                                   state="readonly")
platform_dropdown.pack(padx=10, pady=10)

# Download Path Selection
path_label = ctk.CTkLabel(app, text="Download Folder:")
path_label.pack(padx=10, pady=(20, 5))

path_frame = ctk.CTkFrame(app, fg_color="transparent")
path_frame.pack(padx=10, pady=5)

path_var = tk.StringVar(value="")
path_entry = ctk.CTkEntry(path_frame, textvariable=path_var, width=300, height=35, placeholder_text="Select download folder...")
path_entry.pack(side="left", padx=(0, 5))

browse_button = ctk.CTkButton(path_frame, text="Browse", command=browse_folder, width=80, height=35)
browse_button.pack(side="right")

# Link Input
link_label = ctk.CTkLabel(app, text="Enter Video Link:")
link_label.pack(padx=10, pady=(20, 5))

link_entry = ctk.CTkEntry(app, width=400, height=40, placeholder_text="Paste your video link here...")
link_entry.pack(padx=10, pady=10)

# Download Button
download_button = ctk.CTkButton(app,
                               text="Yoink Video",
                               command=start_download,
                               width=200,
                               height=40)
download_button.pack(padx=10, pady=20)

# Status Label
status_label = ctk.CTkLabel(app, text="", font=("Arial", 16, "bold"))
status_label.pack(padx=10, pady=10)

# Main Loop
app.mainloop()