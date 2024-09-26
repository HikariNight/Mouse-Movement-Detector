from tkinter import *

running = False
x=0

def scanning():
    global x
    if running: 
        x = x+1
        print (x)
    # After 10 milli second, call scanning again (create a recursive loop)
    root.after(10, scanning)

def start():
    global running
    running = True

def stop():
    global running
    running = False

root = Tk()
root.title("Continuous Loop")
root.geometry("100x100")

app = Frame(root)
app.grid()

start = Button(app, text="Start counting", command=start)
stop = Button(app, text="Stop counting", command=stop)

start.grid()
stop.grid()

root.after(1000, scanning)  # After 1 second, call scanning
root.mainloop()