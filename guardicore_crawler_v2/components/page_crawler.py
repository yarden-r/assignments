from guardicore_crawler_v2.components.report import Report
from guardicore_crawler_v2.components.url_parser import URLParser
from guardicore_crawler_v2.components.html_tag import HTMLTag
from guardicore_crawler_v2.components.broken_url import BrokenUrl
from guardicore_crawler_v2.components.good_url import GoodUrl
from guardicore_crawler_v2.helpers.global_threadpool import GlobalThreadPool
from guardicore_crawler_v2.helpers.thread import ThreadWrapper
class PageCrawler(object):
    """
    This class is responsible for crawling the web.
    """
    max_depth = 2
    
    def __init__(self, url , user_agent, file_name,text = 'HomePage', depth=0):
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
       
        print ("Crawling: {}".format(self.url))
        if self.depth == 0 and self.url_parser.is_broken():
            self.report.insert_item(BrokenUrl(self.url))
            return
        
        self.report.insert_item(GoodUrl(self.depth, self.url, self.text))
        
        if self.depth == self.max_depth:
            return

        
        self.depth += 1
        links = self.url_parser.get_elements_by_tag('a')
        for link in links:
            tag = HTMLTag(link)
            text = tag.get_text()
            url = tag.get_attribute('href')
            
            if self.report.contains_name(url):
                continue
            
            p = PageCrawler(url, self.user_agent, self.report.file_name, text, self.depth)

            if p.url_parser.is_broken():
                self.report.insert_item(BrokenUrl(self.depth, url))
                continue

            self.crawlers.append(p)
        

        for crawler in self.crawlers:
            self.threads.append(ThreadWrapper(crawler.crawl))
        
        for thread in self.threads:
            thread.start()
        
        print("crawled {} in depth {}".format(self.url, self.depth))

    def wrap_up(self):
        for thread in self.threads:
            thread.join()