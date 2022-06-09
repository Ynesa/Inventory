import sqlite3

conn = sqlite3.connect("darbuotojai(1).db")
c = conn.cursor()

with conn:
    c.execute("SELEICT * FROM DARBUOTOJAI")
    c.execute("SELECT GIMIMO_DATA FROM DARBUOTOJAI")
    c.execute("SELECT VARDAS, PAVARDĖ, PAREIGOS FROM DARBUOTOJAI")
    c.execute("SELECT DISTINCT SKYRIUS_PAVADINIMAS FROM DARBUOTOJAI")
    c.execute("SELECT * FROM DARBUOTOJAI WHERE SKYRIUS_PAVADINIMAS = 'Gamybos')
    c.execute("SELECT PAREIGOS FROM DARBUOTOJAI WHERE VARDAS = 'Giedrius')
    c.execute("SELECT * FROM DARBUOTOJAI WHERE GIMIMO_DATA = '1986-09-19')
    c.execute("SELECT VARDAS FROM DARBUOTOJAI WHERE PAVARDĖ = 'Sabutis')
    c.execute("SELECT VARDAS, PAVARDĖ FROM DARBUOTOJAI WHERE PAREIGOS = 'Programuotojas' AND SKYRIUS_PAVADINIMAS = 'Gamybos')
    c.execute("INSERT INTO DARBUOTOJAI VALUES ("'Romas', 'Kundrotas', "1994-03-04", 'Vadovas', 'Gamybos'"))
    c.execute("INSERT INTO DARBUOTOJAI VALUES('Pranas', 'Antanaitis', '2003-01-06', 'Programuotojas', 'Gamybos'); INSERT INTO DARBUOTOJAI VALUES('Linas', 'Antanaitis', '2004-11-10', 'Programuotojas', 'Gamybos')





