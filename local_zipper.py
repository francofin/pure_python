from utils import todo_functions
import tkinter
import searcher
import PySimpleGUI as sg
sg.theme('DarkAmber')
layout = [[sg.Text('Enter Path of files to zip'), sg.InputText(), sg.FilesBrowse(tooltip="Enter Path")],
            [sg.Text('Enter Path to save zipped folder'), sg.InputText(), sg.FolderBrowse(tooltip="Enter Path")],
            [sg.Button('Compress Folder')] ]
window = sg.Window("Local Zipper No hacks", layout=layout)
window.read()
print("Files zipped")
window.close()