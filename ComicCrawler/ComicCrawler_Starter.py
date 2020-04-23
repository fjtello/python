import ComicCrawler_Data as comic_data
import ComicCrawler_Functions as comic_functions

str_path_destiny = "C:/Comic/Extract/"
str_path_destiny_cbr = "C:/Comic/cbr/"
str_path_destiny_html = "C:/Comic/html/"

str_tag_pages = "post-title entry-title"
str_csv_books = "C:/Comics/books_csv"


def start_process_elements():
    comic_list = comic_data.load_comic_list()
    text_excepts = comic_data.texts_to_replace()
    tag_to_extract = comic_data.load_item_tag()

    i = 1
    for element in comic_list:
        if element.Collection != "":
            title = element.get_title(i)
            title_formatted = element.get_format_filename()

            print("WORKING ON ==>   ", i, "     ", title)

            path_destiny_files = str_path_destiny + "" + title_formatted + ".html"
            comic_functions.save_url_content_into_html_file(str(element.URL), path_destiny_files, tag_to_extract)

            path_destiny_images = str_path_destiny + title + "/"
            url_images_list = comic_functions.get_list_images(path_destiny_files, path_destiny_images)
            comic_functions.move_file(path_destiny_files, str_path_destiny_html + title_formatted + ".html")

            local_images_list = comic_functions.download_images(path_destiny_images, url_images_list, text_excepts)
            comic_functions.compress_dir_content(path_destiny_images, title_formatted, local_images_list,
                                                 str_path_destiny_cbr)
            comic_functions.remove_aux(path_destiny_images, str_path_destiny_html + title_formatted + ".html")
        i += 1