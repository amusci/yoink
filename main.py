import tkinter as tk
import customtkinter as ctk
import yt_dlp
import os

def startDownload():
    # Function to download videos from different platforms
    platform = platform_var.get()
    link = link_entry.get()
    
    if not link:
        print("Please enter a valid link.")
        return
    
    # Set download path based on platform
    if platform == "YouTube":
        download_path = "C:/coding/mainprojects/yoink/DownloadedItems/YT"
    elif platform == "X":
        download_path = "C:/coding/mainprojects/yoink/DownloadedItems/X"
    elif platform == "Newgrounds":
        download_path = "C:/coding/mainprojects/yoink/DownloadedItems/NG"
    else:
        print("Invalid platform selected.")
        return
    
    # Create download directory if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    try:
        download_options = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(download_options) as ydl:
            ydl.download([link])
            print(f"Download Complete! Saved to: {download_path}")
    except Exception as e:
        print(f"Error: {e}")

# System Settings
ctk.set_appearance_mode("System")

# App Frame
app = ctk.CTk()
app.geometry("600x400")
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

# Link Input
link_label = ctk.CTkLabel(app, text="Enter Video Link:")
link_label.pack(padx=10, pady=(20, 5))

link_entry = ctk.CTkEntry(app, width=400, height=40, placeholder_text="Paste your video link here...")
link_entry.pack(padx=10, pady=10)

# Download Button
download_button = ctk.CTkButton(app, 
                               text="Yoink Video", 
                               command=startDownload,
                               width=200,
                               height=40)
download_button.pack(padx=10, pady=20)

# Main Loop
app.mainloop()