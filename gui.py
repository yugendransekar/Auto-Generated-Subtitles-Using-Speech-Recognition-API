import PySimpleGUI as sg
from app import generateSRT

sg.theme("DarkBlack")

layout = [[sg.Text("Track The File to generate SRT file")],
          [sg.Input(), sg.FileBrowse(file_types=(("MP4 File","*.mp4"),("MKV File","*.mkv"),("AVI File","*.avi")))], 
          [sg.Text("Progress"), sg.ProgressBar(100, orientation='h', size=(20, 20), key='progress')],
          [sg.Button("Generate"), sg.Button("Cancel")]]

window  = sg.Window("Auto SRT File Generator", layout)
progress_bar = window['progress']

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	
        break
    elif event == 'Generate':
        print("Generating...")
        flag = generateSRT(values[0],progress_bar)
        if flag == True:
            sg.Popup("SRT File Generated... Look in the file location")

