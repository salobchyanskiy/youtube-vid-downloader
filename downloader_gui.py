import customtkinter
import webbrowser
import tkinter
from pytube import YouTube
import time

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title("YouTube video downloader")
app.geometry("400x235")


def Download():
    video = YouTube('https://www.youtube.com/watch?v=YiLhPMT9K3Q')
    i = checkbox.get()
    if i == 1:
        video1 = video.streams.get_audio_only()
    if i == 0:
        video1 = video.streams.get_highest_resolution()
    try:
        video1.download()
    except:
        print("Error!")
    print("Success!")


frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

entry = customtkinter.CTkEntry(master=frame, placeholder_text="Video link")
entry.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Only audio",)
checkbox.pack(pady=10, padx=10)

button = customtkinter.CTkButton(master=frame, text="Download", command=Download)
button.pack(pady=12, padx=10)

app.mainloop()