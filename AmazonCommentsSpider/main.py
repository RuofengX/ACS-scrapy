from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from AmazonCommentsSpider.spiders.comment import CommentSpider
import AmazonCommentsSpider.settings


process: CrawlerProcess = CrawlerProcess(settings=get_project_settings())
process.crawl(CommentSpider)
process.start() # the script will block here until the crawling is finished