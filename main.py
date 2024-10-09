import tkinter as tk
import customtkinter as ctk
import yt_dlp
import os

def startYouTubeDownload():

# Function to download youtube videos

    ytLink = yt_link.get()

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

def startXDownload():

    # Function to download X videos

    xLink = x_link.get()
    download_path = "C:/coding/mainprojects/yoink/DownloadedItems/X"
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    try:
        
        download_options = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s')  
        }

        
        with yt_dlp.YoutubeDL(download_options) as ydl:
            ydl.download([xLink])
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

# YT UI 

yt_title = ctk.CTkLabel(app, text="Insert A Youtube Video/Shorts Link")
yt_title.pack(padx=10, pady=10)

# YT Link

yt_url = tk.StringVar()
yt_link = ctk.CTkEntry(app, width=350, height=40)
yt_link.pack(padx=10, pady=10)

# Download YT Button
download_yt = ctk.CTkButton(app, text="Download Youtube", command=startYouTubeDownload)
download_yt.pack(padx=10, pady=10)

# X UI 

x_title = ctk.CTkLabel(app, text="Insert A X Video Link")
x_title.pack(padx=10, pady=10)

# X Link

x_url = tk.StringVar()
x_link = ctk.CTkEntry(app, width=350, height=40)
x_link.pack(padx=10, pady=10)

# Download X Button
download_x = ctk.CTkButton(app, text="Download X", command=startXDownload)
download_x.pack(padx=10, pady=10)

# Main Loop

app.mainloop()


