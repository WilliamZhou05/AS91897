import tkinter as tk
from functools import partial
from tkinter import font # a quick way to make a callback function
#importing Tkinter

font_colour = "#00ffff"
border_colour = "#00ffff"
background_colour = "#000000"
#selecting colours for certain objects

class Situation(tk.Frame): #making a frame
    def __init__(self, master = None, story = '', buttons = [], **kwargs):#sets up the main part of the code
        tk.Frame.__init__(self, master, **kwargs)#creates the frame for the main code
        story_label = tk.Label(self, text = story, bg = background_colour, fg = font_colour, justify = tk.LEFT, anchor = tk.NW, font = ("Play", 10))#creates the label of the main story code
        story_label.pack()#places the label

        for btn_text, new_situation in buttons:#creates buttons according to the defined "buttons" list
            btn = tk.Button(self, text = btn_text, bg = background_colour, fg = font_colour, command = partial(self.quit_, new_situation)) #creates the button which when pressed loads the situation that is set as the button
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
"""You are standing in the middle of a country road overgrown with weeds.
There is a forest behind you and a hill in front of you.
At his feet there is a sign, partially obscured by a piece of dirty dirt
mesh. You can't tell from here what's on the other
side of the hill. You guess you're here coming out of the woods
but you feel a pain in your head when you try to remember something.
It looks like rain and you are wearing only a light tracksuit and flip flops.
In your sweatshirt pocket you can smell a ham and cheese sandwich. The wind is menacing
rocks the trees and the net on the sign breaks out encouragingly towards you.
Whachu doin?
""",
        'buttons': [
            ('you go up the hill and look around', 'situation_1'),
            ('you approach the sign and break the net off it', 'situation_2'),
            ('you eat a sandwich', 'situation_3'),
            ('you turn back towards the forest', 'situation_4'),
            ]
        },
    'situation_1': {
        'story':                                                                        
"""The flip flops made your task a bit more difficult, but in the end you pretend
you become standing on the top of the hill. Before you stretches
there is a huge field of cabbage, followed by a submerged one
the countryside in gray. The cloudy sky seems to be overwhelming
roofs of houses, and you start to feel uncomfortable ...
What are you doing?
""",
        'buttons': [
            ('you walk to the sign and break the net', 'situation_2v1'),
            ('youre eating a sandwich', None),
            ('youre turning back to the woods', None),
            ('you are approaching a cabbage field', None) # using None until you fill in the correct value
            ]
        },
    'situation_2': {
        'story':
"""The mesh is damp and full of soaked pieces of earth.
You manage to pull it off with one hand movement, but it gets dirty
mud on the occasion. Your eyes appear blurred,
however, the inscription: Tomaszowice is still legible.
What are you doing?
""",
        'buttons': [
            ('you go up the hill and look around', None),
            ('you eat a sandwich', None),
            ('you turn back towards the forest', None)
            ]
        },
    'situation_3': {
        'story':
"""The sandwich has a firm, firm consistency.
The smell of fresh bread lifts you up,
and the classic combination of ham and cheese is reminiscent of
think of a house. You feel ready to go on!
What are you doing?
""",
        'buttons': [
            ('you go up the hill and look around', None),
            ('you walk to the sign and break the net', None),
            ('youre turning back to the woods', None),
            ]
        },
    'situation_4': {
        'story':
""" You take a few steps towards the tree line, but
some mysterious force prevents you from overcoming it.
You feel powerless. You finally turn back
towards the place where you just stood.
What are you doing?
""",
        'buttons': [
            ('you go up the hill and look around', None),
            ('you go to the sign and break the net', 'situation_2v3'),
            ('youre eating a sandwich', None),
            ]
        },
    'situation_2v1': {
        'story':
"""The mesh is damp and full of soaked debris.
You manage to pull it off with one hand movement, but it gets dirty
mud on the occasion. Your eyes appear blurred,
however, the inscription: Tomaszowice is still legible.
What are you doing?
""",
        'buttons': [
            ('youre eating a sandwich', None),
            ('youre turning back to the woods', None),
            ('you are approaching a cabbage field', None),
            ]
        },
    'situation_2v2': {
        'story':
"""The mesh is damp and full of soaked pieces of earth.
You manage to pull it off with one hand movement, but it gets dirty
mud on the occasion. Your eyes appear blurred,
however, the inscription: Tomaszowice is still legible.
What are you doing?
""",
        'buttons': [
            ('you go up the hill and look around', None),
            ('youre turning back to the woods', None),
            ]
        },
    'situation_2v3': {
        'story':
"""The mesh is damp and full of soaked pieces of earth.
You manage to pull it off with one hand movement, but it gets dirty
mud on the occasion. Your eyes appear blurred,
however, the inscription: Tomaszowice is still legible.
What are you doing?
""",
        'buttons': [
            ('you go up the hill and look around', None),
            ('youre eating a sandwich', None),
            ]
        },

    }
def beginning(): #the beginning destroys the starter boxes
    title_text.destroy()
    start_button.destroy()
    name_entry_box.destroy()
    load() # load the first story

#WINDOW
root = tk.Tk()
root.geometry('500x500-500-300')
root.title('The Adventure')
root.config(background = background_colour)

#TEXT BOX
title_text = tk.Label(root, text = "Welcome To The Adventure", bg = background_colour, fg = font_colour)
title_text.place(relx = .5, rely = .4, anchor = 'c')

#NAME ENTRY
name_entry_box = tk.Entry(root, highlightthickness = 2, bg = "#333333", fg = font_colour)
name_entry_box.place(relx = .5, rely = .5, anchor = 'c')
name_entry_box.config(highlightbackground = font_colour, highlightcolor= "blue")



#START
start_button = tk.Button(root, text = "START", command = beginning, bg = background_colour, fg = font_colour)
start_button.place(relx = .5, rely = .6, anchor = 'c')

#THE LOOP
root.mainloop()