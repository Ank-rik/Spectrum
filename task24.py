import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. CGPA

options = [
    ("CGPA",1),
    ("GRADE",2),
    ("NEW INPUT",3),
]

def ShowChoice():
    print(v.get())

tk.Label(root, 
         text="""Choose the options:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(options):
    tk.Radiobutton(root, 
                  text=options,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)