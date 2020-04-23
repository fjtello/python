from ComicCrawler_Entities import comic
from ComicCrawler_Entities import Page

def load_comic_list():
    comic_list = [ 
comic("collection", "https://www.web.com/page1.html", "Title1"), \
comic("collection", "https://www.web.com/page2.html", "Title2"), \
]

    return comic_list


def texts_to_replace():
    txts = [ \
        "escanear", \
        "Escanear0", \
        "PaginaComic", \
        "%2B", "", \
        "Scan", ""
    ]

    return txts
 
 
def load_item_tag():
    return "post-body entry-content"


