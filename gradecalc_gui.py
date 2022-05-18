import tkinter
from gradecalc import gradecalc

def onClick():
    name = nBox.get()
    h = int(hBox.get())
    a = int(aBox.get())
    f = int(fBox.get())
    result = gradecalc(name, h, a, f)
    label = tkinter.Label(root, text = result, background='White', padx=1.5, pady=2, relief='ridge')
    label.grid(row = 5, column = 2)
    

root = tkinter.Tk()

title = tkinter.Label(root, text = "Grade Calculator")
nBox = tkinter.Entry(root)
hBox = tkinter.Entry(root)
aBox = tkinter.Entry(root)
fBox = tkinter.Entry(root)

nBox.grid(row = 1, column = 1)
hBox.grid(row = 2, column = 1)
aBox.grid(row = 3, column = 1)
fBox.grid(row = 4, column = 1)

nLabel = tkinter.Label(root, text = "Name: ")
labelOne = tkinter.Label(root, text = "Homework (/25): ")
labelTwo = tkinter.Label(root, text = "Assessment (/50): ")
labelThree = tkinter.Label(root, text = "Exam (/100): ")
buttonOne = tkinter.Button(root, text = "Calculate", command = onClick)

nLabel.grid(row = 1, column = 0)
labelOne.grid(row = 2, column = 0)
labelTwo.grid(row = 3, column = 0)
labelThree.grid(row = 4, column = 0)

title.grid(row = 0, column = 0)
buttonOne.grid(row = 5, column = 1)

root.mainloop()