# -*- coding: utf-8 -*-

# Scrapy settings for company_list project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'company_list'

SPIDER_MODULES = ['company_list.spiders']
NEWSPIDER_MODULE = 'company_list.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'company_list (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html


# DB_ADDR = '120.55.98.237'
# DB_PORT = 3306
# DB_USER = 'root'
# DB_PWD = '#!/root/Passw0rd@zeaho.com'
# DB_NAME = 'scrapy'

DB_ADDR = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PWD = '123456'
DB_NAME = 'scrapy'


DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
    'company_list.middlewares.ProxyMiddleWare': 25,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': None
}

