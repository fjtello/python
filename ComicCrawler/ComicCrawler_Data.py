from ComicCrawler_Entities import comic

def load_comic_list():
    comic_list = [ 
comic("collection", "https://www.web.com/page1.html", "Title1"), \
comic("collection", "https://www.web.com/page2.html", "Title2"), \
]

    return comic_list


def texts_to_replace():
    txts = [ \
        "escanear", \
        "Sin%2Bt%25C3%25ADtulo-Escaneado-", \
        "Escanear0", \
        "20151102110937726_", \
        "PaginaComic", \
        "%2B", ""
    ]

    return txts