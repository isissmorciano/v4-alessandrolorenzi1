# # Verifica su File e JSON 

# ## Consegna
# Consegna un singolo file Python rinominato come `cognome.py` (es. `rossi.py`).
# Testa il codice eseguendolo in terminale con `python cognome.py`.

# ---

# ## Esercizio: Gestione Biblioteca

# Stai costruendo un sistema per gestire una piccola biblioteca.
# I dati di partenza sono da definire hardcoded nel `main()`:

# ```python
# libri = [
#     {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
#     {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
#     {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
#     {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
# ]
# ```

# ---

# ### Punto A – Salvataggio e caricamento JSON 

# 1. Definisci `salva_biblioteca(libri: list[dict], nome_file: str) -> None`:
#    Salva la lista in formato JSON con indentazione. Stampa un messaggio di conferma.

# 2. Definisci `carica_biblioteca(nome_file: str) -> list[dict]`:
#    Carica e restituisce la lista da JSON.
#    Se il file non esiste, stampa un messaggio di errore e restituisce `[]`.

# Nel `main()`:
# - Chiama `salva_biblioteca` per salvare su `"biblioteca.json"`.
# - Chiama `carica_biblioteca` e stampa quanti libri sono stati caricati.

# **Esempio di output:**
# ```
# File 'biblioteca.json' salvato con successo.
# Libri in archivio: 4
# ```


# ---

# ### Punto B – Filtro per genere

# 1. Definisci `filtra_per_genere(libri: list[dict], genere: str) -> list[dict]`:
#    Restituisce una nuova lista con solo i libri il cui campo `"genere"` corrisponde a quello passato.

# Nel `main()`:
# - Usa i libri caricati nel Punto A.
# - Filtra per `"Fantascienza"` e stampa quanti ne hai trovati e i loro titoli.

# **Esempio di output:**
# ```
# Libri di Fantascienza: 2
# - 1984
# - Dune
# ```

# ---

# ### Punto C – Statistiche 

# 1. Definisci `calcola_media_anno(libri: list[dict]) -> float`:
#    Restituisce la media degli anni di pubblicazione come `float`.
#    Se la lista è vuota, restituisce `0.0`.

# 2. Definisci `trova_libro_piu_recente(libri: list[dict]) -> dict | None`:
#    Restituisce il dizionario del libro con l'anno più alto.
#    Se la lista è vuota, restituisce `None`.

# Nel `main()`:
# - Chiama entrambe le funzioni sui libri caricati e stampa i risultati.

# **Esempio di output:**
# ```
# Media anno di pubblicazione: 1963.5
# Libro più recente: Harry Potter (1997)
# ```

# ---

# ### Punto D – Conta libri per genere

# 1. Definisci `conta_per_genere(libri: list[dict]) -> dict[str, int]`:
#    Restituisce un dizionario dove le chiavi sono i generi e i valori sono il numero di libri per genere.

# Nel `main()`:
# - Chiama la funzione sui libri caricati.
# - Stampa il risultato ordinato per genere (alfabetico).

# **Esempio di output:**
# ```
# Libri per genere:
# Fantasy: 1
# Fantascienza: 2
# Romanzo: 1
# ```

# ---

# ### Punto E – Bonus: Modifica anno di un libro 

# Definisci `modifica_anno_libro(libri: list[dict], titolo: str, nuovo_anno: int) -> tuple[bool, str, list[dict]]`:
# - Trova il libro con quel titolo (ricerca esatta) e aggiorna l'anno.
# - Restituisce una tupla `(success, messaggio, libri_modificati)` dove `success` è `True` se il libro è stato trovato e modificato, altrimenti `False`. La lista modificata è sempre restituita.

# Nel `main()`, dopo il Punto D:
# - Chiedi all'utente un titolo e un nuovo anno.
# - Chiama `modifica_anno_libro` e stampa il messaggio.
# - Se la modifica è riuscita, richiama `salva_biblioteca` per salvare le modifiche su `"biblioteca.json"`.

# **Esempio di interazione:**
# ```
# Inserisci titolo da modificare: 1984
# Inserisci nuovo anno: 1950
# Libro '1984' aggiornato con anno 1950. Totale libri: 4
# ```

# **Se il libro non esiste:**
# ```
# Inserisci titolo da modificare: Titanic
# Libro 'Titanic' non trovato.
# ```





#  1. Definisci `salva_biblioteca(libri: list[dict], nome_file: str) -> None`:
# #    Salva la lista in formato JSON con indentazione. Stampa un messaggio di conferma.

# # 2. Definisci `carica_biblioteca(nome_file: str) -> list[dict]`:
# #    Carica e restituisce la lista da JSON.
# #    Se il file non esiste, stampa un messaggio di errore e restituisce `[]`.

import json

def salva_biblioteca(libri:list[dict], nome_file: str) -> None:
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            json.dump(libri,file,indent=4)
        print(f"File {nome_file} salvato con successo!")
    except IOError as e:
        print(f"Errore durante il salvataggio del file: {e}")


def  carica_biblioteca(nome_file: str) -> list[dict]:
    try:
        with open(nome_file,"r",encoding="utf-8") as file:
            libri = json.load(file)
        return libri
    except FileNotFoundError:
        print(f"Errore! Il file {nome_file} non è stato trovato. ")
        return[]
    except IOError as e:
        print(f"Errore nella caricatura del file: {e}")
        return []
    
# . Definisci `filtra_per_genere(libri: list[dict], genere: str) -> list[dict]`:
# #    Restituisce una nuova lista con solo i libri il cui campo `"genere"` corrisponde a quello passato.

# # Nel `main()`:
# # - Usa i libri caricati nel Punto A.
# # - Filtra per `"Fantascienza"` e stampa quanti ne hai trovati e i loro titoli.

def filtra_per_genere(libri: list[dict], genere: str) -> list[dict]:
    filtrati = []
    for libro in libri:
        if libro["genere"] == genere:
            filtrati.append(libro["titolo"])
    return filtrati

# 1. Definisci `calcola_media_anno(libri: list[dict]) -> float`:
# #    Restituisce la media degli anni di pubblicazione come `float`.
#    Se la lista è vuota, restituisce `0.0`.

# 2. Definisci `trova_libro_piu_recente(libri: list[dict]) -> dict | None`:
#    Restituisce il dizionario del libro con l'anno più alto.
#    Se la lista è vuota, restituisce `None`.

# Nel `main()`:
# - Chiama entrambe le funzioni sui libri caricati e stampa i risultati.


def calcola_media_anno(libri: list[dict]) -> float:
    somma = 0
    for libro in libri:
        somma = somma + libro["anno"]   
    media = somma / len(libri)
    return media        



def trova_libro_piu_recente(libri: list[dict]) -> dict | None:
    






def main():
    libri = [
     {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
     {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
     {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
     {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
]
    # salva_biblioteca(libri,"libri.json")
    # carica_biblioteca("libri.json")
    # genere = input("Inserisci un genere tra Fantascienza,Fantasy o Romanzo: ")
    # print(f"I film filtrati sono:{filtra_per_genere(libri,genere)} ")
    # print(f"La media degli anni è {calcola_media_anno(libri)}")
if __name__ == "__main__":
    main()    


        


