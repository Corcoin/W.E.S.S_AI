import wolframalpha
client = wolframalpha.Client("PG533J-V49G9PXV2P")

import wikipedia

import PySimpleGUI as sg

sg.theme('DarkRed')
layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")], [sg.InputText()]]
window = sg.Window("BRIAN II", layout)


while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    #res = client.query(values[0])
    #wolfram_res = next(res.results).text
    wiki_res = wikipedia.summary(values[0], sentences=1)
    print (values[0])
    sg.Popup(wiki_res)

window.close()