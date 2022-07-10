

import datetime
import os
from bs4 import BeautifulSoup
import requests
import logging
import comunFunction as cf
from models.root_url import RootUrl
from os.path import exists


PATH_JSON = 'jsons'
NAME_FILE_JSON = 'theporndude.json'

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

class Recursive():
    def __init__(self,domain):
        self._domain=domain
        self._list_urls = []
        self._list_dict_url =  {}

    def scrape_recursive(self,url):
        try:

            
            headers = {'User-Agent': 'Mozilla/5.0'}
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, "html.parser") 
            link_thumbnail = soup.find_all("div",attrs={"class": "link-thumbnail"})
            
            if link_thumbnail and url not in self._list_dict_url.keys():
                self.save_url(link_thumbnail,soup,url)
            for link in soup.find_all("a", href=True):
                
                url = link.get('href')
                    
    
                        
                if (url.startswith("/") or url.startswith(self._domain)) and (url not in  self._list_urls) and (url != "/"):
                    url_ok = self.url_valid(url)
                    self._list_urls.append(url)
                    self.scrape_recursive(url_ok)
                        
        except Exception as e:
            logging.error('Problem in {0} method, error is {1}'.format('scrape_recursive',e))       
                        

    
    
    
    def create_update_json(self,dict_json):
        path_file = f'{PATH_JSON}\{NAME_FILE_JSON}'
        if exists(path_file):
            list_json = cf.read_json(NAME_FILE_JSON)
            list_json.append(dict_json)
            cf.write_json(list_json,NAME_FILE_JSON)
            
        else:
            list_json = [dict_json]
            cf.write_json(list_json,NAME_FILE_JSON)
            
            
    def url_valid(self,url):
        url_ok = cf.ok_url(url,self._domain)
        if not url_ok.startswith("https://"): 
            url_ok = f'https://{url_ok}'
        elif url_ok.startswith("//"): 
            url_ok = f'https:{url_ok}'
        return url_ok
    
    def save_url(self,link_thumbnail,soup,url):
            dict_url = {}
            link_thumb =  soup.find("div",attrs={"class": "link-thumb"})
            img = link_thumb.find("img")
            link = link_thumb.find("a")
            dict_url["url"] = url
            dict_url["urlPage"] = link.get("href")
            dict_url["urlImagen"] = img.get("src")
            link_details_review = soup.find("div",attrs={"class": "link-details-review"})
            dict_url["texto"] = link_details_review.get_text(
                        '\n').replace(u'\xa0c', u' ').replace(u'\xa0', u' ')
            if soup.title:
                dict_url["title"] = soup.title.text   
            else:
                dict_url["title"] = ''
            self._list_dict_url[url] = True
            self.create_update_json(dict_url)