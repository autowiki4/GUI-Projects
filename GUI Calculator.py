import tkinter
from tkinter import END

sample_app = tkinter.Tk()
sample_app.title('GUI Calculator')

# change the icon for the title of GUI window
# must be an icon image type with file extension '.ico'
sample_app.iconbitmap('959091.ico')

# Entries
entry = tkinter.Entry(width=15,font=('bahnschrift',20),borderwidth=5) # You can only adjust width

# Function to enter the numbers
def calcul(input):
    # get the length of string in entry
    no_character_in_entry = len(entry.get())
    # add number after the current text being held in case teh number is a multi-digit number
    entry.insert(no_character_in_entry,input)

''' the 'math' variable helps the program to know which operatoin is currently being carried out'''

# add function
def add():
    global f_num
    global  math
    math = 'add'
    # store the first number involved in the arithmetic operation
    f_num = int(entry.get())
    entry.delete(0,END)

# subtract function
def subtract():
    global f_num
    global math
    math = 'subtract'
    f_num = int(entry.get())
    entry.delete(0, END)

# multiply function
def  multiply():
    global f_num
    global math
    math = 'multiply'
    f_num = int(entry.get())
    entry.delete(0, END)

# divide funtion
def divide():
    global f_num
    global math
    math = 'divide'
    f_num = int(entry.get())
    entry.delete(0, END)

# create list to store results
output_list = []
length = len(output_list)

# function to give output
def result():
    # store the second number
    s_num = int(entry.get())
    entry.delete(0,END)

    if math == 'add':
        entry.insert(0,f"{f_num} + {s_num} = {f_num + s_num}")
    elif math == 'subtract':
        entry.insert(0,f"{f_num} - {s_num} = {f_num - s_num}")
    elif math == 'multiply':
        entry.insert(0,f"{f_num} x {s_num} = {f_num * s_num}")
    elif math == 'divide':
        entry.insert(0,f"{f_num} ÷ {s_num} = {f_num / s_num}")

    # collect the current result on the screen and store it
    output = entry.get()
    output_list.append(output)

# clear entry
def delete():
    entry.delete(0,END)

# clear all evidence of previous calculations
def dlt_list():
    entry.delete(0,END)
    output_list.clear()

# view previous calculations
def pre_output():
    # length of list of calculations
    length = len(output_list)

    # if no output has been stored, i.e. no calculation has been done
    if length == 0:
        pass

    elif length > 0:
        if entry != '':
            current_index = output_list.index(entry.get())
            if current_index > 0:
                entry.delete(0, END)
                entry.insert(0, output_list[current_index-1])
            else:
                pass
        else:
            pass

# view subsequent calculations
def post_ouput():
    # length of list of calculations
    length = len(output_list)

    # if no output has been stored, i.e. no calculation has been done
    if length == 0:
        pass

    elif length > 0:
        if entry != '':
            current_index = output_list.index(entry.get())
            if current_index < length - 1:
                entry.delete(0, END)
                entry.insert(0, output_list[current_index + 1])
            elif current_index == length - 1:
                entry.delete(0, END)
            else:
                pass
        else:
            pass

# Buttons
btn_7 = tkinter.Button(text='7',font=('bahnschrift',25),fg='#fff',bg='#000',command=lambda:calcul("7"))
btn_8 = tkinter.Button(text='8',font=('bahnschrift',25),fg='#fff',bg='#000',command=lambda:calcul("8"))
btn_9 = tkinter.Button(text='9',font=('bahnschrift',25),fg='#fff',bg='#000',command=lambda:calcul("9"))
btn_4 = tkinter.Button(text='4',font=('bahnschrift',25),fg='#fff',bg='#000',command=lambda:calcul("4"))
btn_5 = tkinter.Button(text='5',font=('bahnschrift',25),fg='#fff',bg='#000',command=lambda:calcul("5"))
btn_6 = tkinter.Button(text='6',font=('bahnschrift',25),fg='#fff',bg='#000',command=lambda:calcul("6"))
btn_1 = tkinter.Button(text='1',font=('bahnschrift',25),fg='#fff',bg='#000',width=2,command=lambda:calcul("1"))
btn_2 = tkinter.Button(text='2',font=('bahnschrift',25),fg='#fff',bg='#000',command=lambda:calcul("2"))
btn_3 = tkinter.Button(text='3',font=('bahnschrift',25),fg='#fff',bg='#000',command=lambda:calcul("3"))
btn_0 = tkinter.Button(text='0',font=('bahnschrift',25),fg='#fff',bg='#000',command=lambda:calcul("0"))
btn_add = tkinter.Button(text='+',font=('bahnschrift',25),fg='#fff',bg='#000', command=add)
btn_subtract = tkinter.Button(text='-',font=('bahnschrift',25),fg='#fff',bg='#000', command=subtract)
btn_times = tkinter.Button(text='x',font=('bahnschrift',25),fg='#fff',bg='#000', command=multiply)
btn_divide = tkinter.Button(text='÷',font=('bahnschrift',25),fg='#fff',bg='#000', command=divide)
btn_equal = tkinter.Button(text='=',font=('bahnschrift',25),fg='#fff',bg='#000', command=result)
btn_clear = tkinter.Button(text='C',font=('bahnschrift',25),fg='#fff',bg='#000', command=lambda :delete())
btn_delete_list = tkinter.Button(text='CE',font=('bahnschrift',15),height=1,width=8,fg='#fff',bg='#000',command=dlt_list)
btn_previous_output = tkinter.Button(text='PRE',font=('bahnschrift',10),width=4,fg='#fff',bg='#000',command=pre_output)
btn_next_output = tkinter.Button(text='NEX',font=('bahnschrift',10),width=4,fg='#fff',bg='#000',command=post_ouput)


# Positioning
#Counting system in python starts from 0 like 0,1,2,3,4,5,6,7,8,9...
entry.grid(row=0,column=0,columnspan=4,pady=5)
btn_7.grid(row=2,column=0,pady=5)
btn_8.grid(row=2,column=1,pady=5)
btn_9.grid(row=2,column=2,pady=5)
btn_4.grid(row=3,column=0,pady=5)
btn_5.grid(row=3,column=1,pady=5)
btn_6.grid(row=3,column=2,pady=5)
btn_1.grid(row=4,column=0,pady=5)
btn_2.grid(row=4,column=1,pady=5)
btn_3.grid(row=4,column=2,pady=5)
btn_0.grid(row=5,column=0,pady=5)
btn_add.grid(row=5,column=1,pady=5)
btn_subtract.grid(row=5,column=2,pady=5)
btn_clear.grid(row=2,column=3,pady=5)
btn_times.grid(row=3,column=3,pady=5)
btn_divide.grid(row=4,column=3,pady=5)
btn_equal.grid(row=5,column=3,pady=5)
btn_delete_list.grid(row=1,column=2,pady=5,columnspan=2)
btn_previous_output.grid(row=1,column=0,pady=5)
btn_next_output.grid(row=1,column=1,pady=5)

# Display
sample_app.mainloop()

