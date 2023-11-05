import PySimpleGUI as sg
from fileCompressor import make_archive

files_label = sg.Text("Select files to compress:")
files_input = sg.Input(key='filestext')
browse_button = sg.FilesBrowse("Browse",key='filepaths')
destination_lbl = sg.Text("Select destination path:")
destination_folder = sg.Input(key='foldertext')
browse_dst_button = sg.FolderBrowse("Browse",key='folderpath')
compress_button = sg.Button("Compress")
feedback_label = sg.Text(key='feedback',text_color='green')


window = sg.Window('Files Compressor',layout=
        [[files_label,files_input,browse_button], [destination_lbl,destination_folder,browse_dst_button],[compress_button,feedback_label]])
while True:

    event,values = window.read()
    filepaths = values['filepaths'].split(';')
    print(filepaths)
    destination_folder = values['folderpath']

    make_archive(filepaths,destination_folder)
    window["feedback"].update('Compression completed..')





# Finish up by removing from the screen
window.close()