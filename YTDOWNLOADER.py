print ("WELCOME TO THE YOUTUBE VIDEO/ AUDIO DOWNLOADER ")
print ("1.VIDEO")
print ("2.AUDIO")
print ("3.BOTH")
import pyperclip
import pafy

url = pyperclip.paste()
def VIDEO():
    video = pafy.new(url)
    streams = video.streams
    for i in streams:
        print(i)
    best = video.getbest()
    best.download()
def AUDIO():
    video = pafy.new(url)
    bestaudio = video.getbestaudio()
    bestaudio.download()
users_choice = int(input("\nEnter your Choice: "))  
if users_choice == 1:
    VIDEO()
elif users_choice == 2:
    AUDIO()
elif users_choice == 3:
    VIDEO()
    AUDIO()