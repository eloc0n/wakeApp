import tkinter as tk
from tkinter import filedialog, Text, ttk
import os

root = tk.Tk()
apps= []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                         filetypes=(("executables", "*.exe" ), ("all files", "*.*")))
    apps.append(filename)
    
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()      
        comboExample.configure(values=apps)


def runApps():
    for app in apps:
        os.startfile(app)

def saveApps():
    f = open('save.txt', 'w') 
    for app in apps:
        f.write(app + ',')

def deleteApps():
    os.remove("save.txt")
    for widget in frame.winfo_children():
        widget.destroy()
    
    apps.clear()

def callbackFunc():
    for app in apps:
        if comboExample.get() == app:
            os.startfile(app)
            break    
          

        


canvas = tk.Canvas(root, height=300, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.4, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack(padx=5, pady=5, ipadx=25)

runApps = tk.Button(root, text="Run All", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack(padx=5, pady=5, ipadx=31)

deleteApps = tk.Button(root, text="Delete All", padx=10, pady=5, fg="white", bg="#263D42", command=deleteApps)
deleteApps.pack(padx=5, pady=5, ipadx=25)

saveApps = tk.Button(root, text="Save All", padx=10, pady=5, fg="white", bg="#263D42", command=saveApps)
saveApps.pack(padx=5, pady=5, ipadx=29)

labelTop = tk.Label(root, text = "Choose your favourite app to open")
labelTop.pack(side=tk.LEFT, padx=5, pady=5)

comboExample = ttk.Combobox(root, values=apps)
comboExample.pack(side=tk.LEFT, padx=5, pady=5)

comboExample.current(0)

myBtn = tk.Button(root, text="Run App", command=callbackFunc)
myBtn.pack(side=tk.LEFT, padx=5, pady=5, ipadx=50)




for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()



root.mainloop()

