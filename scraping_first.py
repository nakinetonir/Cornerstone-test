

import datetime
import os
from bs4 import BeautifulSoup
import requests
import logging
from models.category import Category
import comunFunction as cf
from models.urls_first import UrlsFirts

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


class ScrapingFirts:

    def __init__(self,category:Category):
        self._category:Category=category
        self._domain='https://theporndude.com/' 
        self._list_firts = []
    
    def run_links_category_firts(self):
        try:
            driver = cf.connection_drive()
            driver.get(self._category.get_url_header())
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            thumbs = cf.find_element(driver,"xpath", "//*[@class='url_links_wrapper url_links_hover thumbs-list-content']") 
            url_link_container_list = cf.find_elements(thumbs,"class", "url_link_container")
            self.get_categoris(driver,url_link_container_list)
            driver.quit()
        except Exception as e:
            logging.error('Problem in {0} method, error is {1}'.format('run_links_category_firts',e))

            
            
    def get_categoris(self,driver,list_cards):
        try:
            for card in list_cards:
                card_soup = BeautifulSoup(
                        card.get_attribute(
                'outerHTML'), "html.parser")
                title_link = card_soup.find("div",attrs={"class": "url_link_title"})
                text_div = card_soup.find("div",attrs={"class": "url_short_desc"})
                text = text_div.get_text('\n').replace(
                        "\n", " ").replace(u'\xa0c', u' ').replace(u'\xa0', u' ')
                
                """image = cf.find_element(card,"class", "url_link_image") 
                cf.action_move_on(driver,image)
                image_soup = BeautifulSoup(
                        image.get_attribute(
                'outerHTML'), "html.parser")"""
                list_link = card_soup.find_all("a")
                img = card_soup.find("img")
                urls_firts = UrlsFirts(cf.ok_url(list_link[1].get("href"),self._domain),list_link[0].get("data-site-link"),img.get("src"),text,title_link.text,self._domain)
                self._list_firts.append(urls_firts)
        except Exception as e:
            logging.error('Problem in {0} method, error is {1}'.format('get_categoris',e))       
        
        
    def get_list_urls(self):
        return self._list_firts
