# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from dataclasses import dataclass


@dataclass
class CommentItem():
    friendly_name: str
    user_name: str
    rate: float
    comment: str
