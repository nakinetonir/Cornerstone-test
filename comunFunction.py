
from selenium import webdriver
from urllib.parse import urlparse
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from bson.json_util import dumps
import json
from os.path import exists

PATH_WRITE = 'jsons'

def ok_url(url_link, base_url):
    domain = urlparse(url_link).netloc
    if domain != '' and domain is not None:
        return url_link
    else:
        return base_url + url_link


def connection_drive():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver



def action_move_on(driver,elem_hover):
    actions = ActionChains(driver)
    actions.move_to_element(elem_hover)
    actions.perform()
    return driver
    
def action_click(driver,elem_click):
    actions = ActionChains(driver)
    actions.click(elem_click)
    actions.perform()
    return driver


def find_element(driver,type:str, text_find:str):
    return driver.find_element(return_by_type(type), text_find)

def find_elements(driver,type:str, text_find:str):
    return driver.find_elements(return_by_type(type), text_find)

def return_by_type(type:str):
    
    if type=="class":
        return By.CLASS_NAME
    
    if type=="id":
        return By.ID
    
    if type=="css":
        return By.CSS_SELECTOR
    
    if type=="xpath":
        return By.XPATH
    
  
def get_domain_from_uri(url_link):
    return urlparse(url_link).netloc

def check_domain_from_uri(url_link,domain):
    return urlparse(url_link).netloc==domain


def write_json(json,name_file):
    json_data = dumps(json)

    with open(f"{PATH_WRITE}\{name_file}", "w") as outfile:
        outfile.write(json_data)
        
        
def read_json(name_file):
    f = open(f"{PATH_WRITE}\{name_file}")
    
    data = json.load(f)
    
    return data

def url_valid(url,domain):

    url_ok = ok_url(url,domain)
    if not url_ok.startswith("https://"): 
        url_ok = f'https://{url_ok}'
    elif url_ok.startswith("//"): 
        url_ok = f'https:{url_ok}'
    return url_ok

def create_update_json(dict_json,name_file):
    path_file = f'{PATH_WRITE}\{name_file}'
    if exists(path_file):
        list_json = read_json(name_file)
        list_json.append(dict_json)
        write_json(list_json,name_file)
        
    else:
        list_json = [dict_json]
        write_json(list_json,name_file)