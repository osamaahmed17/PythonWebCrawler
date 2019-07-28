from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def error (self,message,page_url):
        pass

    def page_links(self):
        return self.links

    def __init__(self):
        super().__init__()
        self.base_url=base_url
        self.page_url=page_url
        self.link=set()

    def handle_starting(self,tag,attrs):
        if tag=='a':
            for(attribute,value) in attrs:
                if attribute =='href':
                    url=parse.urljoin(self.base_url,value)
                    self.links.add(url)

    

finder=LinkFinder()
finder.feed()
