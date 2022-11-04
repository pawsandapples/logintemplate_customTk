from tkinter import *

from tkinter import Tk
from tkinter import messagebox
import customtkinter
import tkinter.font

from data import *

#colors``
__bgcolour = "#151515"
__hovercolour = "#404258"
__dimgrey = "#696969"
__error = "#F96666"
__placeholdercolours = "#808080"
__whitecolour = "#FFFFFF"
__entrycolour = "#404258"
__haveacc = "#6C4AB6"


#Special characters list to aware incorrect symbols in login. "' included.
special_characters = '"'
special_characters2 = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "
numbers = "1234567890"
alphabet = "qwertyuiopasdfghjklzxcvbnm"




window = customtkinter.CTk()
window.title("@pawsandapples")
window.geometry(f"{1260}x{600}")
window.resizable(width=False, height=False)
window.configure(fg_color=__bgcolour)

icon = PhotoImage(file="img/apple.png")
window.iconphoto(False, icon)


# frames

registrationframe = Frame(window, width=1260, height=600, bg=__bgcolour)
registrationframe.pack(padx=20, pady=100)

loginframe = Frame(window, width=1260, height=600, bg=__bgcolour)


#Fonts

username_font = tkinter.font.Font(family = "Poppins", 
                                 size = 12, 
                                 weight = "normal")

password_font = tkinter.font.Font(family = "Poppins", 
                                 size = 12, 
                                 weight = "normal")

loginReg_font = tkinter.font.Font(family = "Poppins", 
                                 size = 12, 
                                 weight = "normal")

passwordReg_font = tkinter.font.Font(family= "Poppins",
                                    size = 12,
                                    weight="normal")


username = customtkinter.CTkLabel(master=loginframe,
                                height=25,
                                text="Login",
                                text_font= username_font,
                                corner_radius=8)


e_name = customtkinter.CTkEntry(master=loginframe,
                                placeholder_text="Enter Login",
                                width=400,
                                height=25,
                                placeholder_text_color=__placeholdercolours,
                                fg_color=__entrycolour,
                                border_width=1,
                                corner_radius=10)


    #Password, login section.

password = customtkinter.CTkLabel(master=loginframe,
                                height=25,
                                text="Password",
                                text_font= password_font,
                                corner_radius=8)


e_password = customtkinter.CTkEntry(master=loginframe,
                                placeholder_text="Enter Password",
                                width=400,
                                fg_color=__entrycolour,
                                height=25,
                                placeholder_text_color=__placeholdercolours,
                                border_width=1,
                                corner_radius=10)

username.pack(padx=20, pady=10)
e_name.pack(padx=20, pady=5)
password.pack(padx=20, pady=10)
e_password.pack(padx=20, pady=5)


#Login, registration section.

LoginReg = customtkinter.CTkLabel(master=registrationframe,
                               height=25,
                               text="Create Login",
                               text_font=loginReg_font,
                               corner_radius=8)
LoginReg.pack(padx=20, pady=10)

e_LoginReg = customtkinter.CTkEntry(master=registrationframe,
                               placeholder_text="Create Login",
                               width=400,
                               height=25,
                               text_color=__whitecolour,
                               border_width=1,
                               fg_color=__entrycolour,
                               placeholder_text_color=__placeholdercolours,
                               corner_radius=10)
e_LoginReg.pack(padx=20, pady=5)

#Password, registration section.
passwordReg = customtkinter.CTkLabel(master=registrationframe,
                               height=25,
                               text="Create Password",
                               text_font=passwordReg_font,
                               corner_radius=8)
passwordReg.pack(padx=20, pady=10)

e_passwordReg = customtkinter.CTkEntry(master=registrationframe,
                               placeholder_text="Create Password",
                               width=400,
                               fg_color=__entrycolour,
                               height=25,
                               border_width=1,
                               placeholder_text_color=__placeholdercolours,
                               corner_radius=10)
e_passwordReg.pack(padx=20, pady=5)

#OutputThing


thing_font = tkinter.font.Font(family= "Tw Cen MT",
                                    size = 9,
                                    weight="normal")

