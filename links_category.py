import datetime
import os
from bs4 import BeautifulSoup
import requests
import logging
import sys
from models.category import Category
from models.root_url import RootUrl 
import comunFunction as cf


logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


class ListCategory:

    def __init__(self):
        self._url='https://theporndude.com/'
        self._domain='https://theporndude.com/' 
        self._root_url = RootUrl(self._url,self._domain)
        self._list_categories = []
    
    def run_links_category(self):
        try:
            driver = cf.connection_drive()
            driver.get(self._root_url.get_url())
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            soup = BeautifulSoup(
                        driver.page_source, "html.parser")
            driver.quit()
            main_container = soup.find("div", attrs={"id": "main_container"})
            
            list_headers = main_container.find_all("div",attrs={"class": "category-header"})
            self.get_categoris(list_headers)
            
        except Exception as e:
            logging.error('Problem in {0} method, error is {1}'.format('run_links_category',e)) 



    def get_categoris(self,list_headers):
        try:
            for category_header in list_headers:
                    link_header = category_header.find("a")
                    txt_header = link_header.text
                    url = self._root_url.url_domain(link_header.get("href"))
                    category = Category(txt_header,url)
                    print(url)
                    self._list_categories.append(category)
        except Exception as e:
            logging.error('Problem in {0} method, error is {1}'.format('get_categoris',e))     

    def get_list_categories(self):
        return self._list_categories



