#guidemo.py
#code based on python tutorial
#script 1


import PySimpleGUIWeb as sg
import remi

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.figure
import io
import inspect

import time
import matplotlib.image as img
import os.path as osp


# Put any saved images here
dir= './'

message = 'word'

menu = "\na) Water" + "\nb) Tea" + "\nc) Coffee"
print(menu)

order = input("Hi! What would you like to drink?")


if order == "a":
   # def water(ax): 
        #print("Enjoy your water!")
    message = "Enjoy your water!"
        
elif order == "b":
    #def tea(ax):
        #print("Enjoy your tea!")
      message = "Enjoy your tea!"

elif order == "c":
    #def coffee(ax):
        #print("Enjoy your coffee!")
    message = "Enjoy your coffee!"


# ---------------------------- draw_figure (the helper function) ----------------------------
def draw_figure(func, element, fig, ax):
    """
    Draws the previously created "figure" in the supplied Image Element
    :param func: a function that returns a Matplotlib figure
    :param element: an Image Element
    :return: The figure canvas
    """
    # Using ax.clear() or plt.cla() is NECESSARY -- otherwise the memory goes bananas
    #plt.cla()            # erases previously drawn plots
    ax.clear()            # does the same thing as plt.cla()

    func(ax)
    canv = FigureCanvasAgg(fig)
    buf = io.BytesIO()
    canv.print_figure(buf, format='png')
    if buf is None:
        return None
    buf.seek(0)
    element.update(data=buf.read())
    #print("hello text")
    return canv

# -------------------------------- GUI Starts Here -------------------------------#
def main():

    
   # fig, ax = plt.subplots(figsize = (7,5))
    # define the layout -- very easy with PySimpleGUI because it's just a 2d array of blocks
    #fig_dict = {'Cafe': cafe}
    

#    col_listbox = [[sg.Listbox(values=fig_dict.keys(), enable_events=True, size=(25, len(fig_dict.keys())), key='-LISTBOX-')],
#                   [sg.Exit(size=(5, 2))]]

    layout = [[sg.Text('Matplotlib Plot Browser', font=('current 25')), sg.Text(message)],
              [sg.Text('Choose a plot from the list to see the plot and the source code used to make it.')],
              [element_justification='c'), sg.Image(key='-IMAGE-'),

               sg.Multiline(size=(40, 20), font='Courier 12', key='-MULTILINE-')], ]
   

    # create the window
    window = sg.Window('Embedding Matplotlib In PySimpleGUIWeb', layout)
    
    # Initial plot
    choice= 'Cafe'
    the_plotting_func = fig_dict[choice]  # get function to call from the dictionary
    window['-MULTILINE-'].Widget= remi.gui.TextInput() # prevent updating a NoneType
    window['-MULTILINE-'].update(inspect.getsource(the_plotting_func))

    while True:  # The event loop
        
        # the timeout enables image refreshing (i.g. live plotting)
        # It can be kind of slow though depending on what's being plotted
        event, values = window.read(timeout=1)
    
        if event in (sg.WIN_CLOSED, 'Exit'):  # if user closed window or clicked Exit button
            break

        # If no new button has been pressed:
        if event == '__TIMEOUT__' or values['-LISTBOX-'][0] == None:
            draw_figure(the_plotting_func, window['-IMAGE-'], fig, ax)
            #print("hello world")
            continue

        # If a button has been pressed
        else:
            # If it's a new button
            if values['-LISTBOX-'][0] != choice:
                choice = values['-LISTBOX-'][0]  # get first listbox item chosen (returned as a list)
                the_plotting_func = fig_dict[choice]  # get function to call from the dictionary
                window['-MULTILINE-'].update(inspect.getsource(the_plotting_func))  # show source code to function in multiline

            #draw_figure(the_plotting_func, window['-IMAGE-'], fig, ax)  # draw the figure
    

    window.close()


if __name__ == '__main__':
    main()
