from tkinter import *  
import random

# Import required libraries
root = Tk() 
root.geometry('410x400') 
root.resizable(False, False) 
root.title('DataFlair - Rock,Paper,Scissors') 
root.config(bg ='#856ff8') 

Label(root, text = 'Rock, Paper, Scissors' ,
     font='arial 20 bold', bg = 'white', ).place(x=60 , y = 15)

# For User Choice
user_take = StringVar() 

Label(root, text = 'Choose any one: rock, paper, scissors',
     font='arial 15 bold', bg = 'white').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take ,
      bg = 'white').place(x=90 , y = 130)

# For Computer Choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

# Function to Start Game
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('Congratulations, you both select same!')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('You loose, computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('You win, computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('You loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('You win, computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('You loose, computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('You win, computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

# Function to Reset
def Reset():
    Result.set("") 
    user_take.set("")

# Function to Exit
def Exit():
    root.destroy()

# Define Buttons
Entry(root, font = 'arial 10 bold', textvariable = Result,
        bg ='white',width = 50,).place(x=25, y = 250)
Button(root, font = 'arial 13 bold', text = 'PLAY' 
       ,padx =5,bg ='white' ,command = play).place(x=160,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET' 
       ,padx =5,bg ='white' ,command = Reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  
       ,padx =5,bg ='white' ,command = Exit).place(x=250,y=310)

root.mainloop()


