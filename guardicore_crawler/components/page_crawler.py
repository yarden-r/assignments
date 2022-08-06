from guardicore_crawler.components.report import Report
from guardicore_crawler.components.url_parser import URLParser
from guardicore_crawler.components.html_tag import HTMLTag
from guardicore_crawler.components.broken_url import BrokenUrl
from guardicore_crawler.components.good_url import GoodUrl
from guardicore_crawler.helpers.thread import ThreadWrapper
from concurrent.futures import ThreadPoolExecutor as ThreadPool
class PageCrawler(object):
    """
    This class is responsible for crawling the web.
    """
    max_depth = 3
    
    def __init__(self, url, text, user_agent, file_name, depth=0):
        self.url = url
        self.user_agent = user_agent
        self.depth = depth
        self.text = text
        self.report = Report(file_name)
        self.url_parser = URLParser(url, user_agent)
        self.crawlers = []
        self.threads = []

    def __str__(self):
        return "PageCrawler: depth: {}, {}, {}".format(self.depth, self.url, self.text)

    def crawl(self):
       
        if self.url_parser.is_broken():
            # print("adding broken url")
            self.report.insert_item(BrokenUrl(self.depth, self.url))
            return
        
        # print("added good url")
        self.report.insert_item(GoodUrl(self.depth, self.url, self.text))
        
        if self.depth == self.max_depth:
            return

        
        
        print("depth: {}".format(self.depth))
        self.depth += 1
        links = self.url_parser.get_elements_by_tag('a')
        for link in links:
            tag = HTMLTag(link)
            text = tag.get_text()
            url = tag.get_attribute('href')
            
            if self.report.contains_name(url):
                continue
            self.crawlers.append(PageCrawler(url, text, self.user_agent,\
                                self.report.file_name, self.depth))
        
        with ThreadPool() as executor:
            for crawler in self.crawlers:
                executor.submit(crawler.crawl)
        # for crawler in self.crawlers:
            # print(crawler)
            # self.threads.append(ThreadWrapper(crawler.crawl))
            # self.threads[-1].start()
            
        # self.__wrap_up()
            
    
    def __wrap_up(self):
        for thread in self.threads:
            print("waiting for thread to finish")
            thread.join()
