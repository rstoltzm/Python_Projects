import webbrowser
from selenium import webdriver
from tkinter import *

"""
#Code for customizing webbrowser, set chrome, ie path and register.

chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
ie_path="C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe"

webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
webbrowser.register('internet_explorer', None,webbrowser.BackgroundBrowser(ie_path),1)

#Use this for using a specific webbrowser
webbrowser.get(using='chrome').open(url)
"""

window=Tk()

# Color Scheme
font = '#000000'
button_color = '#F4F4F9'
label = '#BFBFBF'
background_color = '#564256'

window.configure(bg=background_color)

def Open_Chrome(url):
    webbrowser.open(url)

# Code for opening using internet explorer, need to set ie_path, and register above
def Open_Internet_Explorer(url):
    webbrowser.get(using='internet_explorer').open(url)

window.wm_title("Toolbox")
window.geometry('{}x{}'.format(200, 600))

top_frame = Frame(window, width=40, height=200, padx=3, pady=3,bg=background_color,bd=1)
top_frame.grid(row=0, column=0, sticky=W)

center_frame = Frame(window, width=40, height=200, padx=3, pady=3,bg=background_color)
center_frame.grid(row=1, column=0, sticky="W")

bottom_frame = Frame(window, width=40, height=200, padx=3, pady=3,bg=background_color)
bottom_frame.grid(row=2, column=0, sticky="W")

# Creates buttons for each link specified.
t1=Label(top_frame,text="Everyday", width=20, anchor='w',fg=label,bg=background_color,font='Helvetica 12 bold')
t1.grid(row=0,column=0,padx=8)

def Url_Top_Button(url,name,row):
    b = Button(top_frame,text=name,anchor='w',borderwidth=2, fg=font,bg=button_color, font='Helvetica 10 bold', width=20,command= lambda: Open_Chrome(url))
    b.grid(row=row,column=0,padx=10,pady=3,sticky='w')

t1=Label(center_frame,text="Bills", width=20, anchor='w',fg=label,bg=background_color,font='Helvetica 14')
t1.grid(row=0, column=0,padx=8)

def Url_Center_Button(url,name,row):
    b = Button(center_frame,text=name,anchor='w', borderwidth=2, fg=font,bg=button_color, font='Helvetica 10 bold', width=20,command= lambda: Open_Chrome(url))
    b.grid(row=row,column=0,padx=10,pady=3,sticky='w')

t1=Label(bottom_frame,text="Training", width=20, anchor='w',fg=label,bg=background_color,font='Helvetica 14')
t1.grid(row=0, column=0,padx=8)

def Url_Bottom_Button(url,name,row):
    b = Button(bottom_frame,text=name,anchor='w',  borderwidth=2, fg=font,bg=button_color, font='Helvetica 10 bold', width=20,command= lambda: Open_Chrome(url))
    b.grid(row=row,column=0,padx=10,pady=3,sticky='w')

# Insert url, name, row #
Url_Top_Button('https://mail.google.com/mail/u/0/#inbox','Gmail',1)
Url_Top_Button('https://www.amazon.com/','Amazon',2)
Url_Top_Button('https://www.reddit.com/','Reddit',3)
Url_Top_Button('https://www.bloomberg.com/','Bloomberg News',4)
Url_Top_Button('https://www.google.com','Bank',5)

Url_Center_Button('https://www.google.com','Energy',1)
Url_Center_Button('https://www.google.com','Internet',2)
Url_Center_Button('https://www.google.com','Apartment',3)
Url_Center_Button('https://www.google.com','Insurance',4)
Url_Center_Button('https://www.google.com','Credit Card',5)

Url_Bottom_Button('https://www.udemy.com/home/my-courses/learning/','Udemy',1)
Url_Bottom_Button('https://www.keybr.com/','Typing',2)
Url_Bottom_Button('https://github.com/','Github',3)
Url_Bottom_Button('https://aws.amazon.com/?nc2=h_lg','AWS',4)

window.mainloop()
