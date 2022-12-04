# Scrapy settings for AmazonCommentsSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'AmazonCommentsSpider'

LOG_LEVEL = 'INFO'

SPIDER_MODULES = ['AmazonCommentsSpider.spiders']
NEWSPIDER_MODULE = 'AmazonCommentsSpider.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
DOWNLOAD_TIMEOUT = 3

RETRY_ENABLED = True
RETRY_TIMES = 60

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

FEEDS = {
    'result.csv': {
        'format': 'csv',
    },
}