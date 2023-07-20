from tkinter import *
import tkinter.ttk as ttk


root = Tk()
root.wm_attributes("-topmost", 1)

class Window(Frame):
    
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        #clear button
        def clear():
            ROInput.delete(0, END)
            InvNumInput.delete(0, END)
            PartNumInput.delete(0, END)
            QuantityInput.delete(0, END)
            LocationInput.delete(0, END)
            Pers1.deselect()
            Pers2.deselect()
        
        #close menu option
        def close():
            root.quit()
        
        #Menu Bar
        menu = Menu(root)
        item = Menu(menu)
        item.add_command(label="Show Data")
        item.add_command(label="Exit", command=close)
        menu.add_cascade(label="File", menu=item)
        root.config(menu=menu)
        
        #Labels
        RO = Label(self, text="RO Number: ")
        RO.grid()
        
        InvNum = Label(self, text="Invoice Number: ")
        InvNum.grid()
        
        PartNum = Label(self, text="Part Number: ")
        PartNum.grid()
        
        Quantity = Label(self, text="Quantity: ")
        Quantity.grid()
        
        Location = Label(self, text="Location: ")
        Location.grid()
        
        #Input Boxes
        ROInput = Entry(self, width=10)
        ROInput.grid(column=1, row=0)
        
        InvNumInput = Entry(self, width=15)
        InvNumInput.grid(column=1, row=1)
        
        PartNumInput = Entry(self, width=15)
        PartNumInput.grid(column=1, row=2)
        
        QuantityInput = Entry(self, width=10)
        QuantityInput.grid(column=1, row=3)
        
        LocationInput = Entry(self, width=10)
        LocationInput.grid(column=1, row=4)
        
        #Buttons
        EnterBtn = Button(self, text="Enter")
        EnterBtn.grid(column=0, row=5)
        
        ClearBtn = Button(self, text="Clear", command=clear)
        ClearBtn.grid(column=1, row=5)
        
        #CheckBoxes
        Pers1 = Checkbutton(self, text="Keep Selection?")
        Pers1.grid(column=2, row=0)
        
        Pers2 = Checkbutton(self, text="Keep Selection?")
        Pers2.grid(column=2, row=1)
        
        



app = Window(root)
root.wm_title("Diehl Inventory System")
root.geometry("300x300")
root.mainloop()