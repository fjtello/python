import requests as rq
import io as os
import bs4 as bs
from pathlib import Path
import urllib.request as ul_rq
import shutil as sh
import patoolib as pt
from zipfile import ZipFile
import ComicCrawler_Entities as comic_entities


# Saves a web html content into a local html file
def save_url_content_into_html_file(url_source, path_destiny):
    web_content = rq.get(url_source)
    destiny_content = web_content.text[:].encode('utf-8').strip().decode('utf-8')

    # Only saves SECTION "post-body entry-content"
    destiny_content = get_section_main(destiny_content, "post-body entry-content")
    file_text = os.open(path_destiny, mode='w', encoding='UTF-8')

    file_text.write(destiny_content)
    file_text.close()
    return path_destiny


# Takes only the inner section of a local html file
def get_section_main(par_content, section):
    contents = bs.BeautifulSoup(par_content, features="html.parser")

    main_block = contents.find("div", {"class": section})
    main_block = "{}</div>".format(main_block)
    main_block = "<html><body>{}</body></html>".format(main_block)

    main_block = main_block.replace("<img","\r\n<img").\
        replace("<br>", "\r\n<br>").\
        replace("<a href", "\r\n<a href")

    return main_block


# Gets an image list
def get_list_images(path_source, path_dir_imgs):
    Path(path_dir_imgs).mkdir(parents=True, exist_ok=True)

    res = [""]

    contents = open(path_source).read()
    cont_soup = bs.BeautifulSoup(contents, features="html.parser")

    images = cont_soup.find_all("img")
    for image_elem in images:

        initial_position = str(image_elem).lower().index("src=")

        if str(image_elem).find(".jpeg") > 0:
            final_position = str(image_elem).lower().rindex(".jpeg") + 5
        else:
            final_position = str(image_elem).lower().rindex(".jpg") + 4

        res.append(str(image_elem)[initial_position+5:final_position:1])

    return res


# Downloads an image list with no path
def download_images(path, image_list, texts_to_replace):
    res = []

    for element in image_list:
        if str(element) != "":
            image_name = element.split('/')[-1]

            element2 = element.replace("%2B", "")
            resource = ul_rq.urlopen(element2)

            image_name2 = image_name
            for repl in texts_to_replace:
                image_name2 = image_name2.replace(repl, "")

            output = open(path + "" + image_name2, "wb")
            output.write(resource.read())
            output.close()

            res.append(image_name2)

    return res


def compress_dir_content(path, filename, image_list, destination_cbx):
    compressed_files = []
    for image in image_list:
        if image != "":
            compressed_files.append(path + image)
            print(image)

    # to rar (CBR)
    # create rar
    # rar_file_name = path + filename + ".rar"
    # pt.create_archive(rar_file_name, compressed_files)
    # sh.move(rar_file_name, destination_cbx + filename + ".cbr")

    # to zip (CBZ)
    zip_file_name = path + filename + ".zip"
    zip_file = ZipFile(zip_file_name, 'w')
    for image in image_list:
        zip_file.write(path + str(image))
    zip_file.close()

    # move and rename file created
    sh.move(zip_file_name, destination_cbx + filename + ".cbz")


def move_file(path_origin, path_desstination):
    sh.move(path_origin, path_desstination)


def get_books_from_page(htmlpath, page, tag):
    res = [comic_entities.comic("", "", "")]
    save_url_content_into_html_file2(page.URL, htmlpath + page.Title + ".html", tag)
    get_list_links(htmlpath + page.Title + ".html")


def create_csv_from_books(list_books, csv, page):
    return -1


def get_list_links(path_source):
    res = [""]

    contents = open(path_source).read()
    cont_soup = bs.BeautifulSoup(contents, features="html.parser")

    images = cont_soup.find_all("img")
    for image_elem in images:

        initial_position = str(image_elem).lower().index("src=")

        if str(image_elem).find(".jpeg") > 0:
            final_position = str(image_elem).lower().rindex(".jpeg") + 5
        else:
            final_position = str(image_elem).lower().rindex(".jpg") + 4

        page = comic_entities.Page(str(image_elem)[initial_position + 5:final_position:1], )

        res.append()

    return res