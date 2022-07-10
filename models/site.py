from scrapy.item import Item, Field

class Site(Item):
    titulo = Field()
    urlImagen = Field()
    urlSite = Field()
    texto = Field()