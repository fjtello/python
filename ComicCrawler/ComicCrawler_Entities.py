
class comic:

    Collection = ""
    URL = ""
    Title = ""

    def __init__(self, collection, url, title):
        self.Collection = collection
        self.URL = url
        self.Title = title

    def echo(self):
        print("echo comic Collection: ", self.Collection)
        print("echo comic URL: ", self.URL)
        print("echo comic Title: ", self.Title)

    def get_title(self, position):
        return ("000" + str(position))[-3:] + "_" +\
            self.Title.replace(":", "").\
            replace("  ", " ").\
            replace("  ", " ").\
            replace("-", "").\
            replace("  ", " ").\
            replace("!", "")

    def get_format_filename(self, position):
        return ("000" + str(position))[-3:] + "_" +\
            self.Title.replace(":", "").\
            replace("  ", " ").\
            replace("  ", " ").\
            replace("-", "").\
            replace("  ", " ").\
            replace("!", ""). \
            replace(" ", "_").\
            replace("-", "_").\
            replace("á", "a").\
            replace("é", "e").\
            replace("í", "i").\
            replace("ó", "o").\
            replace("ú", "u").\
            replace("Á", "A").\
            replace("É", "E").\
            replace("Í", "I").\
            replace("Ó", "O").\
            replace("Ú", "U").\
            replace("ñ", "n").\
            replace("Ñ", "N").\
            replace("%2B", "_")
