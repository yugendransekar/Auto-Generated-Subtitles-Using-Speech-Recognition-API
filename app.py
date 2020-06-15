
import moviepy.editor as mp
import speech_recognition as sr
import datetime
import soundfile as sf
import os
import progressbar
import PySimpleGUI as sg

widget = widgets=[
    ' [', progressbar.Timer(), '] ',
    progressbar.Bar(),
    ' (', progressbar.ETA(), ') ',
]

def generateSRT(filePath, progress_bar):
    #Coverting .mp4 to .wav
    clip = mp.VideoFileClip(filePath)
    clip.audio.write_audiofile("audio.wav")

    #Extract end time
    f = sf.SoundFile('audio.wav')
    seconds = len(f) / f.samplerate
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    #print(int(h),int(m),int(s))

    #Converting Speech to Text
    global filename
    filename = os.path.basename(filePath)
    filename,_ = filename.split(".")
    filePath,_ = filePath.split(filename)
    filename = filename + ".srt"
    filePath = os.path.join(filePath,filename)
    fp = open(filePath,"w")
    r = sr.Recognizer()
    delay = 8
    start_time = datetime.datetime(100,1,1,0,0,0)
    max_time = datetime.datetime(100,1,1,int(h),int(m),int(s))
    block = 0
    audio_file = sr.AudioFile("audio.wav")
    current_second = 0 
    bar = progressbar.ProgressBar(widgets=widget).start()

    def speech_to_srt(current_time, block, current_second, delay):
        if current_time >= max_time:
            print("Speech Recognition is over...")

        else:
            #block = block+1
            with audio_file as source:
                r.adjust_for_ambient_noise(source)
                audio = r.record(source,offset=current_second,duration=delay)
            
            try:
                block = block+1
                sentence = r.recognize_google(audio)

                current_second = current_second+delay
                end_time = current_time + datetime.timedelta(0,delay)

                with open(filePath,"a") as fp:
                    fp.write(str(block))
                    fp.write("\n")
                    fp.write(str(current_time.time()))
                    fp.write(" --> ")
                    fp.write(str(end_time.time()))
                    fp.write("\n")
                    fp.write(sentence)
                    fp.write("\n")
                    fp.write("\n")
            except:
                current_second = current_second+delay
                end_time = current_time + datetime.timedelta(0,delay)

            bar.update(current_second,seconds)
            progress_bar.UpdateBar(current_second,seconds)
            #print("Finished... "+str(int((current_second/seconds)*100))+"%")
            speech_to_srt(end_time, block, current_second, delay)

    speech_to_srt(start_time, block, current_second, delay)
    return True

#generateSRT('C:/Users/HackMachine/Downloads/Video/test.mp4')