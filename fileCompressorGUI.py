import PySimpleGUI as sg

files_label = sg.Text("Select files to compress:")
files_input = sg.Input()
browse_button = sg.FilesBrowse("Browse")
destination_lbl = sg.Text("Select destination path:")
destination_folder = sg.Input()
browse_dst_button = sg.FolderBrowse("Browse")
compress_button = sg.Button("Compress")


# Display and interact with the Window using an Event Loop
while True:

    window = sg.Window('Files Compressor',layout=
        [[files_label,files_input,browse_button], [destination_lbl,destination_folder,browse_dst_button],[compress_button]])

    window.read()
    # See if user wants to quit or window was closed



# Finish up by removing from the screen
window.close()