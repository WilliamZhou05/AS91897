import tkinter as tk
from functools import partial  # a quick way to make a callback function
from tkinter import font #importing font
#importing Tkinter

font_colour = "#00ffff"
border_colour = "#00ffff"
background_colour = "#000000"
#selecting colours for certain objects

class Situation(tk.Frame): #making a frame
    def __init__(self, master = None, story = '', buttons = [], **kwargs):#sets up the main part of the code kwargs is a function that allows me to put as much story inside the code as possible
        tk.Frame.__init__(self, master, **kwargs)#creates the frame for the main code
        story_label = tk.Label(self, text = story, bg = background_colour, fg = font_colour, justify = tk.LEFT, anchor = tk.NW, font = ("Play", 10))#creates the label of the main story code
        story_label.pack()#places the label

        for btn_text, new_situation in buttons:#creates buttons according to the defined "buttons" list
            btn = tk.Button(self, text = btn_text, highlightthickness = 2, bg = background_colour, fg = font_colour, command = partial(self.quit_, new_situation))
            btn.config(highlightbackground = font_colour, highlightcolor= "blue") #creates the button which when pressed loads the situation that is set as the button
            btn.pack() #places the button


    def quit_(self, new_situation):#defines the quit
        self.destroy()#destroys the current situation
        load(new_situation)#loads new situation

def load(situation = None):#defining the loading
    frame = Situation(root, **SITUATIONS.get(situation))#grabs the situations
    frame.config(bg = background_colour)#colours the background
    frame.pack()#places the frame
    
SITUATIONS = { #the story scenes
    None: { # I named 'beginning' as None so that all the unassigned buttons use it
        'story':
""""Welcome to Las Cerviz, You have one objective and one objective only."
                                                    "Survive"

This announcment keeps playing as neon cars speed around the city. 
You hear a loud rumbling sound and you can see concrete walls rising
from the ground surrounding the city.
You look around, you can see a broken neon sign leading into a hotel
and a gas station with a hovercar parked next to the building.
What do you do?
""",
        'buttons': [
            ('Go into the hotel', 'situation_1'),
            ('Walk to the wall', 'situation_2'),
            ('Sit there and cry', 'situation_3'),
            ('Go to the gas station', 'situation_4'),
            ]
        },
    'situation_1': {
        'story':                                                                        
"""The neon hotel sign flickers. 
The hotel looks uninhabited, there are a bunch of broken cups and plates
but nothing of much notice.
What are you doing?
""",
        'buttons': [
            ('Keep going through the Hotel', 'situation_2v1'),
            ('Leave the Hotel', None),
            ('Stare at the plates', 'situation_2v2'),
            ]
        },
    'situation_2': {
        'story':
"""The wall seems to be made of concrete, you try to punch it and to your suprise
its made of concrete and now your hand hurts, what did you expect?
What do you do now?
""",
        'buttons': [
            ('Go back to the start', None),
            ('Sit there and cry', 'situation_3')
            ]
        },
    'situation_3': {
        'story':
"""You sit there and cry,
an hour passes and you're still sitting there
just crying
why?
just why?
""",
        'buttons': [
            ('Get back up', None),
            ('Cry some more', 'situation_3'),

            ]
        },
    'situation_4': {
        'story':
"""You walk to the gas station, an invisible force stops you from going further
What are you doing?
""",#invisible wall cuz i dont wanna write this out :D
        'buttons': [
            ('Go back to the start', None),
            ]
        },
    'situation_2v1': {
        'story':
"""The hotel lights are flickering and you hear sirens outside.
The hotel is dark inside 
What are you doing?
""",
        'buttons': [
            ('Walk into a room', 'situation_3v1'),
            ('Go back out', 'situation_1'),
            ('Sit there and cry', 'situation_3v3'),
            ]
        },
    'situation_2v2': {
        'story':
""" You see plates.
What did you expect?
""",
        'buttons': [
            ('Look away from plates', 'situation_1'),
            ]
        },
    'situation_3v1': {
        'story':
"""The room is completly black inside you cant see anything,
you trip and fall while trying to walk in and the door closes on you, 
you are now trapped in a black box.
(The game isnt finished yet so please be patient and wait as this is the 
whole story so far)
""",
        'buttons': [
            ('Give up and go back to the start', None),
            ('Exit the game (sorry the games not finished yet)', None),
            ]
        },

    'situation_3v3': {
        'story':
"""You sit there and cry,
an hour passes and you're still sitting there
just crying
why?
just why?
""",
        'buttons': [
            ('Get back up', 'situation_2v1'),
            ('Cry some more', 'situation_3v3'),

            ]
        },

    }
def beginning(): #the beginning destroys the starter boxes
    title_text.destroy()
    start_button.destroy()
    name_entry_box.destroy()
    name_text.destroy()
    load() # load the first story

#WINDOW
root = tk.Tk()
root.geometry('500x500-500-300')
root.title('The Adventure')
root.config(background = background_colour)

#TEXT BOX
title_text = tk.Label(root, text = "Welcome To The Adventure", bg = background_colour, fg = font_colour, font = ("bold", "20"))
title_text.place(relx = .5, rely = .3, anchor = 'c')

#NAME ENTRY BOX
name_text = tk.Label(root, text = "Please enter your name below:", bg = background_colour, fg = font_colour)
name_text.place(relx = .5, rely = .4, anchor = 'c')

#NAME ENTRY
name_entry_box = tk.Entry(root, highlightthickness = 2, bg = "#333333", fg = font_colour)
name_entry_box.place(relx = .5, rely = .5, anchor = 'c')
name_entry_box.config(highlightbackground = font_colour, highlightcolor= "blue")

#START
start_button = tk.Button(root, text = "START", highlightthickness = 2, command = beginning, bg = background_colour, fg = font_colour)
start_button.place(relx = .5, rely = .6, anchor = 'c')
start_button.config(highlightbackground = font_colour, highlightcolor= "blue")

#THE LOOP
root.mainloop()