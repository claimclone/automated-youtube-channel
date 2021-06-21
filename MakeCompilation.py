from moviepy.editor import *
import os

def makeCompilation(path,intro,outro):  #Compiling Videos
    nameOfAllFiles = os.listdir(path)   #Storing Name Of All Downloaded Files/Videos In a List[]
    if intro!= "":  #Adding Intro Video
        outputVideo = VideoFileClip(intro)
    for i in nameOfAllFiles:
        if i.endswith("mp4"):   #Checking If File Is mp4(video)
            if intro == "":
                outputVideo = VideoFileClip(path+'\\'+i)
                intro = "No Intro:)"  #Adding Dummy Data to make this condition False For Next Iteration
            else:
                clip = VideoFileClip(path+'\\'+i)
                clip = clip.resize(width=1920)  #Resizing Video Width
                clip = clip.resize(height=1080) #Resizing Video Height  
                #You Can Also Resize Intro And Outro Video Using Above Two Statements
                outputVideo = concatenate_videoclips([outputVideo,clip],method='compose')   #Concatening Videos One By One
    if outro != "": #Adding Outro Video
        clip = VideoFileClip(outro)
        outputVideo = concatenate_videoclips([outputVideo,clip],method='compose')
    outputVideo.to_videofile("output.mp4",threads=8, remove_temp=True)  #Converting Everything Into Final Video

if __name__ == "__main__":
    makeCompilation("./DownlodedVideos","","")