#making button in pysimplegui_demo.py
#https://funprojects.blog/2020/02/18/pysimplegui-quick-and-easy-interfaces/

import PySimpleGUIWeb as sg


layout = [[sg.Button("Press me!")], [sg.Button("Don't press me!")]]

window = sg.Window("This is a window", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, "Exit"):
        break
    if event == "Go":
        windos["-OUT-"].Update(values["-IN-"])
window.close()
