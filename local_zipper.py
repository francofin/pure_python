from utils import todo_functions
import zipper
import tkinter
import searcher
import shutil
import PySimpleGUI as sg
sg.theme('DarkAmber')
layout = [[sg.Text('Enter a file or multiple files to zip'), sg.InputText(key="browsed_files"), sg.FilesBrowse(tooltip="Enter Files")],
            [sg.Text('Enter folder to save zipped files'), sg.InputText(), sg.FolderBrowse(tooltip="Enter Path", key="new_folder")],
            [sg.Button('Compress Folder')],
          [sg.Button('Exit')]]
window = sg.Window("Local Zipper No hacks", layout=layout)
while True:
    event, values = window.read()
    print(event, values)

    match event:
        case 'Compress Folder':
            files = values['browsed_files']
            all_files = files.split(";")
            save_folder = values['new_folder']
            zipper.zip_filer(all_files, save_folder)
        case 'Exit':
            break


print("Files zipped")
window.close()