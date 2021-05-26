# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZlibraryItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    author_name = scrapy.Field()
    publisher = scrapy.Field()
    year_published = scrapy.Field()
    book_language = scrapy.Field()
    img_link = scrapy.Field()
    
