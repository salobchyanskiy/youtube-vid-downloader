from pytube import YouTube


print("Youtube-vid-downloader v.0.1")
link = input("Enter a video link: ")
video = YouTube(link)
quality = input("Choose a video quality (High/Low)")

if quality = "High":
  print("Downloading...")
  output = video.streams.get_highest_resolution()
  print("Successfull downloading!")
  
if quality = "Low":
  print("Downloading...")
  output = video.streams.get_lowest_resolution()
  print("Successfull downloading!")
  
else:
  print("Incorrect choose!")

  
output.download()
