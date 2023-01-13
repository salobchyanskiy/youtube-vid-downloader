from pytube import YouTube
from colorama import *

"""
https://github.com/salobchyanskiy


  ██████  ▄▄▄       ██▓     ▒█████   ▄▄▄▄    ▄████▄   ██░ ██▓██   ██▓ ▄▄▄       ███▄    █   ██████  ██ ▄█▀ ██▓▓██   ██▓
▒██    ▒ ▒████▄    ▓██▒    ▒██▒  ██▒▓█████▄ ▒██▀ ▀█  ▓██░ ██▒▒██  ██▒▒████▄     ██ ▀█   █ ▒██    ▒  ██▄█▒ ▓██▒ ▒██  ██▒
░ ▓██▄   ▒██  ▀█▄  ▒██░    ▒██░  ██▒▒██▒ ▄██▒▓█    ▄ ▒██▀▀██░ ▒██ ██░▒██  ▀█▄  ▓██  ▀█ ██▒░ ▓██▄   ▓███▄░ ▒██▒  ▒██ ██░
  ▒   ██▒░██▄▄▄▄██ ▒██░    ▒██   ██░▒██░█▀  ▒▓▓▄ ▄██▒░▓█ ░██  ░ ▐██▓░░██▄▄▄▄██ ▓██▒  ▐▌██▒  ▒   ██▒▓██ █▄ ░██░  ░ ▐██▓░
▒██████▒▒ ▓█   ▓██▒░██████▒░ ████▓▒░░▓█  ▀█▓▒ ▓███▀ ░░▓█▒░██▓ ░ ██▒▓░ ▓█   ▓██▒▒██░   ▓██░▒██████▒▒▒██▒ █▄░██░  ░ ██▒▓░
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▒░▒░ ░▒▓███▀▒░ ░▒ ▒  ░ ▒ ░░▒░▒  ██▒▒▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒░▓     ██▒▒▒ 
░ ░▒  ░ ░  ▒   ▒▒ ░░ ░ ▒  ░  ░ ▒ ▒░ ▒░▒   ░   ░  ▒    ▒ ░▒░ ░▓██ ░▒░   ▒   ▒▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░░ ░▒ ▒░ ▒ ░ ▓██ ░▒░ 
░  ░  ░    ░   ▒     ░ ░   ░ ░ ░ ▒   ░    ░ ░         ░  ░░ ░▒ ▒ ░░    ░   ▒      ░   ░ ░ ░  ░  ░  ░ ░░ ░  ▒ ░ ▒ ▒ ░░  
      ░        ░  ░    ░  ░    ░ ░   ░      ░ ░       ░  ░  ░░ ░           ░  ░         ░       ░  ░  ░    ░   ░ ░     
                                          ░ ░                ░ ░                                               ░ ░     

"""

print("Youtube-vid-downloader v.0.1 by salobchyanskiy")
link = input("Enter a video link: ")
video = YouTube(link)
quality = input("Choose a video quality (High/Low): ")

if quality == "High":
    print(f"Downloading video {video.title} from channel {video.author}")
    output = video.streams.get_highest_resolution()
    print(Fore.LIGHTGREEN_EX + "Successfully downloading! Check a folder with this program")
  
if quality == "Low":
    print(f"Downloading video {video.title} from channel {video.author}")
    output = video.streams.get_lowest_resolution()
    print(Fore.LIGHTGREEN_EX + "Successfully downloading! Check a folder with this program")


output.download()

print("Press a random button to exit")