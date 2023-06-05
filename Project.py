import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json as jj
from json import *

i=1

json_dict={}

def pop_up_dict(key_in):
    
    top_frame = tkinter.LabelFrame(frame,text = "Dictionary Information")
    top_frame.grid(row=1,column=0, sticky="news", padx=20, pady=20)
    
    #top = tkinter.Toplevel(window)  
    #top_frame = tkinter.LabelFrame(top,text = "JSON Information")
    #top_frame.grid(row=0, column=0, pady=20, sticky="nw")

    
    pop_key_label = tkinter.Label(top_frame, text="KEY")
    pop_key_label.grid(row=0, column=0)

    pop_key_entry = tkinter.Entry(top_frame)
    pop_key_entry.grid(row=0,column=1)

    pop_data_label = tkinter.Label(top_frame, text="DATA")
    pop_data_label.grid(row=1, column=0)

    pop_data_entry = tkinter.Entry(top_frame)
    pop_data_entry.grid(row=1,column=1)


    def add_val2(super_key=key_in):
        print(i)
        xdata = pop_data_entry.get()
        xkey = pop_key_entry.get()
        if xdata:
                print("Key:",xkey,"Data", xdata)
                json_dict[key_in].update({xkey:xdata})
                #json_dict[key_in]={xkey:xdata}
                print(json_dict)
                print("magic")
        else:
            tkinter.messagebox.showwarning(title="Error", message="Data is missing.")
            
   
    def add_list2(super_key=key_in):
        xdata = pop_data_entry.get()
        xkey = pop_key_entry.get()
        print(xdata)
        #print(i+1)
        if xdata:
            li = list(xdata.split(","))
            print("Key:", xkey,"Data", li)
            json_dict[key_in].update({xkey:li})
            #json_dict[key_in]={xkey:li}
            print(json_dict)
        else:
            tkinter.messagebox.showwarning(title="Error", message="Either Key or Data is missing.")

    def add_dict2(super_key=key_in):
        #print(i+2)
        xdata = pop_data_entry.get()
        xkey = pop_key_entry.get()
        if xdata and super_key!=None:
                print("Key:",xkey,"Data", xdata)
                dict_o = str_to_dict(xdata)
                json_dict[key_in].update({xkey:dict_o})
                print(json_dict)
                print("magic")
        else:
            tkinter.messagebox.showwarning(title="Error", message="Either Key or Data is missing.")

    pop_button1 = tkinter.Button(top_frame, text=" Add value ", command= add_val2)
    pop_button1.grid(row=2,column=1, sticky="news", padx=20, pady=20)

    pop_button2 = tkinter.Button(top_frame, text=" Add list", command= add_list2)
    pop_button2.grid(row=2,column=2, sticky="news", padx=20, pady=20)

    pop_button3 = tkinter.Button(top_frame, text=" Add Dict", command= add_dict2)
    pop_button3.grid(row=2,column=3, sticky="news", padx=20, pady=20)
   
    pop_button4 = tkinter.Button(top_frame, text=" CLOSE", command= top_frame.destroy)
    pop_button4.grid(row=3,column=0, sticky="news", padx=10, pady=10)
    # b3 = tk.Button(my_w_child, text=' Close Child',                   command=my_w_child.destroy)
    #b3.grid(row=3,column=2)

    #top.mainloop()



def pop_up_list(key_in):
    
    top_frame = tkinter.LabelFrame(frame,text = "JSON Information")
    top_frame.grid(row=1,column=0, sticky="news", padx=20, pady=20)
    
    #top = tkinter.Toplevel(window)  
    #top_frame = tkinter.LabelFrame(top,text = "JSON Information")
    #top_frame.grid(row=0, column=0, pady=20, sticky="nw")

    
    pop_key_label = tkinter.Label(top_frame, text="KEY")
    pop_key_label.grid(row=0, column=0)

    pop_key_entry = tkinter.Entry(top_frame)
    pop_key_entry.grid(row=0,column=1)

    pop_data_label = tkinter.Label(top_frame, text="DATA")
    pop_data_label.grid(row=1, column=0)

    pop_data_entry = tkinter.Entry(top_frame)
    pop_data_entry.grid(row=1,column=1)


    def add_val2(super_key=key_in):
        print(i)
        xdata = pop_data_entry.get()
        xkey = pop_key_entry.get()
        if xdata:
                print("Key:",xkey,"Data", xdata)
                json_dict[key_in].append({xkey:xdata})
                #json_dict[key_in]={xkey:xdata}
                print(json_dict)
                print("magic")
        else:
            tkinter.messagebox.showwarning(title="Error", message="Data is missing.")
            
   
    def add_list2(super_key=key_in):
        xdata = pop_data_entry.get()
        xkey = pop_key_entry.get()
        print(xdata)
        #print(i+1)
        if xdata:
            li = list(xdata.split(","))
            print("Key:", xkey,"Data", li)
            json_dict[key_in].append({xkey:li})
            #json_dict[key_in]={xkey:li}
            print(json_dict)
        else:
            tkinter.messagebox.showwarning(title="Error", message="Data is missing.")
            

    def add_dict2(super_key=key_in):
        #print(i+2)
        xdata = pop_data_entry.get()
        xkey = pop_key_entry.get()
        if xdata and super_key!=None:
                print("Key:",xkey,"Data", xdata)
                dict_o = str_to_dict(xdata)
                json_dict[key_in].append({xkey:dict_o})
                print(json_dict)
                print("magic")
        else:
            tkinter.messagebox.showwarning(title="Error", message="Data is missing.") 

    pop_button1 = tkinter.Button(top_frame, text=" Add value ", command= add_val2)
    pop_button1.grid(row=2,column=1, sticky="news", padx=20, pady=20)

    pop_button2 = tkinter.Button(top_frame, text=" Add list", command= add_list2)
    pop_button2.grid(row=2,column=2, sticky="news", padx=20, pady=20)

    pop_button3 = tkinter.Button(top_frame, text=" Add Dict", command= add_dict2)
    pop_button3.grid(row=2,column=3, sticky="news", padx=20, pady=20)
   
    pop_button4 = tkinter.Button(top_frame, text=" CLOSE", command= top_frame.destroy)
    pop_button4.grid(row=3,column=0, sticky="news", padx=10, pady=10)
    # b3 = tk.Button(my_w_child, text=' Close Child',                   command=my_w_child.destroy)
    #b3.grid(row=3,column=2)

    

    #top.mainloop() 
    

