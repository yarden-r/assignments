from guardicore_crawler.components.page_crawler import PageCrawler

if __name__ == "__main__":
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
    crawler = PageCrawler('http://www.google.com', 'HomePage',\
                             user_agent, 'report.txt')
    crawler.crawl()
    