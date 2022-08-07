import requests
from guardicore_crawler_v2.helpers.thread import ThreadWrapper


from bs4 import BeautifulSoup ;""" This is a library that allows us to \
                                      parse html """
                                    

class URLParser(object):
    
    def __init__(self, url, user_agent):
        self.url = url
        self.user_agent = user_agent
        self.r = None
        self.got = False

    def get_request(self):
        if self.got == True:
            return self.r
        try:
            self.r = requests.get(self.url, headers={'User-Agent': self.user_agent})
            self.got = True
            return self.r
        except:
            return None

    def is_broken(self):

        if self.url is None or self.get_request() is None \
                            or self.get_request().status_code != 200:
            return True
        return False
    
    def get_html(self):
        return BeautifulSoup(self.get_request().text, 'html5lib')

    # method to get all elements with given tag
    def get_elements_by_tag(self, tag):
        return self.get_html().find_all(tag)
