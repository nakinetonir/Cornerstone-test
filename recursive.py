

import datetime
import os
from bs4 import BeautifulSoup
import requests
import logging
import comunFunction as cf

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

class Recursive():
    def __init__(self,start_url):
        self._start_url=start_url
        self._domain= cf.get_domain_from_uri(self._start_url)
        self._list_urls = []
        self._list_dict_url =  []

    def scrape_recursive(self,url):
        try:
            dict_url = {}
            headers = {'User-Agent': 'Mozilla/5.0'}
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, "html.parser") 
            dict_url["url"] = url
            """dict_url["texto"] = soup.get_text('\n').replace(
                        "\n", " ").replace(u'\xa0c', u' ').replace(u'\xa0', u' ')"""
            if soup.title:
                dict_url["title"] = soup.title.text   
            else:
                dict_url["title"] = ''
            self._list_dict_url.append(dict_url)
            for link in soup.find_all("a", href=True):
                
                url = link.get('href')
                    
    
                        
                if (url.startswith("/") or url.startswith(self._domain)) and (url not in  self._list_urls) and ( not url == "/"):
                    url_ok = cf.ok_url(url,self._domain)
                    if not url_ok.startswith("http://"): 
                        url_ok = f'http://{url_ok}'
                    self._list_urls.append(url_ok) 
                    self.scrape_recursive(url_ok)
                        
        except Exception as e:
            logging.error('Problem in {0} method, error is {1}'.format('scrape_recursive',e))       
                        
    def get_list_dict_url(self):
        return self._list_dict_url