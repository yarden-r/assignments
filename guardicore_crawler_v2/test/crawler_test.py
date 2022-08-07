from guardicore_crawler_v2.components.page_crawler import PageCrawler
from time import perf_counter
if __name__ == "__main__":
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
    crawler = PageCrawler('https://www.google.com/',\
                             user_agent, 'report.txt')
    crawler.report.clear()
    start = perf_counter()
    crawler.crawl()
    crawler.wrap_up()
    end = perf_counter()
    print("Time: {}".format(end - start))


    