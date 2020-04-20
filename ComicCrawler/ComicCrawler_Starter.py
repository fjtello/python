import ComicCrawler_Data as comic_data
import ComicCrawler_Functions as comic_functions

str_tag_elements = "tag unique"
str_path_destiny = "C:/Comic/"
str_path_destiny_cbx = "C:/Comic/cbx/"
str_path_destiny_html = "C:/Comic/html/"


def start_process_elements():
    comic_list = comic_data.load_comic_list()
    text_excepts = comic_data.texts_to_replace()

    i = 1
    for element in comic_list:
        if element.Collection != "":
            title = element.get_title(i)
            title_formatted = element.get_format_filename()
            path_destiny_files = str_path_destiny + "" + title_formatted + ".html"
            path_destiny_images = str_path_destiny + title + "/"
            
            print("PROCESSING...   [", i, "]   ==>   ", title)

            # get inner block pf images
            comic_functions.save_url_content_into_html_file(str(element.URL), path_destiny_files)

            # get list of the images to download
            url_images_list = comic_functions.get_list_images(path_destiny_files, path_destiny_images)
            
            comic_functions.move_file(path_destiny_files, str_path_destiny_html + title_formatted + ".html")

            # download the images
            local_images_list = comic_functions.download_images(path_destiny_images, url_images_list, text_excepts)
            
            # compress the set of images for a comic book and 
            comic_functions.compress_dir_content(path_destiny_images, title_formatted, local_images_list,
                                                 str_path_destiny_cbx)
    
    
start_process_elements()
