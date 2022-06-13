import tkinter
from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
import pandas as pd

langas = Tk()
langas.title("Medžiagų sąrašas")
langas.geometry("1080x720")
my_tree = ttk.Treeview(langas)
# Duomenų bazės sukūrimas

conn = sqlite3.connect('medziagos.db')
c = conn.cursor()

# Lentelės sukūrimas
c.execute("""CREATE TABLE IF NOT EXISTS medziagu_sarasas (
        kodas text,
        pavadinimas text,
        kaina text,
        kiekis text
        )""")


# Funkcija atnaujinti duomenims:
def refresh():
    # Clean the data before displaying the new one.
    for data in my_tree.get_children():
        my_tree.delete(data)

    # Get elements from table and display
    data_from_table = sarasas()
    for data in data_from_table:
        my_tree.insert(parent='', index='end', iid=data, text="", values=(data), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)


# Sukuriama funkcija duomenų įvedimui į duomenų bazę
def ivesti():
    conn = sqlite3.connect('medziagos.db')
    c = conn.cursor()
    c.execute("INSERT INTO medziagu_sarasas VALUES(:kodas, :pavadinimas, :kaina, :kiekis)",
              {
                  'kodas': kodas.get(),
                  'pavadinimas': pavadinimas.get(),
                  'kaina': kaina.get(),
                  'kiekis': kiekis.get(),
              })
    messagebox.showinfo("Informacija", "Duomenys įvesti sėkmingai")

    conn.commit()
    conn.close()

    # Įvedus duomenus, jie automatiškai išsivalo iš laukelio ir galima įvesti kitus duomenis
    kodas.delete(0, END)
    pavadinimas.delete(0, END)
    kaina.delete(0, END)
    kiekis.delete(0, END)
    # Refresh the table to display the newly inserted row.
    refresh()


