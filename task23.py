import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. math

subjects = [
    ("Math",1),
    ("Physics",2),
    ("Submit",3),
]

def ShowChoice():
    print(v.get())

tk.Label(root, 
         text="""Choose the subject:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(subjects):
    tk.Radiobutton(root, 
                  text=subjects,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)