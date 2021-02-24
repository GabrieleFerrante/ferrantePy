from json import *
from os.path import join

libri = [
    {"titolo": "Era meglio il libro",
     "autore": "Valerio Lundini",
     "editore": "Rizzoli Lizard"},
    {"titolo": "La carezza della memoria",
     "autore": "Carlo Verdone",
     "editore": "Bompiani"},
    {"titolo": "Il duca e io",
     "autore": "Quinn Jiulia", 
     "editore": "Mondadori"},
    {"titolo": "Insieme in cucina",
     "autore": "Benedetta Rossi",
      "editore": "Mondadori Electa"},
    {"titolo": "Eresia",
     "autore": "Citro Della Riva Massimo",
      "editore": "Byoblu"},
    {"titolo": "Finché il caffe è caldo",
     "autore": "Toshikazu Kawaguchi",
      "editore": "Garzanti Libri"},
    {"titolo": "365 giorni senza di te",
     "autore": ["Anna Bells Campani", "Raffaella di Girolamo"],
      "editore": "Spierling & Kupfer"},
    {"titolo": "La città di vapore",
     "autore": "Carlos Ruiz Zafon",
      "editore": "Mondadori"},
    {"titolo": "La legge dell'innocenza",
     "autore": "Michael Connelly",
      "editore": "Piemme"},
    {"titolo": "Il visconte che mi amava",
     "autore": "Quinn Jiulia",
      "editore": "Mondadori"}
] #La lista dei libri è stata recuperata al sito: https://www.mondadoristore.it/Classifica-libri-Best-Seller/gr-308/

nome_file = "data.json"

with open(join("./ferrantePy/accessoFile",nome_file), "w") as f:
    dump(libri, f, separators=[",", ":"], indent=2)