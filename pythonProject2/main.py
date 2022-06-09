import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

langas = Tk()
langas.title("Medžiagų sąrašas")
langas.geometry("1080x720")
my_tree = ttk.Treeview(langas)
lenteles_pavadinimas = "Medžiagų sąrašas"

# Lentelės sukūrimas



def ivesti(kodas, pavadinimas, kaina, kiekis):
    conn = sqlite3.connect('medziagos.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS 
    medziagu_sarasas(itemkodas text, itempavadinimas text, itemkaina text, itemkiekis text)""")

    c.execute("INSERT INTO medziagu_sarasas VALUES ('" + str(kodas) + "','" + str(pavadinimas) + "','" + str(kaina) + "','" + str(kiekis) + "')")
    conn.commit()

    messagebox.showinfo("Informacija", "Duomenys įvesti sėkmingai")

    conn.commit()
    conn.close()

    # Įvedus duomenus, jie automatiškai išsivalo iš laukelio ir galima įvesti kitus duomenis

    kodas.delete(0, END)
    pavadinimas.delete(0, END)
    kaina.delete(0, END)
    kiekis.delete(0, END)

def sarasas():
    conn = sqlite3.connect('medziagos.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS 
    medziagu_sarasas(itemkodas text, itempavadinimas text, itemkaina text, itemkiekis text)""")

    c.execute("SELECT * FROM medziagu_sarasas")
    resultatas = c.fetchall()
    conn.commit()
    return resultatas


def istrinti(medziagos):
    conn = sqlite3.connect('medziagos.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS 
    medziagu_sarasas(itemkodas text, itempavadinimas text, itemkaina text, itemkiekis text)""")

    c.execute("DELETE FROM medziagu_sarasas WHERE itemkodas = '" + str(medziagos) + "'")
    messagebox.showinfo("Informacija", "Duomenys ištrinti sėkmingai")
    conn.commit()

def atnaujinti(itemkodas, itempavadinimas, itemkaina, itemkiekis):
    conn = sqlite3.connect('medziagos.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS 
    medziagu_sarasas(itemkodas text, itempavadinimas text, itemkaina text, itemkiekis text)""")

    c.execute("UPDATE medziagu_sarasas SET itemkodas = '" + str(kodas) + "', pavadinimas = '" + str(pavadinimas) + "', kaina = '" + str(kaina) + "', kiekis = '" + str(kiekis) + "' WHERE kodas='"+str(pavadinimas)+"'")
    messagebox.showinfo("Informacija", "Duomenys atnaujinti sėkmingai")

    conn.commit()


def ivesti_data():
    itemkodas = str(entrykodas.get())
    itempavadinimas = str(entrypavadinimas.get())
    itemkaina = str(entrykaina.get())
    itemkiekis = str(entrykiekis.get())
    if itemkodas == "" or itempavadinimas == " ":
        print("Error Inserting Id")
    if itempavadinimas == "" or itempavadinimas == " ":
        print("Error Inserting Name")
    if itemkaina == "" or itemkaina == " ":
        print("Error Inserting Price")
    if itemkiekis == "" or itemkiekis == " ":
        print("Error Inserting Quantity")
    else:
        ivesti(str(itemkodas), str(itempavadinimas), str(itemkaina), str(itemkiekis))

    for medziagos in my_tree.get_children():
        my_tree.delete(medziagos)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

def istrinti():
    pasirinkti = my_tree.selection()[0]
    istrinti_duomenis = str(my_tree.item(pasirinkti)['values'][0])
    istrinti(istrinti_duomenis)

    for medziagos in my_tree.get_children():
        my_tree.delete(medziagos)


    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

def atnaujinti():
    pasirinkti = my_tree.selection()[0]
    atnaujinti_duomenis = my_tree.item(pasirinkti)['values'][0]
    atnaujinti_data(entrykodas.get(), entrypavadinimas.get(), entrykaina.get(), entrykiekis.get(), atnaujinti_duomenis)

    for data in my_tree.get_children():
        my_tree.delete(medziagos)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

titleLabel = Label(langas, text=lenteles_pavadinimas, font=('Arial bold', 30), bd=2)
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

idLabel = Label(langas, text="kodas", font=('Arial bold', 15))
nameLabel = Label(langas, text="pavadinimas", font=('Arial bold', 15))
priceLabel = Label(langas, text="kaina", font=('Arial bold', 15))
quantityLabel = Label(langas, text="kiekis", font=('Arial bold', 15))
idLabel.grid(row=1, column=0, padx=10, pady=10)
nameLabel.grid(row=2, column=0, padx=10, pady=10)
priceLabel.grid(row=3, column=0, padx=10, pady=10)
quantityLabel.grid(row=4, column=0, padx=10, pady=10)

entrykodas = Entry(langas, width=25, bd=5, font=('Arial bold', 15))
entrypavadinimas = Entry(langas, width=25, bd=5, font=('Arial bold', 15))
entrykaina = Entry(langas, width=25, bd=5, font=('Arial bold', 15))
entrykiekis = Entry(langas, width=25, bd=5, font=('Arial bold', 15))
entrykodas.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entrypavadinimas.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entrykaina.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entrykiekis.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

buttonEnter = Button(
    langas, text="Įrašyti", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#0099ff", command=ivesti)
buttonEnter.grid(row=5, column=1, columnspan=1)

buttonUpdate = Button(
    langas, text="Atnaujinti", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#ffff00", command=atnaujinti)
buttonUpdate.grid(row=5, column=2, columnspan=1)

buttonDelete = Button(
    langas, text="Ištrinti", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#e62e00", command=istrinti)
buttonDelete.grid(row=5, column=3, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

my_tree['columns'] = ("Kodas", "Pavadinimas", "Kaina", "Kiekis")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Kodas", anchor=W, width=100)
my_tree.column("Pavadinimas", anchor=W, width=200)
my_tree.column("Kaina", anchor=W, width=150)
my_tree.column("Kiekis", anchor=W, width=150)
my_tree.heading("Kodas", text="Kodas", anchor=W)
my_tree.heading("Pavadinimas", text="Pavadinimas", anchor=W)
my_tree.heading("Kaina", text="Kaina", anchor=W)
my_tree.heading("Kiekis", text="Kiekis", anchor=W)

for medziagos in my_tree.get_children():
    my_tree.delete(medziagos)


my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

langas.mainloop()







