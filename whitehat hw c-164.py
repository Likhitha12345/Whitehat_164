from tkinter import *

root = Tk()
root.title("planet encyclopedia")
root.geometry("500x500")
root.configure(background="Black")

def RotateImage():
    print("hi")

btn = Button(root, text="rotate Image" , command=RotateImage)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

root.mainloop()