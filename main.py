
from tkinter import *
import random

import fileinput
WordleTable = []
Root = Tk()
#gets random number, to correlate to word in possible words file
RandomNum = random.randint(0,2309)
RandomWord = ""

Turn = 0


with open("Possible Words", "r") as PossibleWords:
    for i in range(0, RandomNum):
        PossibleWords.readline()

    RandomWord = PossibleWords.readline()
    print(RandomWord)
for i in range(0, 6):
    for v in range(0, 5):

        myLabel = Label(Root, text="",width= 5,height=5,borderwidth=1,bg="grey",padx=30,pady=10)
        myLabel.grid(row=i, column=v)
        WordleTable.append(myLabel)
def func():
    global Turn

    WordTable = []
    for letter in RandomWord.strip():
        WordTable.append(letter)




    Input = myInput.get().lower()
    if not (myInput.get().isalpha()) or (len(myInput.get()) != 5):
        print("Please enter a valid input")
        return
    ValidWord = False
    with open("Allowed Words", "r") as AllowedWords:
        for line in AllowedWords:

            if line.strip() == Input:
                ValidWord = True
    if not ValidWord:
        print("Please enter a valid word")
        return
    for i in range(0,5):
        Found = False
        if Input[i] == WordTable[i]:
            Found = True
            Root.grid_slaves(row=Turn, column=i)[0].config(text = Input[i],bg = "green")
            WordTable[i] = ""
        else:
            for v in range(0, 5):
                if Input[i] == WordTable[v]:
                    Root.grid_slaves(row=Turn, column=i)[0].config(text=Input[i], bg="yellow")
                    WordTable[v] = ""
                    Found = True
            if not Found:
                Root.grid_slaves(row=Turn, column=i)[0].config(text=Input[i], bg="grey")
    if Input==RandomWord.strip():
        print("You Won!")
        myButton.config(command=NONE)
    Turn += 1
    if Turn>5:
        print("Game Over,the word was "+ RandomWord.strip()+"!")
        myButton.config(command=NONE)


myInput = Entry(text = "",width = 10)
myInput.insert(0,"Word Here")


myButton = Button(text = "Submit",width = 10,command=func)
myButton.grid(row = 7,column = 2)
myInput.grid(row = 6,column = 2)
def func2():

    global Turn
    global RandomWord
    global RandomNum
    myButton.config(command=func)
    print("The word was " + RandomWord)
    Turn = 0
    for item in WordleTable:
        item.config(text = "",bg= "grey")
    RandomNum = random.randint(0, 2309)
    with open("Possible Words", "r") as PossibleWords:
        for i in range(0, RandomNum):
            PossibleWords.readline()

        RandomWord = PossibleWords.readline()
resetButton = Button(text = "Reset",width = 10,command=func2)

resetButton.grid(row = 7,column = 3)
myInput.bind('<FocusIn>', lambda x: myInput.selection_range(0, END))
Root.mainloop()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
