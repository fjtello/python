import ComicCrawler_Data as comic_data
import ComicCrawler_Functions as comic_functions

str_path_destiny = "C:/Temp/"
str_path_destiny_cbr = "C:/Temp/cbr/"
str_path_destiny_html = "C:/temp/html/"

def start_process():
    comic_list = comic_data.load_comic_list()

    i = 1
    for element in comic_list:
        title = element.get_title(i)
        title_format = element.get_format_filename(i)

        path_destiny_files = str_path_destiny + "" + title_format + ".html"
        comic_functions.save_url_content_into_html_file(str(element.URL), path_destiny_files)

        path_destiny_images = str_path_destiny + title + "/"
        url_images_list = comic_functions.get_list_images(path_destiny_files, path_destiny_images)
        comic_functions.move_file(path_destiny_files, str_path_destiny_html + title_format + ".html")

        local_images_list = comic_functions.download_images(path_destiny_images, url_images_list, title_format)
        comic_functions.compress_dir_content(path_destiny_images, title_format, local_images_list, str_path_destiny_cbr)

        i = i + 1
        if i == 500:
            break


start_process()