import tkinter as tk

calcWindow = tk.Tk()  # initialize the main window
calcWindow.title("Calculator") #name the window

# create all the number buttons
buttons = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "0"]

#create the operation buttons
opBut = ["/","*","-","+"]

#create entry list
userEntry=[]

#initialize the entry box
entryBox = tk.Text(height=1, width=12, font=('Arial', 35), wrap='none')
entryBox.grid(row=0, column=0, columnspan=5, rowspan=2)


#adds the number pressed to the list
def addNum(button):
    userEntry.append(button)
    entryBox.insert(tk.END, button)

#adds the operation to the list
def addOpp(ops):
    userEntry.append(ops)
    entryBox.insert(tk.END, ops)

#converts the entry into a string and evaluate
def evaluate():
    finalNum =''.join(userEntry)
    result = eval(finalNum)
    entryBox.delete(1.0, tk.END)
    entryBox.insert(tk.END, result)
    
def clear():
    userEntry.clear()
    entryBox.delete(1.0, tk.END)

#start the row and column counter at zero
i=4
j=0

#initialize each button
for button in buttons:
    tk.Button(text=str(button), width=10, height=5,command=lambda b=button: addNum(b)).grid(row=i, column=j)
    j+=1
    
    #since we only want 3 columns, if j exceeds 2, we will reset the column counter and increase row
    if j>2:
        j=0
        i+=1
        
#reset the values of i and j for the operator buttons
i=3

for ops in opBut:
    tk.Button(text=ops, width=10, height=5,command=lambda b=ops: addOpp(b)).grid(row=i, column=4)
    i+=1

#initialze the equals button seperately, since it performs mutiple other functions
equalsButton = tk.Button(text="=", command=evaluate, width=10, height=5)
equalsButton.grid(row=7, column=4)

#initialize clear button
clearButton = tk.Button(text='C', command=clear, width=10, height=5)
clearButton.grid(row=2, column=2, columnspan=1, rowspan=2)

calcWindow.mainloop()  # start the main event loop 