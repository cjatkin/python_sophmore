# guiBasic.py pulls up a GUI in a webbrowzer with button (that is connected to the commander)
# and when the button is pressed, the commander is accessed

# DISPLAYS MESSAGE ONCE BUTTON IS PRESSED


import redis
import sys
import json
from time import sleep
import commandBasic
import data
import remi.gui as gui
from remi import start, App
import saved_data.py

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):

        # setting up the gui
        container = gui.VBox(width=120, height=100)
        self.btn1 = gui.Button("Connect with Redis")
        self.text1 = gui.Label("status: NOT CONNECTED")

        # triggers the action after the event occured
        self.btn1.onclick.do(self.on_button_pressed)

        # adds objects to the container so it actually is displayed
        container.append(self.btn1)
        container.append(self.text1)

        # returns the root widget
        return container

    # triggered when event happens
    def on_button_pressed(self, widget):

        # changes text when button is pressed
        message = commandBasic.msg              #msg imported from commandBasic
        message2 = message.decode('UTF-8')      #msg converted from bytes to string
        self.btn1.set_text(message2)            #msg displayed as text

	########to display saved graph######################################3
	im = img.imread(dir + 'saved_data.jpeg'):
	   ax.imshow(im)
	   ax.axis('off')


        ##########################################################################################
        # simple howdy redis
        redis_host = "localhost"
        redis_port = 6379
        redis_password = ""

        def howdy():
            try:
                r = redis.StrictRedis(
                    host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
                r.set("greeting:howdy", "Howdy!!!")
                greeting = r.get("greeting:howdy")
                print(greeting)
                self.text1.set_text("status: CONNECTION ACHIEVED")

            except Exception as e:
                print(e)

        if __name__ == '__main__':
            howdy()


# start the webserver
start(MyApp)
