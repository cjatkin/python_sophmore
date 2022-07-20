
#import PySimpleGUIWeb as sg
import redis
import sys
import json
from time import sleep
import somefirmware as foo
import remi.gui as gui
from remi import start, App

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        #creates button and text
        '''
        layout = [[sg.Button("Connect with Redis")],
                    [sg.Text("Status: NOT CONNECTED")]]

        #gives the window a title
        window = sg.Window("CommanderGUI", layout)
        '''
        #setting up the gui
        container = gui.VBox(width=120, height=100)
        self.btn1 = gui.Button("Connect with Redis")
        self.text1 = gui.Label("status: NOT CONNECTED")

        #triggers the action after the event occured
        self.btn1.onclick.do(self.on_button_pressed)

        #adds objects to the container so it actually is displayed
        container.append(self.btn1)
        container.append(self.text1)

        #returns the root widget
        return container

    #triggered when event happens
    def on_button_pressed(self, widget):

        #changes text when button is pressed
        self.btn1.set_text("Button pressed: connection pending")

        ##########################################################################################
        #simple howdy redis
        redis_host = "localhost"
        redis_port = 6379
        redis_password = ""


        def howdy():
            try:
                r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
                #print("howdy!")
                r.set("msg:howdy", "Howdy!!!")
                msg = r.get("msg:howdy")
                print(msg)
                self.text1.set_text("status: CONNECTION ACHIEVED")

            except Exception as e:
                print(e)

        if __name__ == '__main__':
            howdy()







#start the webserver
start(MyApp)





'''
#the below opens the window and is unecessary if remi is used
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, "Exit"):
        break
    if event == "Go":
        windos["-OUT-"].Update(values["-IN-"])
window.close()
'''