window = tkinter.Tk()

window.title("JSON Entry Form")

def show():   
    result = jj.dumps(json_dict, indent = 3)
    print(result)
    my_text.delete('1.0',END) 
    my_text.insert('1.0',result)
    #temp = json.dumps(json_dict)
    #print(temp)

    

def add_list():
    data = data_entry.get()
    key = key_entry.get()

    print(i+1)
    if data :
        li = list(data.split(","))
        print("Key:", key,"Data", data)
        json_dict[key]=li
        print(json_dict)
    else:
        tkinter.messagebox.showwarning(title="Error", message="Data is missing.")
    pass

def str_to_dict(string):
    # remove the Spaces from the string
    string = string.replace(" ", "")
    # remove the curly braces from the string
    string = string.strip('{}')
 
    # split the string into key-value pairs
    pairs = string.split(',')
    dict1={}
    for pair in pairs:
        key, value = pair.split(':')
        dict1[key]=value
    return dict1

def add_dict():
    key = key_entry.get()
    data = data_entry.get()
    if data and key :
        dict_o = str_to_dict(data)
        json_dict[key]=dict_o
    else:
        tkinter.messagebox.showwarning(title="Error", message="Either Key or Data is missing.")
    
def add_val():
    print(i)
    data = data_entry.get()
    key = key_entry.get()
    if data :
        print("Key:", key,"Data", data)
        json_dict[key]=data
        #my_text.insert(END,json_dict)
        print(json_dict)
    else:
        tkinter.messagebox.showwarning(title="Error", message="Data is missing.")
        
    pass

def add_list_value():
    key = key_entry.get()
    json_dict[key]=[]
    print("List Button")
    if key:
        pop_up_list(key)

def add_dict_value():
    key = key_entry.get()
    json_dict[key]={}
    print("Dict Button")
    if key:
        pop_up_dict(key)
    else:
        tkinter.messagebox.showwarning(title="Error", message="Key is missing.")


frame = tkinter.Frame(window)
frame.pack() # geomatry manager

user_info_frame2 = tkinter.LabelFrame(frame,text = "JSON Information")
user_info_frame2.grid(row=0, column=1, pady=20,padx=20, sticky="e")

my_text = Text(user_info_frame2, width=40, height=20,)
my_text.pack(pady=20)
my_text.grid(row=0, column=1, pady=20, sticky="e")

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame,text = "JSON Information")
user_info_frame.grid(row=0, column=0, pady=50, sticky="news")

key_label = tkinter.Label(user_info_frame, text="KEY")
key_label.grid(row=0, column=0,pady=10)

key_entry = tkinter.Entry(user_info_frame)
key_entry.grid(row=0,column=1)

data_label = tkinter.Label(user_info_frame, text="DATA")
data_label.grid(row=1, column=0)

data_entry = tkinter.Entry(user_info_frame)
data_entry.grid(row=1,column=1)

button1 = tkinter.Button(user_info_frame, text=" Add value ", command= add_val)
button1.grid(row=2,column=1, sticky="news", padx=20, pady=20)

button2 = tkinter.Button(user_info_frame, text=" Add list", command= add_list)
button2.grid(row=2,column=2, sticky="news", padx=20, pady=20)

button3 = tkinter.Button(user_info_frame, text=" Add Dict", command= add_dict)
button3.grid(row=2,column=3, sticky="news", padx=20, pady=20)

button4 = tkinter.Button(user_info_frame, text=" list", command= add_list_value)
button4.grid(row=0,column=2, sticky="news", padx=20, pady=20)

button5 = tkinter.Button(user_info_frame, text=" Dict", command= add_dict_value)
button5.grid(row=0,column=3, sticky="news", padx=20, pady=20)



for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

# Button
button6 = tkinter.Button(frame, text=" Show ", command= show)
button6.grid(row=3,column=0, sticky="news", padx=10, pady=10)
button7 = tkinter.Button(frame, text=" CLOSE", command= window.destroy)
button7.grid(row=3,column=1, sticky="news", padx=10, pady=10)


window.mainloop()