# Cornerstone-test

## Test scraping

## [Para la url theporndude](https://theporndude.com/)

## He relaizado dos scraping.

### **libreria scrapyt**


###### Si queremos ejecutar el script hay que lanzar:



```Python
    scrapy_recursive.py
```

Se generan un json con la siguiente extructura:

```Python
    class Site(Item):
        titulo = Field()
        urlImagen = Field()
        urlSite = Field()
        urlSite = Field()
```


### **selenium, beautifulsoup**


###### Para ejecutar el código se hace con el siguiente archivo:

```Python
    main.py
```

Creamos un listado de json que contienen

* Un campo titulo que contiene el cada categoria indetificada en la página
* Un campo listPages que contiene info de cada website perteneciente a la categoria (titulo, url, urlImagen, texto)


=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci