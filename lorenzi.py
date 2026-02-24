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
    

def filtra_per_genere(libri: list[dict], genere: str) -> list[dict]:
    filtrati = []
    for libro in libri:
        if libro["genere"] == genere:
            filtrati.append(libro["titolo"])
    return filtrati


def calcola_media_anno(libri: list[dict]) -> float:
    somma = 0
    for libro in libri:
        somma = somma + libro["anno"]   
    media = somma / len(libri)
    return media        


def trova_libro_piu_recente(libri: list[dict]) -> dict | None:
    massimo = 0
    for libro in libri:
        if libro["anno"] > massimo:
            massimo = libro["anno"]
            libro_recente = libro
    return libro_recente
        

def conta_per_genere(libri: list[dict]) -> dict[str, int]:
    rom = 0
    fantascienza = 0
    fantasy = 0
    for libro in libri:
        genere = libro["genere"]
        if genere == "Romanzo":
            rom = rom + 1
        elif genere == "Fantascienza":
            fantascienza = fantascienza + 1
        elif genere == "Fantasy":
            fantasy == fantasy + 1
    contatore_generi={"Romanzo" : rom,
                      "Fantascienza" : fantascienza,
                      "Fantasy" : fantasy}
    return contatore_generi
    

def modifica_anno_libro(libri: list[dict], titolo: str, nuovo_anno: int) -> None:
    for libro in libri:
        if libro["titolo"] == titolo:
            libro["anno"] == nuovo_anno
    print("\nAnno cambiato con successo!")
    print(f"\n{libri}")


def main():
    libri = [
     {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
     {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
     {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
     {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
]
    salva_biblioteca(libri,"libri.json")
    carica_biblioteca("libri.json")
    genere = input("\nInserisci un genere tra Fantascienza,Fantasy o Romanzo: ")
    print(f"\nI film filtrati sono:{filtra_per_genere(libri,genere)} ")
    print(f"\nLa media degli anni è {calcola_media_anno(libri)}")
    print(f"\nIl libro più recente è {trova_libro_piu_recente(libri)}")
    print(f"\nContatore per generi: {conta_per_genere(libri)}")
    titolo = input("\nInserisci il titolo del libro a cui vuoi modificare l'anno: ")
    nuovo_anno = input("\nInserisci il nuovo anno da cambiare: ")
    modifica_anno_libro (libri,titolo,nuovo_anno)
if __name__ == "__main__":
    main()    



        