OutputThing = customtkinter.CTkLabel(master=registrationframe,
                               height=12,
                               text="",
                               text_font=thing_font,
                               text_color=__error,
                               corner_radius=8)
OutputThing.pack(ipadx=0, ipady=5)

thing_font = tkinter.font.Font(family= "Tw Cen MT",
                                    size = 9,
                                    weight="normal")

OutputThingLogin = customtkinter.CTkLabel(master=loginframe,
                               height=12,
                               text="",
                               text_font=thing_font,
                               text_color=__error,
                               corner_radius=8)
OutputThingLogin.pack(ipadx=0, ipady=5)

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------

cb_font = tkinter.font.Font(family = "Poppins", 
                                 size = 8, 
                                 weight = "normal")

checkbox = customtkinter.CTkCheckBox(master=registrationframe, text="I accept ToS",text_font=cb_font, onvalue="on",width=20, height=20, border_width=1, offvalue="off", hover_color=__whitecolour)
checkbox.pack(padx=20, pady=5)

#bad english l
#def register() contains code what will take care of most things and warning user when something wrong. Like special symbols in special_characters(2)
#Also it check if e_LoginReg or e_passwordReg contain nothing, instead of succesfully add new *blank account* you will get warning/error about it.
#enDi meaning [Ending of I], i using here to check every value in list AccountsUsernames and show error if inputed login already exist.
def ClearErrorLabels():
    OutputThing.configure(text="")
    e_LoginReg.configure(border_color=__placeholdercolours, text_color=__placeholdercolours, placeholder_text_color=__placeholdercolours)
    OutputThingLogin.configure(text="")
    e_passwordReg.configure(border_color=__placeholdercolours, text_color=__placeholdercolours, placeholder_text_color=__placeholdercolours)

def RegistrationLoginEntryError():
    e_LoginReg.configure(border_color=__error, text_color=__error, placeholder_text_color=__error)

def RegistrationPasswordEntryError():
    e_passwordReg.configure(border_color=__error, text_color=__error, placeholder_text_color=__error)

def LoginError():
    e_password.configure(border_color=__error, text_color=__error, placeholder_text_color=__error)
    e_name.configure(border_color=__error, text_color=__error, placeholder_text_color=__error)

def checkboxerror():
    checkbox.configure(border_color=__error)

def ClearEntrys():
    e_LoginReg.delete(0, END)
    e_passwordReg.delete(0, END)
    e_name.delete(0, END)
    e_password.delete(0, END)

def loginframe_open():
    ClearErrorLabels()
    registrationframe.pack_forget()
    loginframe.pack(padx=20, pady=100)

def registrationframe_open():
    ClearErrorLabels()
    loginframe.pack_forget()
    registrationframe.pack(padx=20, pady=100)

def register():
    name = e_LoginReg.get()
    password = e_passwordReg.get()
    enDi = len(AccountsUsernames)
    i = 0

    #If e_LoginReg contain nothing OR any of special characters in specific list, it will occur an error.
    if not e_LoginReg.get():
        ClearErrorLabels()
        OutputThing.configure(text="You must enter login.")
        RegistrationLoginEntryError()
    elif any(c in special_characters for c in name) or any(c in special_characters2 for c in name):
        ClearErrorLabels()
        OutputThing.configure(text="Login contain unsupported symbols, please try another.")
        RegistrationLoginEntryError()


    #If login is right it will check if you entered atleast any password.
    elif any(c in numbers for c in name) and not any(c in alphabet for c in name):
        ClearErrorLabels()
        OutputThing.configure(text="Login can't contain only numbers.")
        RegistrationLoginEntryError()
    else:
        if not e_passwordReg.get():
            ClearErrorLabels()
            OutputThing.configure(text="You must enter the password to create an account!")
            RegistrationPasswordEntryError()
        else:
            #This *while* check if entered login already exist is list.
            #~81
            while i != enDi:
                if name.lower() == AccountsUsernames[i]:
                    ClearErrorLabels()
                    OutputThing.configure(text="This login already exist! Please try another.")
                    RegistrationLoginEntryError()
                    break
                else:
                    i = i + 1
            if i == enDi:
                if checkbox.get() == "on":
                    ClearErrorLabels()
                    ConfirmRegistration = messagebox.askquestion('Registration', 'Are you sure want to create account named ' + name + '?',icon='warning')
                    if ConfirmRegistration == 'yes':
                        ClearErrorLabels()
                        AccountsUsernames.append(name.lower())
                        AccountsPasswords.append(password)
                        ClearEntrys()
                        messagebox.showinfo('Registration', 'Successfully added new account: ' + name)
                        print(AccountsUsernames[i], AccountsPasswords[i])
                elif checkbox.get() == "off":
                    ClearErrorLabels()
                    OutputThing.configure(text="You should accept ToS before creating account",text_color=__error)
                    checkboxerror()

