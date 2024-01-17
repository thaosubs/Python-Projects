# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:28:38 2024

@author: Thao Tran
"""
import pandas as pd
from collections import Counter
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import ttk

#initialize the main window
mainWin = tk.Tk()
mainWin.title("Expense Tracker")
mainWin.geometry("700x500")
#define the list of categories of spending
categories = ["Bills", "Groceries", "Shopping", "Other"]
#create an object to store the dropdown selection
selected_cat = tk.StringVar(mainWin)
#set the dropdown menu text
selected_cat.set("Select a category...")
    
#allow the user to enter in the expense, date, and category
expenseBox = tk.Entry()
dateBox = DateEntry(mainWin,selectmode='day')
category_menu = tk.OptionMenu(mainWin, selected_cat, *categories)

#set counter at 0
i = 0

#define the function that checks if an input is a number
def isNumber(entry):
    try:
        float(entry)
        return True
    except ValueError:
        return False
    
#defines the function to add expenses to the table and dictionary
def addExpense():
    global i
    #retrieve the user entered value from each box and insert it into the table
    expense = expenseBox.get()
    if isNumber(expense) == False:
        expense = 000
    #ensure the user entry is in 0.00 format
    expense = "{:.2f}".format(float(expense))
    date = dateBox.get()
    category = selected_cat.get()
    #create a new dictionary item
    newItem = (date, expense, category)
    #insert the item at the i-th index
    expDic[i] = newItem
    #insert the values into the table into their respective columns
    table.insert("", "end", values=(date, expense, category))
    #increment counter by one
    i +=1
    #run the total
    addTotal()
    topCat()
    #print the dictionary for coding purposes
    print(expDic)

#defines a function that will reset the table, counter, and dictionary
def resetTable():
    global expDic
    #go through every item in the table and delete them 
    for i in table.get_children():
        table.delete(i)
    #reset dictionary
    expDic = {}
    #reset counter
    i = 0
    tk.Label(text="{:.2f}".format(0)).place(x=335, y=10)
    catVar.set("N/A")

#defines a function that will take each value from the expense column and add it up
def addTotal():
    #start the total at 0
    total = 0
    #iterate through each item in the table and sum up the expenses
    for i in table.get_children():
        expense = float(table.item(i, 'values')[1])  # Assuming 'Expense' column is at index 1
        total += expense
    tk.Label(text="{:.2f}".format(total)).place(x=335, y=10)

def topCat():
    bills = 0 
    shopping = 0
    groceries = 0 
    other = 0 
    for value in expDic.values():
        if value[2] == "Bills":
            bills += 1
        elif value[2] == "Shopping":
            shopping += 1
        elif value[2] == "Groceries":
            groceries += 1
        elif value[2] == "Other":
            other += 1

    
    if max(bills, shopping, groceries, other) == bills:
        catVar.set("Bills")
    elif max(bills, shopping, groceries, other) == shopping:
        catVar.set("Shopping")
    elif max(bills, shopping, groceries, other) == groceries:
        catVar.set("Groceries")
    elif max(bills, shopping, groceries, other) == other:
        catVar.set("Other")

#initialize the dictionary that will contain each expense with its properties
expDic = {}

#create the table for the expenses and name each header
table = ttk.Treeview(mainWin, columns=("Date", "Expense", "Category"), show="headings")
table.heading("Date", text="Date")
table.heading("Expense", text="Expense")
table.heading("Category", text="Category")

#Allow the user to choose between different options (e.g., add expense, view expenses, exit).
addBut = tk.Button(text="Add", command=addExpense, width=10)
resetBut = tk.Button(text="Reset", command=resetTable)

#place buttons
tk.Label(text="Expense: ").place(x=5, y=40)
expenseBox.place(x=60, y=40)

tk.Label(text="Date: ").place(x=5, y=10)
dateBox.place(x=60, y=10)

category_menu.place(x=60, y=70)
addBut.place(x=60, y=110)
resetBut.place(x=300, y=150)

#place table
table.place(x=50, y=200)

tk.Label(text="Total : ").place(x=300, y=10)
tk.Label(text="Top category spent in : ").place(x=300, y=30)

catVar = tk.StringVar()
catVar.set("N/A")
catLabel = tk.Label(mainWin, textvariable=catVar).place(x=450, y=30)

#start main loop event

mainWin.mainloop()