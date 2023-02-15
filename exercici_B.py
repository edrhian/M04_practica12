import json
def libros():
    book1 = {"book" : [{"titel":"El corazon de la piedra", "cover":"Dura","year":"2013","pages":"560"}]}
    book2 = {"book": [{"titel": "Salmos de visperas", "cover": "Dura", "year": "2003", "pages": "135"}]}
    book3 = {"book": [{"titel": "La polifonia clasica", "cover": "Dura", "year": "1956", "pages": "216"}]}
    book4 = {"book": [{"titel": "Juana I,  reina sonambula", "cover": "Dura", "year": "2023", "pages": "144"}]}

    print(json.dumps(book1, indent=2))
    print(json.dumps(book2, indent=2))
    print(json.dumps(book3, indent=2))
    print(json.dumps(book4, indent=2))
libros()