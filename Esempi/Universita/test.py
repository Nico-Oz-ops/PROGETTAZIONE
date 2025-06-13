from CorsoDiLaurea_senza_link import *
from Custom_Types import *
from Studente import *
from datetime import date

# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# creo un paio di oggetti studenti

stud1: Studente = Studente("Roberto", "Rossi")
stud2: Studente = Studente("Mario", "Maluco")
stud3: Studente = Studente("Maialo", "Marion")

# creo oggwto di tipo corso di laurea

tpl: TipoCorsoDiLaurea = TipoCorsoDiLaurea("Magistrale")

# creo oggetto del corso di laurea

cdl: CorsoDiLaurea = CorsoDiLaurea("AA-25", "Informatica", tpl)

# aggiungere studenti con le date d'iscrizione
oggi = date.today()
cdl.add_stud_iscritti(stud1, date(2025, 1, 18))
cdl.add_stud_iscritti(stud2, oggi)
cdl.add_stud_iscritti(stud3, date(2024, 5, 20))

# ottenere una lista degli iscritti

iscritti = cdl.getStudentiIscritti()

# stampa risultato per avere una verifica visiva

for studente, data_iscrizione in iscritti:
    print(f"{studente.nome()} il {data_iscrizione}")


# # Verifica con assert (semplice test manuale)
# assert (stud1, date(2023, 9, 15)) in iscritti
# assert (stud2, date(2023, 10, 2)) in iscritti
# print("\nTest completato con successo.")