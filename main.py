#importing
import tkinter
from tkinter import messagebox
import customtkinter

#software screen size
screen = customtkinter.CTk()
screen.title("Modern Calculator")
screen.geometry("260x260")
#screen theme
customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")

#Font Style
font1 = ("Arial", 20,"bold")


#function
def button_click(number):
    entry.insert(tkinter.END, number)

def clear_fun():
    entry.delete(0,tkinter.END)

#equation function
def calculate():
    
        equation = entry.get()
        new_equation = equation.replace("x","*")
        result = eval(new_equation)
        clear_fun()
        entry.insert(0, result)



#Entry screen
entry = customtkinter.CTkEntry(screen, width=240, height= 40, text_color="#fff",font=font1, border_color="#ff5a8c")
entry.place(x=10, y=30)

#Number Button
num1 = customtkinter.CTkButton(screen,command=lambda:button_click("1"), width=40,height=15,text="1", fg_color="#ff1493",font=font1)
num1.place(x=10, y =80)
num2 = customtkinter.CTkButton(screen,command=lambda:button_click("2"), width=40,height=15,text="2", fg_color="#ff1493",font=font1)
num2.place(x=60, y =80)
num3 = customtkinter.CTkButton(screen,command=lambda:button_click("3"), width=40,height=15,text="3", fg_color="#ff1493",font=font1)
num3.place(x=110, y =80)
num4 = customtkinter.CTkButton(screen,command=lambda:button_click("4"), width=40,height=15,text="4", fg_color="#ff1493",font=font1)
num4.place(x=10, y =120)
num5 = customtkinter.CTkButton(screen,command=lambda:button_click("5"), width=40,height=15,text="5", fg_color="#ff1493",font=font1)
num5.place(x=60, y =120)
num6 = customtkinter.CTkButton(screen,command=lambda:button_click("6"), width=40,height=15,text="6", fg_color="#ff1493",font=font1)
num6.place(x=110, y =120)
num7 = customtkinter.CTkButton(screen,command=lambda:button_click("7"), width=40,height=15,text="7", fg_color="#ff1493",font=font1)
num7.place(x=10, y =160)
num8 = customtkinter.CTkButton(screen,command=lambda:button_click("8"), width=40,height=15,text="8", fg_color="#ff1493",font=font1)
num8.place(x=60, y =160)
num9 = customtkinter.CTkButton(screen,command=lambda:button_click("9"), width=40,height=15,text="9", fg_color="#ff1493",font=font1)
num9.place(x=110, y =160)
num0 = customtkinter.CTkButton(screen,command=lambda:button_click("0"), width=40,height=15,text="0", fg_color="#ff1493",font=font1)
num0.place(x=160, y =160)
point = customtkinter.CTkButton(screen,command=lambda:button_click("."), width=40,height=15,text=".", fg_color="#ff1493",font=font1)
point.place(x=210, y =160)

#Operator Button
sum = customtkinter.CTkButton(screen,command=lambda:button_click("+"),width=40,height=15,text="+", fg_color="#FF4500",font=font1)
sum.place(x= 160, y=80)
sub = customtkinter.CTkButton(screen,command=lambda:button_click("-"),width=40,height=15,text="-", fg_color="#FF4500",font=font1)
sub.place(x= 210, y=80)
mul = customtkinter.CTkButton(screen,command=lambda:button_click("x"),width=40,height=15,text="x", fg_color="#FF4500",font=font1)
mul.place(x= 160, y=120)
div = customtkinter.CTkButton(screen,command=lambda:button_click("/"),width=40,height=15,text="/", fg_color="#FF4500",font=font1)
div.place(x= 210, y=120)

#Clear Button
clear = customtkinter.CTkButton(screen,command=clear_fun, width=40,height=15,text="C", text_color="#fff",font=font1)
clear.place(x=210,y = 200)
#Submit Button
submit1 = customtkinter.CTkButton(screen,command=calculate, width=190,height=15,text="=", text_color="#fff",font=font1)
submit1.place(x=10, y=200)

#Result Screen



#loop for not exit the GUI
screen.mainloop()


