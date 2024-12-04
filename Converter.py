from tkinter import *
import tkinter.font as font

def convert():
    temp_celsius = celsius_value.get()

    if(temp_celsius.replace('.','',1).isdigit()):
        error_msg.grid_forget()
        temp_farenheit = (float(temp_celsius) *9/5) +32
        t.config(text= 'Temperature in Farenheit :' + str(temp_farenheit))


    else :
        error.msg.grid(row=1 , column = 1)


    my_window=Tk()
    my_window.title("Celsius to Farenheit Converter")

        #displaying the heading inside the window
    description = Label(text= 'Celsius -> Farenheit',font=font.Font(size=20), fg="grey")
    description.pack()

    frame=Frame(my_window)
    frame.pack(pady = 20)

    message_one=Label(gui, text = "Enter temperature in celsius", bg="light grey", font = font.Font("times",10))
    message_one.grid(row=0, column= 0)

    celsius_value = Entry(frame)
    celsius_value.grid(row=0, column=1)

    error_msg= Label(frame, text = 'Please enter valid input...', font=font.Font(size=8), fg='red')

    output_farenheit = Label(frame, font.Font(size=12))
    output_farenheit.grid(row=2, column=0, columnspan = 2,pady=10)

    submit_btn = Button(frame, text='Convert', width= 30, fg = "black", bg =  "light green", bd=0, padx=20, pady=10, command = convert)
    submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

    my_window.geometry('500x250')
    my_window.mainloop()
