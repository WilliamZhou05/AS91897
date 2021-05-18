from tkinter import *
import random

global questions_answers
names = []
asked = []
score = 0
questions_answers = {
1 : ["What must you do when you see blue and red flashing lights behind you?", "Speed up and get out of the way", "Slow down and drive carefully", "Slow down and stop", "Drive on as usual", "Slow down and stop", 6],
2 : ["You may stop on a motorway only:", "If there is an emergency", "To let down or pick up passengers", "To make a U turn", "To take a photo", "If there is an emergency", 1],
3 : ["When coming up to a pedestrian crossing without a raised traffic island, what must you do?", "Speed up before the pedestrians cross", "Stop and give way to a pedestrian on any part of the crossing", "Sound the horn on your vehicle to warn the pedestrians", "Slow down to 30kmh", "Stop and give way to pedestrians on any part of the crossing", 2],
4 : ["Can you stop on a bus stop in private motor vehicle?", "Only between midnight and 6am", "Under no circumstances", "When dropping off passengers", "Only if its less than 5 minutes", "Under no circumstances", 2],
5 : ["What is the maximum speed you may drive if you have a 'space saver wheel' fitted? (km/h)", "70 km/h", "100 km/h so you do not hold up traffic", "80 km/h and if the wheel spacer displays the lower limit that applies" "90 km/h", "80 km/h and if the wheel spacer displays the lower limit that applies", 3],
6 : ["When following another vehicle on a dusty road, you should", "Speed up to get passed", "Turn your vehicles windscreen wipers on", "Stay back from the dust cloud", "Turn vehicle head lights on", "Stay back from the dust cloud", 3],
7 : ["What does the sign containing letters 'LSZ' mean?", "Low safety zone", "Low stability zone", "Lone star zone", "Limited speed zone", "Limited speed zone", 4],
8 : ["What speed are you allowed to pass a school bus that has stoppe to let students get on or off?", "20 km/h", "30 km/h", "70 km/h", "10 km/h", "20 km/h", 1],
9 : ["What is the maximum distance a load may extend in front of a car?", "2 meters forward of the front edge of the seat", "4 meters forward of the front edge of the seat", "3 meters forward of the front edge of the seat", "2.5 meters forward of the front edge of the seat", "3 meters forward of the front edge of the street", 3],
10 : ["To avoid being blinded by the headlights of another vehicle coming towards you what should you do?", "Look to the left of the road", "Look to the center of the road", "Wear sunglasses that have sufficient strength", "Look to the right side of the road", "Look to the left of the road", 1]
}


class QuizStarter:

  def name_collection(self):
      name=self.entry_box.get()
      names.append(name)
      self.quiz_frame.destroy()
      Quiz(root)
  
  def __init__(self,parent):
    background_colour="pink"
    
    #creating Frame
    self.quiz_frame = Frame(parent, bg = background_colour, padx=200, pady=100)
    self.quiz_frame.grid()

    #creating Label
    self.head_label = Label(self.quiz_frame, text="Placeholder", bg = background_colour)
    self.head_label.grid(row=0, padx=20, pady=20)

    #create a Label to ask for the name
    self.user_label = Label(self.quiz_frame, text="Can you smell what the Rock is cooking?", bg = background_colour)
    self.user_label.grid(row=1, padx=20, pady=20)

    #creating Entry Box
    self.entry_box = Entry(self.quiz_frame, bg = "bisque")
    self.entry_box.grid(row=2, padx=20, pady=20)

    #creating a Button
    self.continue_button = Button(self.quiz_frame, text="Continue",bg = "darkorange",command=self.name_collection)
    self.continue_button.grid(row=3, padx=20 , pady=20)

