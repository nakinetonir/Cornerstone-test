

from links_category import ListCategory 
from scraping_first import ScrapingFirts 
from recursive import Recursive
import comunFunction as cf


if __name__ == '__main__':
    print("start")
    list_all_json = []
    list_dict_all_link = {}
    list_category = ListCategory()
    list_category.run_links_category()
    for category in list_category.get_list_categories():
        list_all_json = []
        scraping_first = ScrapingFirts(category)
        scraping_first.run_links_category_firts()
        for start_url in scraping_first.get_list_urls():
            dict_url = {}
            #recursive = Recursive(start_url.get_url_page())
            #recursive.scrape_recursive(start_url.get_url_page())
            dict_url["titulo"] = start_url.get_title()
            dict_url["url"] = start_url.get_url_page()
            dict_url["urlImagen"] = start_url.get_url_imagen()
            dict_url["texto"] = start_url.get_texto()
            #list_dict_all_lins["links"] = recursive.get_list_dict_url()   
            list_all_json.append(dict_url)
        list_dict_all_link['titulo'] = category.get_header()
        list_dict_all_link['listPages'] = list_all_json
        cf.write_json(list_dict_all_link,f"{category.get_header()}.json")
        
        
