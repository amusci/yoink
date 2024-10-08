import tkinter as tk
import customtkinter as ctk
import yt_dlp
import os

def startYouTubeDownload():

     # Function to download youtube videos

    ytLink = link.get()

    download_path = "C:/coding/mainprojects/yoink/DownloadedItems/YT"
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    try:
        download_options = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(download_options) as ydl:
            ydl.download([ytLink])
            print(f"Download Complete! Saved to: {download_path}")
    except Exception as e:
        print(f"Error: {e}")


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

# Download Youtube Video Button
downloadyt = ctk.CTkButton(app, text="Download Youtube", command=startYouTubeDownload)
downloadyt.pack(padx=10, pady=10)

# Main Loop

app.mainloop()