class Quiz:
  def test_progress(self):
    global score
    scr_label=self.score_label
    choice=self.var1.get()
    if len(asked)>9:
      if choice == questions_answers[qnum][6]:
        score+=1
        scr_label.configure(text=score)
        self.quiz_instance.config(text="Confirm")
      else:
        score+=0
        scr_label.configure(text="The correct answer was" + questions_asnwers[qnum][5])
        self.quiz_instance.config(text="Confirm")
    else:
      if choice == 0:
        self.quiz_instance.config(text="Please press a button them submit again")
        choice=self.var1.get()
      else:
        if choice == questions_answers[qnum][6]:
          score+=1
          scr_label.configure(text=score)
          self.quiz_instance.config(text="Confirm")
        else:
          score+=0
          scr_label.configure(text="The correct answer was" + questions_asnwers[qnum][5])
          self.quiz_instance.config(text="Confirm")
          
  def __init__(self,parent):
    background_colour="blue"

    self.quiz_frame = Frame(parent, bg = background_colour, padx=100, pady=100)
    self.quiz_frame.grid()

    #questions
    self.question_label = Label(self.quiz_frame , text = questions_answers[qnum][0],bg = background_colour)
    self.question_label.grid(row=1 , padx=10 , pady=10)

    #holds values for radio buttons
    self.var1 = IntVar()

    #radio button 1
    self.rb1 = Radiobutton(self.quiz_frame , text = questions_answers[qnum][1] , bg=background_colour , value=1 , padx=10 , pady=10 , variable = self.var1 , indicator = 0 , background = background_colour)
    self.rb1.grid(row=2 , sticky=W)

    #radio button 2
    self.rb1 = Radiobutton(self.quiz_frame , text = questions_answers[qnum][2] , bg=background_colour , value=2 , padx=10 , pady=10 , variable = self.var1 , indicator = 0 , background = "light blue")
    self.rb1.grid(row=3 , sticky=W)
    
    #radio button 3
    self.rb1 = Radiobutton(self.quiz_frame , text = questions_answers[qnum][3] , bg=background_colour , value=3 , padx=10 , pady=10 , variable = self.var1 , indicator = 0 , background = "light blue")
    self.rb1.grid(row=4 , sticky=W)
    
    #radio button 4
    self.rb1 = Radiobutton(self.quiz_frame , text = questions_answers[qnum][4] , bg=background_colour , value=4 , padx=10 , pady=10 , variable = self.var1 , indicator = 0 , background = "light blue")
    self.rb1.grid(row=5 , sticky=W)

    #confirm Button
    self.quiz_instance = Button(self.quiz_frame , text = "Confirm" , bg=background_colour, command=self.test_progress)
    self.quiz_instance.grid(row=7 , padx=5 , pady=5)

    #score Label
    self.score_label = Label(self.quiz_frame , text = "Score" , bg=background_colour)
    self.score_label.grid(row=8 , padx=10 , pady=1)

def questions_setup(self):
  
  randomiser()
  self.var1.set(0)
  self.question_label.config(text=questions_answes[qnum][0])
  self.rb1.config(test=questions_answers[qnum][1])
  self.rb2.config(test=questions_answers[qnum][2])
  self.rb3.config(test=questions_answers[qnum][3])
  self.rb4.config(test=questions_answers[qnum][4])

def test_progress(self):
  global score
  scr_label=self.score_label
  choice=self.var1.get()
  if len(asked)>9:
    if choice == questions_answers[qnum][6]:
      score+=1
      scr_label.configure(text=score)
      self.quiz_instance.config(text="Confirm")
    else:
      score+=0
      scr_label.configure(text="The correct answer was" + questions_asnwers[qnum][5])
      self.quiz_instance.config(text="Confirm")
  else:
    if choice == 0:
      self.quiz_instance.config(text="Please press a button them submit again")
      choice=self.var1.get()
    else:
      if choice == questions_answers[qnum][6]:
        score+=1
        scr_label.configure(text=score)
        self.quiz_instance.config(text="Confirm")
      else:
        score+=0
        scr_label.configure(text="The correct answer was" + questions_asnwers[qnum][5])
        self.quiz_instance.config(text="Confirm")

def randomiser():
  global qnum 
  qnum = random.randint(1,10) 
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()

randomiser()



if __name__=="__main__":
  root=Tk() #creating a window
  root.title("Placeholder")
  quiz_instance = QuizStarter(root)
  root.mainloop() #test