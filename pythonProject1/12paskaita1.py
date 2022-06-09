from tkinter import *

langas = Tk()

def spausdinti():
    ivesta = laukas1.get()
    uzrasas2["text"] = (f"Labas, {ivesta}!")

def funkcija():
    kintamasis.set("Naujas tekstas")
    print(kintamasis.get())

def isvalyti():

def atkurti():

def uzdaryti():


uzrasas1 = Label(langas, text="Įveskite vardą")
laukas1 = Entry(langas)
varnele = Button(langas, text="Patvirtinti", command = spausdinti)
uzrasas2 = Label(langas, text="")
langas.bind("<Return>", lambda event: spausdinti())


uzrasas1.grid(row=0, column=0)
laukas1.grid(row=0, column=1)
varnele.grid(row=0, column=2)
uzrasas2.grid(row=1, columnspan=3)


meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="isvalyti")
submeniu.add_command(label="atkurti")
submeniu.add_command(label="iseiti")
langas.mainloop()



