#COMMANDER GUI

#creates textbox that says whether or not the commander is connected to drone
#has a button that sends a command to the drone if connected

import PySimpleGUIWeb as sg
import remi
import redis
import sys
import json
from remi import start, App


r = redis.Redis(host = '192.168.2.66')
p = r.pubsub(ignore_subscribe_messages = True)


class Commander(App):
    #def_init_(self, *args):
        #super(commander, self)._init_(*args)
    '''
    def main(self):
        container = gui.VBox(width = 200, height = 200)
        self.label = gui.Label("Press to send hello command: ")
        self.btn = gui.Button("hello command:")
    '''
    #this function diplays the connections status of the drone to the commander
    def ifConnected():
        box = gui.VBox(width = 120, height = 100)
        self.lbl = gui.Label('Hello world!')
        self.bt = gui.Button('Press me!')

    #this function sends a greeting command to the drone when the button is pressed
    def hello():
        container = gui.VBox(width = 200, height = 200)
        self.label = gui.Label("Press to send hello command: ")
        self.btn = gui.Button("hello command:")
        self.btn.onclick.do(self.pressed)

    def pressed(self, widget):
        #perform redis stuff here??
        # create the button and format
        self.label.set_text("button was pressed")
        self.btn.set_text("howdy!")

    def main(self):

        fig_dict = {"Connection Status:": ifConnected, "Hello Button": hello}



        window = sg.Window("Simple Commander GUI")
        sg.theme("LightGreen3")
'''
    if __name__ == "__main__":
        main()
'''

start(Commander)
