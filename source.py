from pytube import YouTube

link = input("Paste link of YT Video : ")
yt = YouTube(link)

#Print title
print("Title :", yt.title)
#Number of views
print("Views :", yt.views)
#Length of video
print("Duration :", yt.length)
# Get description
print("Description :", yt.description)
#Get ratings
print("Ratings :", yt.rating)

#Download Scraped Video
video = yt.streams.get_highest_resolution()
video.download()
print("Yayyy!! Download Completed!!!")

#To Download Audio File
audio = yt.streams.filter(only_audio=True).first()
audio.download()
