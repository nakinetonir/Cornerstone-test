
class Category:
    def __init__(self, header,url_header):
        self._header = header
        self.url_header = url_header

    def get_header(self):
        return self._header
      

    def set_header(self, x):
        self._header = x
        
        
    def get_url_header(self):
        return self.url_header


    def set_url_header(self, x):
        self.url_header = x