def CheckLogin():
    #Getting values of entry-boxes
    name = e_name.get().lower()
    password = e_password.get()
    
    #If e_name contain nothing, program shows error.
    if not e_name.get() or not e_password.get():
        ClearErrorLabels()
        LoginError()
        OutputThingLogin.configure(text="Incorrect login or password",text_color=__error)

    #If e_name not in AccountsUsernames' or AccountsPasswords' list, program shows error. 
    elif name not in AccountsUsernames or password not in AccountsPasswords:
        ClearErrorLabels()
        LoginError()
        OutputThingLogin.configure(text="Incorrect login or password",text_color=__error)

    #If e_name and e_password match each other program will briefly welcome you.
    else:
        if name == AccountsUsernames[AccountsUsernames.index(name)] and password == AccountsPasswords[AccountsPasswords.index(password)]:
            ClearEntrys()
            messagebox.showinfo('Login', 'Welcome Back ' + name)

def CheckLoginReturn(event):
    #Getting values of entry-boxes
    name = e_name.get().lower()
    password = e_password.get()
    
    #If e_name contain nothing, program shows error.
    if not e_name.get() or not e_password.get():
        ClearErrorLabels()
        OutputThingLogin.configure(text="Incorrect login or password",text_color=__error)

    #If e_name not in AccountsUsernames' or AccountsPasswords' list, program shows error. 
    elif name not in AccountsUsernames or password not in AccountsPasswords:
        ClearErrorLabels()
        OutputThingLogin.configure(text="Incorrect login or password",text_color=__error)

    #If e_name and e_password match each other program will briefly welcome you.
    else:
        if name == AccountsUsernames[AccountsUsernames.index(name)] and password == AccountsPasswords[AccountsPasswords.index(password)]:
            ClearEntrys()
            messagebox.showinfo('Login', 'Welcome Back ' + name)
window.bind('<Return>', CheckLoginReturn)


#buttons
#Add register button command(s)

button_REGconfirm = customtkinter.CTkButton(master=registrationframe,
                                 width=120,
                                 height=32,
                                 border_width=1,
                                 corner_radius=8,
                                 text="Create Account",
                                 border_color=__dimgrey,
                                 hover_color=__hovercolour,
                                 fg_color=__bgcolour,
                                 command=register)
button_REGconfirm.pack(padx=20, pady=5)

button_confirm = customtkinter.CTkButton(master=loginframe,
                                 width=120,
                                 height=32,
                                 border_width=1,
                                 corner_radius=8,
                                 text="Login",
                                 fg_color=__bgcolour,
                                 border_color=__dimgrey,
                                 hover_color=__hovercolour,
                                 command=CheckLogin)

button_confirm.pack(padx=20, pady=15)

AlreadyHaveAnAccountButton = customtkinter.CTkButton(master=registrationframe,
                                 width=9,
                                 height=9,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Already have an account",
                                 text_color=__haveacc,
                                 hover = False,
                                 fg_color=__bgcolour,
                                 command=loginframe_open)
AlreadyHaveAnAccountButton.pack(padx=50, ipady=10)

BackToReg = customtkinter.CTkButton(master=loginframe,
                                 width=12,
                                 height=9,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Back to Registration",
                                 text_color=__haveacc,
                                 hover = False,
                                 fg_color=__bgcolour,
                                 command=registrationframe_open)
BackToReg.pack(padx=50, ipady=10)



window.mainloop()