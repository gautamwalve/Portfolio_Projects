from msilib.schema import Font
from tkinter import messagebox #message box
import tkinter as tk # importing tkinter
from  tkinter import ttk
import datetime as dt
import os
from csv import DictWriter
from turtle import st
import re
from typing_extensions import Self
from wsgiref import validate
from tkinter import *


#------------------------------------------------------------------------------
#Setting up Plate and Size
# Creating Main Window
win = tk.Tk() # main window
win.title ("Cold Lead Capture module") # Header title
win.geometry ('600x250+300+200')
win.resizable(width=False,height = False)

#------------------------------------------------------------------------------
#Tabbing Details
tab_parent = ttk.Notebook(win)
tab0 = ttk.Frame(tab_parent)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab_parent.add(tab0 ,text = "Information") # Adding Child argument
tab_parent.add(tab1 ,text = "Lead Generator") #Adding Child argument
tab_parent.add(tab2 ,text = "Loan Calculator") #Adding Child argument
tab_parent.grid()
#------------------------------------------------------------------------------
#Date maker - shows and captures the date of entry

date_var =dt.datetime.now()
date_var2 = str(date_var)
text2=f"{date_var:%B %d,%Y %A}"
dt_label = ttk.Label(tab1,text = "Date at time of Entry: ",font =("bahnschrift",13)).grid(row = 1, column = 0, sticky = tk.W)
date_label = ttk.Label(tab1,text =f"{date_var:%A,%B %d,%Y}",font =("bahnschrift",13)).grid(row = 1,column=1,sticky = tk.W)
#------------------------------------------------------------------------------
#Labels
name_label = ttk.Label(tab1,text = "Enter Customer's Name: ",font =("bahnschrift",13)).grid(row = 3, column = 0, sticky = tk.W)
phone_label = ttk.Label(tab1,text = "Enter Contact no.: ",font =("bahnschrift",13)).grid(row = 9, column = 0, sticky = tk.W)
email_label = ttk.Label(tab1,text = "Enter Email ID.: ",font =("bahnschrift",13)).grid(row = 17, column = 0, sticky = tk.W)
lead_label = ttk.Label(tab1,text = "Customer's Requirement : ",font =("bahnschrift",13)).grid(row = 22, column = 0, sticky = tk.W)
followup_label = ttk.Label(tab1,text = "Follow up Date : ",font =("bahnschrift",13)).grid(row = 29, column = 0, sticky = tk.W)
#------------------------------------------------------------------------------
#Buttons

#NAME:
name_var = tk.StringVar(value = "Enter Customers Name",)
name_entrybox = ttk.Entry(tab1,width=60,textvariable=name_var).grid(row = 3, column = 1, sticky = tk.W)
#Phone number:
num_var = tk.StringVar(value="Input Valid Phone Number")
num_entrybox = ttk.Entry(tab1,width=40,textvariable=num_var).grid(row = 9, column = 1,ipadx=50 ,sticky = tk.W)
def disp_val():
    try:
        disp = len(str(num_var.get()))
        disp_error = tk.Label(tab1, text=disp, width="2", bd="0", justify="center", fg="white", bg='black',font =("bahnschrift",11)).grid(row=9,column=1,
                                                                                                                 sticky=tk.E)
        tab1.after(10, disp_val)
    except Exception:
        return tab1.after(100, disp_val)
disp_val()
#Email ID:
email_var = tk.StringVar(value ='Enter Valid Email ID')
email_entrybox = ttk.Entry(tab1,width=60,textvariable=email_var)
email_entrybox.grid(row = 17, column = 1, sticky = tk.W)
#LEAD types
lead_var = tk.StringVar()
lead_entrybox = ttk.Combobox(tab1,width = 57,textvariable=lead_var,state='readonly')
lead_entrybox['values'] = (
    'Select the File Type',
    'Home Loan','Personal Loan','Loan Against Property',
    'SME Loan','Balance Transfer','Self Construction',
    'Plot Loan','Re-Finance','Machinery Loan'
    )
lead_entrybox.current(0)
lead_entrybox.grid(row=22, column=1, sticky=tk.W)
#Followup
date_var = tk.StringVar(value="DD-MM-YYYY")
date_btn = ttk.Entry(tab1, width=60,textvariable=date_var)
date_btn.grid(row=29, column=1, sticky=tk.W)
# Check button for subscription
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(tab1, text="Select if the customer wants to be followed up ",var=checkbtn_var).grid(row=30, columnspan=4, sticky=tk.W)

#code for Submit button
def action():  # sourcery skip: use-fstring-for-concatenation
    userName = name_var.get() # for customer name
    try:
        userNumber = num_var.get() # for Ensuring the number is non-number
    except Exception:
        messagebox.showinfo("Input Error","Phone number cannot be non-numeric")
    userEmail = email_var.get() # for email capturing
    userLead = lead_var.get() # for type of lead
    userDate = date_var.get() # for date capturing
    follow_up = "Yes" if checkbtn_var.get() == 1 else "No"
    try:
        print(userName,userNumber,userEmail,userLead,userDate,follow_up)
    except Exception:
        return action

#Printing to FIle
    with open( f"Cold Leads Generated for {text2}.csv", 'a', newline = '') as f:
    #Writing headers
        headers = ['Log Date','Customer Name','Contact Number','Contact Email','Lead Type','Follow up Lead','call back on']
        writer  = DictWriter(f,fieldnames = headers)
        if os.stat(f"Cold Leads Generated for {text2}.csv").st_size == 0:
            writer.writeheader()
        #Writing Rows
        writer.writerow(
        {'Log Date':text2,'Customer Name':userName,'Contact Number':userNumber,'Contact Email':userEmail,'Lead Type':userLead,
         'Follow up Lead':follow_up,'call back on':userDate})

"""#Resetting details
name_entrybox.delete(0,tk.End)
num_entrybox.delete(0,tk.End)
email_entrybox.delete(0,tk.End)
date_btn.delete(0,tk.End)"""
#Tab 01
info = ttk.Label(tab0, text="""Author's Name: Gautam Walve \nFile Name: Lead File Generator \n Publishing Month: February 2021 \nVersion:1.5 \nUpdate Logs: 
>> Tabs Added for extra Functionalities
>> Capturing of the Date can now be done via Calender
>> Message Box Information now displayed in Tab""",font =("bahnschrift",13)).grid(row = 1,column = 2)
#Submit and Clear Button
submit = ttk.Button(tab1, text="Submit",command = action).grid(row=32, column=0, sticky=tk.W)
#clear = ttk.Button(tab1, text="Reset",command = delete).grid(row=32, column=1, sticky=tk.W)
#E-O-D
win.mainloop()