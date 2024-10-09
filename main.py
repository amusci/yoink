import tkinter as tk
import customtkinter as ctk
import yt_dlp
import os

def startDownload(platform):

    # Function to download videos from different platforms

    if platform == "YouTube":
        link = yt_link.get()
        download_path = "C:/coding/mainprojects/yoink/DownloadedItems/YT"
    elif platform == "X":
        link = x_link.get()
        download_path = "C:/coding/mainprojects/yoink/DownloadedItems/X"
    elif platform == "NG":
        link = ng_link.get()
        download_path = "C:/coding/mainprojects/yoink/DownloadedItems/NG"
    else:
        print("Invalid platform selected.")
        return

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
ctk.set_default_color_theme("blue")

# App Frame

app = ctk.CTk()
app.geometry("1080x900")
app.title("yoink")

# YT UI 

yt_title = ctk.CTkLabel(app, text="Insert A Youtube Video/Shorts Link")
yt_title.pack(padx=10, pady=50)

# YT Link

yt_url = tk.StringVar()
yt_link = ctk.CTkEntry(app, width=350, height=40)
yt_link.pack(padx=10, pady=10)

# Download YT Button
download_yt = ctk.CTkButton(app, text="Download Youtube",  command=lambda: startDownload("YouTube"))
download_yt.pack(padx=10, pady=10)

# X UI 

x_title = ctk.CTkLabel(app, text="Insert A X Video Link")
x_title.pack(padx=10, pady=50)

# X Link

x_url = tk.StringVar()
x_link = ctk.CTkEntry(app, width=350, height=40)
x_link.pack(padx=10, pady=10)

# Download X Button
download_x = ctk.CTkButton(app, text="Download X",  command=lambda: startDownload("X"))
download_x.pack(padx=10, pady=10)

# NG UI 

ng_title = ctk.CTkLabel(app, text="Insert A Newgrounds Link")
ng_title.pack(padx=10, pady=50)

# NG Link

ng_url = tk.StringVar()
ng_link = ctk.CTkEntry(app, width=350, height=40)
ng_link.pack(padx=10, pady=10)

# Download NG Button
download_ng = ctk.CTkButton(app, text="Download NG",  command=lambda: startDownload("NG"))
download_ng.pack(padx=10, pady=10)

# Main Loop

app.mainloop()


