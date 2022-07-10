import string
import scrapy
from scrapy import Request
import comunFunction as cf
from scrapy.crawler import CrawlerProcess
from models.site import Site


DOMAIN = 'theporndude.com'
NAME_FILE = 'theporndude.json'
PATH = 'jsons'
FILE_NAME = 'theporndude'

class PruebaBaseSpider(scrapy.Spider):
    name = "Prueba"
    allowed_domains = ['theporndude.com']
    start_urls = ['https://theporndude.com/']
    
    
    def parse(self, response):
        xp = "//div[@id='main_container']//a/@href"
        for url in response.xpath(xp).extract():
            url_ok = cf.url_valid(url,DOMAIN)
            if url_ok.startswith(f"https://{DOMAIN}"): 
                return (Request(url_ok, callback=self.parse_links))
    
    
    def parse_links(self, response):
        for link_thumbnail in response.xpath("//div[@class='link-thumbnail']"):
            site = Site()
            site["titulo"]=response.xpath("//title/text()").extract()
            site["urlImagen"]=link_thumbnail.css('img::attr(src)').extract_first().strip()
            site["urlSite"]=link_thumbnail.xpath("//a[@class= 'link-analytics']/@href").extract_first()
            site["urlSite"]=response.xpath("//div[contains(@class, 'link-details-review')]/text()").extract_first()
            yield site
   
        xp = "//*[contains(@class, 'main-container')]//a/@href"
        for next_url in response.xpath(xp).extract():
            next_url = cf.url_valid(next_url,DOMAIN)
            if next_url.startswith(f"https://{DOMAIN}"):
                yield Request(response.urljoin(next_url), callback=self.parse_links)
        
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_URI':f'{PATH}\{FILE_NAME}',
    'FEED_FORMAT': 'jsonlines'
})


process.crawl(PruebaBaseSpider)
process.start()