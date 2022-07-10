
import comunFunction as cf

class RootUrl:
    def __init__(self, url = '',domain = ''):
         self._url = url
         self._domain = domain
      

    def get_domain(self):
        return self._domain
      

    def set_domain(self, x):
        self._domain = x
        
    def get_url(self):
        return self._domain
      

    def set_url(self, x):
        self._domain = x
        
        
    def url_domain(self,url_primary):
        return cf.ok_url(url_primary, self._domain)
