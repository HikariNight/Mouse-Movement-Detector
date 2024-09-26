import customtkinter
import os
from PIL import ImageTk
import win32api
import keyboard

#GUI Theme
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

#Shortening the CTK command and defining the resolution and name of the application
root = customtkinter.CTk()
root.geometry("316 x 252")
root.resizable(False, False)
root.title("MMD") #Mouse Movement Detector

#Directing to the Icon 
icon = ImageTk.PhotoImage(file=os.path.join("assets", "SEYANAAAAA.JPG"))
root.iconbitmap()
root.iconphoto(False, icon)

#Variables concerning the mouse
status = False
count = 0

#--------------The Code--------------#

#Recursive function to incrament by 1 for each millisecond the cursor changes position
#Can be stopped with F8
def Detection():
    global count
    savedpos = win32api.GetCursorPos()
    if (status):
        curpos = win32api.GetCursorPos()
        if savedpos != curpos:
            count = count +1
            print("Mouse Movement # ", count)
        if keyboard.is_pressed('F8'):
            stopDetection()
    root.after(1, Detection)

#Flips the switch to ON
def startDetection():
    global status
    global count
    status = True
    count = 0

#Flips the switch to OFF and changes the colour of Status to indicate movement
def stopDetection():
    global status
    global count
    status = False
    Moved(count)
    
#Outputs the corresponding actions based on whether it was detected the mouse moved or not
def Moved(count):
    if count == 0:
        label.configure(text_color="#00FF00")
        label2.configure(text="DoMM (in ms): " + str(count))
    else:
        label.configure(text_color="#FF0000")
        label2.configure(text="DoMM (in ms): " + str(count))

#Made this because the function to bind a key takes an arguement and i don't want to ruin the base startDetection code with it
def standIn(event):
    startDetection()
    

#--------------THE GUI--------------#

#The Base/Background
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=30, fill="both", expand=True)

#Current status, can be Grey (for Neutral), Green (for no movement) or Red (for movement)
label = customtkinter.CTkLabel(master=frame, text="Status", font=("Roboto", 24))
label.pack(pady=12, padx=10)

#Shows the User the number of milliseconds the mouse was moved between the detection interval
label2 = customtkinter.CTkLabel(master=frame, text="DoMM (in ms): " + str(count), font=("Roboto", 12))
label2.pack(pady=3, padx=5)

#Button to start the detecting
button = customtkinter.CTkButton(master=frame, text="Start (F7)", command=startDetection)
button.pack(pady=20, padx=60)

#Button to stop the detecting
button = customtkinter.CTkButton(master=frame, text="Stop (F8)", command=stopDetection)
button.pack(pady=20, padx=60)

#Pressing F7 starts detection, which is running but not going through the loop because status is false
root.bind('<F7>', standIn)
root.after(1, Detection)
root.mainloop()

#Would be cool if i could make it start and stop with the same bind, which works with buttons but not with keyboard inputs, so for no i'll make the binds different