def sarasas():
    conn = sqlite3.connect('medziagos.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM medziagu_sarasas")
    irasai = c.fetchall()

    conn.commit()
    conn.close()
    return irasai


def istrinti():
    conn = sqlite3.connect('medziagos.db')
    c = conn.cursor()

    c.execute("DELETE from medziagu_sarasas WHERE kodas = '" + istrinimas.get() + "'")
    istrinimas.delete(0, END)
    messagebox.showinfo("Informacija", "Duomenys ištrinti sėkmingai")

    conn.commit()
    conn.close()
    # Refresh the table to display the recently deleted row.
    refresh()


def atnaujinti():
    conn = sqlite3.connect('medziagos.db')
    c = conn.cursor()

    c.execute("""UPDATE medziagu_sarasas SET
        kodas = :kodas,
        pavadinimas = :pavadinimas,
        kaina = :kaina,
        kiekis = :kiekis
        WHERE kodas = :oid""",
              {'kodas': kodas_redagavimas.get(),
               'pavadinimas': pavadinimas_redagavimas.get(),
               'kaina': kaina_redagavimas.get(),
               'kiekis': kiekis_redagavimas.get(),
               'oid': istrinimas.get()
               })

    messagebox.showinfo("Informacija", "Duomenys atnaujinti sėkmingai")

    conn.commit()
    conn.close()
    redagavimas.destroy()
    # Refresh the table to display the updated row.
    refresh()

def eksportuoti():
    conn = sqlite3.connect('medziagos.db')
    df = pd.read_sql_query("SELECT * FROM medziagu_sarasas", conn)
    df.to_csv('duomenys.csv', encoding="UTF-8", index=False)
    messagebox.showinfo("Informacija", "Duomenys eksportuoti sėkmingai")


def redaguoti():
    global redagavimas
    redagavimas = Tk()
    redagavimas.title('Atnaujinti duomenis')
    redagavimas.geometry("400x400")
    conn = sqlite3.connect('medziagos.db')
    c = conn.cursor()

    c.execute("SELECT * FROM medziagu_sarasas WHERE oid = '" + istrinimas.get() + "'")
    irasai = c.fetchall()

    global kodas_redagavimas
    global pavadinimas_redagavimas
    global kaina_redagavimas
    global kiekis_redagavimas

    kodas_redagavimas = Entry(redagavimas, width=30)
    kodas_redagavimas.grid(row=0, column=1, padx=20, pady=(10, 0))
    pavadinimas_redagavimas = Entry(redagavimas, width=30)
    pavadinimas_redagavimas.grid(row=1, column=1)
    kaina_redagavimas = Entry(redagavimas, width=30)
    kaina_redagavimas.grid(row=2, column=1)
    kiekis_redagavimas = Entry(redagavimas, width=30)
    kiekis_redagavimas.grid(row=3, column=1)

    kodas_label = Label(redagavimas, text="Kodas")
    kodas_label.grid(row=0, column=0, pady=(10, 0))
    pavadinimas_label = Label(redagavimas, text="Pavadinimas")
    pavadinimas_label.grid(row=1, column=0)
    kaina_label = Label(redagavimas, text="Kaina")
    kaina_label.grid(row=2, column=0)
    kiekis_label = Label(redagavimas, text="Kiekis")
    kiekis_label.grid(row=3, column=0)

    for irasas in irasai:
        kodas_redagavimas.insert(0, irasas[0])
        pavadinimas_redagavimas.insert(0, irasas[1])
        kaina_redagavimas.insert(0, irasas[2])
        kiekis_redagavimas.insert(0, irasas[3])

    atnaujinimo_mygtukas = Button(redagavimas, text="Išsaugoti įrašą", command=atnaujinti)
    atnaujinimo_mygtukas.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# Text boxes
kodas = Entry(langas, width=30)
kodas.grid(row=0, column=1, padx=20, pady=(10, 0))
pavadinimas = Entry(langas, width=30)
pavadinimas.grid(row=1, column=1)
kaina = Entry(langas, width=30)
kaina.grid(row=2, column=1)
kiekis = Entry(langas, width=30)
kiekis.grid(row=3, column=1)
istrinimas = Entry(langas, width=30)
istrinimas.grid(row=5, column=1)

kodas_label = Label(langas, text="Kodas", font=('Arial', 15))
kodas_label.grid(row=0, column=0, pady=(10, 0))
pavadinimas_label = Label(langas, text="Pavadinimas", font=('Arial', 15))
pavadinimas_label.grid(row=1, column=0)
kaina_label = Label(langas, text="Kaina", font=('Arial', 15))
kaina_label.grid(row=2, column=0)
kiekis_label = Label(langas, text="Kiekis", font=('Arial', 15))
kiekis_label.grid(row=3, column=0)
istrinimas_label = Label(langas, text="Pasirinkti Kodą", font=('Arial', 15))
istrinimas_label.grid(row=5, column=0, pady=5)

# Sukuriami mygtukai

mygtukas_ivesti = tkinter.Button(
    langas, text="Įvesti", padx=10, pady=1, width=5,
    bd=3, font=('Arial', 15), bg="#63B8FF", command=ivesti)
mygtukas_ivesti.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

mygtukas_atnaujinti = tkinter.Button(
    langas, text="Atnaujinti", padx=10, pady=1, width=5,
    bd=3, font=('Arial', 15), bg="#FFFF00", command=redaguoti)
mygtukas_atnaujinti.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

mygtukas_istrinti = tkinter.Button(
    langas, text="Ištrinti", padx=10, pady=1, width=5,
    bd=3, font=('Arial', 15), bg="#00FF00", command=istrinti)
mygtukas_istrinti.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

mygtukas_eksportuoti = tkinter.Button(
    langas, text="Eksportuoti į CSV", padx=10, pady=1, width=5,
    bd=3, font=('Arial', 15), bg="#e62e00", command=eksportuoti)
mygtukas_eksportuoti.grid(row=18, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#duomenu_ivedimo_mygtukas = Button(langas, text="Įvesti", command=ivesti, bg="blue", fg="red")
#duomenu_ivedimo_mygtukas.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#saraso_mytgukas = Button(langas, text="Rodyti sąrasą", command=sarasas)
#saraso_mytgukas.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#istrinimo_mygtukas = Button(langas, text="Ištrinti įrasą", command=istrinti)
#istrinimo_mygtukas.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#redagavimo_mygtukas = Button(langas, text="Redaguoti įrašą", command=redaguoti)
#redagavimo_mygtukas.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Treeview stulpelių pavadinimai ir stilius:
style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 20))

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

# Ištrinti viską iš treeview.
for data in my_tree.get_children():
    my_tree.delete(data)

# Read all the data from the database at the start of the
# program and dispaly in the treeview.
data_from_table = sarasas()
for data in data_from_table:
    my_tree.insert(parent='', index='end', iid=data, text="", values=(data), tag="orow")

# This puts treeview inside grid to be displayed.
my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
# How many pixels to pad widget, horizontally and vertically, outside v's borders. Padx and pady are for positioning, x is left/right, y is up/down.
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=50)

conn.commit()
conn.close()

langas.mainloop()
