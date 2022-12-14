import random
import threading
from tkinter import *
from tkinter import ttk
import time
from threading import Timer,Thread
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

class Window:
    def __init__(self):
        ##Selecting random texts to type
        self.possibleTexts = [
            'For writers, a random sentence can help them get their creative juices flowing. Since the topic of the sentence is completely unknown, it forces the writer to be creative when the sentence appears. There are a number of different ways a writer can use the random sentence for creativity. The most common way to use the sentence is to begin a story. Another option is to include it somewhere in the story. A much more difficult challenge is to use it to end a story. In any of these cases, it forces the writer to think creatively since they have no idea what sentence will appear from the tool.',
            'The goal of Python Code is to provide Python tutorials, recipes, problem fixes and articles to beginner and intermediate Python programmers, as well as sharing knowledge to the world. Python Code aims for making everyone in the world be able to learn how to code for free. Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.',
            'As always, we start with the imports. Because we make the UI with tkinter, we need to import it. We also import the font module from tkinter to change the fonts on our elements later. We continue by getting the partial function from functools, it is a genius function that excepts another function as a first argument and some args and kwargs and it will return a reference to this function with those arguments. This is especially useful when we want to insert one of our functions to a command argument of a button or a key binding.'
        ]
        self.text = random.choice(self.possibleTexts)
        self.length_of_text = len(self.text)
        #
        # self.left_label_text =
        # self.right_label_text =

        #Moving random text and counting how many words typed
        self.xposition = 0.75
        self.words_typed = 0
        self.timer_text = 60
        self.correct_words = ""
        ##Tracking the keypress
        self.key_press = None
        self.random_text_index = 0


        #Setting up the window/frame
        self.window = Tk()
        self.window.title("Speed Typing Test")
        self.window.geometry("700x700")
        self.frame = ttk.Frame(self.window,padding=20)
        self.frame.grid()

        #Configuring rows and columns
        self.frame.grid(row=0,column=0,sticky="NESW")
        self.frame.grid_rowconfigure(0,weight=1)
        self.frame.grid_columnconfigure(0,weight=1)
        self.window.grid_rowconfigure(0,weight=1)
        self.window.grid_columnconfigure(0,weight=1)
        #Labels
        self.instrunctions = ttk.Label(self.frame,text="Let's see how fast you can type! Press start when you're ready!")
        self.instrunctions.grid(row=0,column=0)
        self.start_button = ttk.Button(self.frame,text="START",command=self.start_test)
        self.start_button.grid(row=1,column=0)
        #Allows window to open when run
        self.window.mainloop()

    def start_test(self):
        self.instrunctions["text"] = ""
        self.start_button.destroy()
        self.timer()
        self.text_update()
    def restart(self):
        self.window.destroy()
        Window()

    def stop_test(self):
        self.random_text.destroy()
        self.user_input.destroy()

        self.correct_words_label.destroy()
        self.timer_label.destroy()
        self.timerr.destroy()


        self.try_again = ttk.Button(self.frame,text="Try Again!",command=self.restart)
        self.try_again.grid(row=1,column=0)

        self.score = ttk.Label(self.frame,text=f"You typed {self.words_typed} words per minute!",font=34)
        self.score.grid(row=0,column=0)



    def timer(self):
        timer = 3
        self.timer_label = ttk.Label(self.frame,text=timer)
        self.timer_label.grid(row=0,column=0)

        for x in range(4):
            self.timer_label["text"] = timer
            time.sleep(1)
            timer -= 1
            self.window.update()

    def check_text(self,char,index):
        if char == self.random_text["text"][index]:

            self.random_text_index +=1
            self.xposition-=.014
            self.correct_words += self.random_text["text"][index]


            self.random_text.place(relx=self.xposition, rely=0.4)
            self.correct_words_label.config(text=self.correct_words,wraplength=600)
            self.correct_words_label.place(relx=0.1, rely=0.6)


            if char == " ":
                self.words_typed +=1


    def timer_update(self):
        time_on = True
        while time_on:
            self.timer_text -= 1
            self.timerr.config(text=self.timer_text)
            print(self.timer_text)


            if self.timer_text == 0:
                time_on = False
                self.timerr.config(text=self.timer_text)

            time.sleep(1)

        self.stop_test()

    def text_update(self):

        self.timer_label.destroy()

        self.random_text = ttk.Label(self.frame, text=self.text,font=24)
        self.random_text.place(relx=self.xposition,rely=.4)

        self.user_input = ttk.Label(self.frame, text="", font=(('Helvatical bold', 30)))
        self.user_input.place(relx=0.5, rely=.75)

        self.correct_words_label = ttk.Label(self.frame, text=self.correct_words, foreground="Green",font=24,wraplength=700)

        self.timerr = ttk.Label(self.frame, text=self.timer_text, font=30)
        self.timerr.place(relx=0.5, rely=.1)
        # self.t = Timer(1, self.timer_update)
        # self.t.start()

        self.thread = Thread(target=self.timer_update)
        self.thread.daemon = True
        self.thread.start()

        def key_pressed(event):
            self.user_input["text"]=""
            self.key_pressed = event.char
            self.user_input["text"] = self.key_pressed
            self.check_text(self.key_pressed,self.random_text_index)

        self.window.bind("<Key>",key_pressed)
        print(self.random_text["text"][0])
Window()