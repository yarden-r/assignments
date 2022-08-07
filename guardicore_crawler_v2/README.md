Author: Yarden Regev

Disclaimers:
1. The Python implementation used in this project is CPython - Python3
2. Make sure to run 'export PYTHONPATH=<parent directory of guardicore_crawler>'
3. Make sure to install the following libraries:
   a. pip install requests - for sending HTTP requests
   b. pip install html5lib - HTML parser used
   c. pip install bs4      - library for extracting information from page
4. www.guardicore.com is blocked for crawling
5. Since this crawler is for crawling through the whole web,
   if requested depth is over 2 it will take a long time
6. Notice example run in report_example.txt

Instructions:
1. Make sure to pass in correct user agent for your machine, you can find out 
   in this link 'https://deviceatlas.com/blog/list-of-user-agent-strings#desktop'

2. Import PageCrawler module from from guardicore_crawler_v2.components.page_crawler

3. PageCrawler initializer takes 6 parameters
      url = url of the page you want to crawl,
      user_agent = user agent of machine
      file_name = output file to write report to
      max_depth = how deep do you want to go in the web
      text = the text between the 'a' tags, defaults to "HomePage",
             you can change with whatever description you want
      depth = depth of current page, defaults to 0

4. After making PageCrawler, use crawl() method and then use wrap_up() method

Notes:
1. In hindsight a threadpool would have been fit to use to manage threads
2. Please refere to png file for UML diagram of project