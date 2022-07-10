import comunFunction as cf


class UrlsFirts:
    def __init__(self, url_text = '',url_page = '',url_imagen='', text = '',title='',domain=''):
         self._domain = domain
         self._url_text = cf.ok_url(url_text, self._domain)
         self._url_page = url_page
         self._url_imagen = url_imagen
         self._texto = text
         self._title = title
      

    def get_url_text(self):
        return self._url_text
      
        
    def get_url_page(self):
        return self._url_page
      
        
    def get_title(self):
        return self._title
    
    def get_url_imagen(self):
        return self._url_imagen
    
    def get_texto(self):
        return self._texto
      

        
        

