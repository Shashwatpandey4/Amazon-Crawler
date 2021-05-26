import scrapy
from ..items import ZlibraryItem

class ZCrawlerSpider(scrapy.Spider):
    name = 'z_crawler'
    page_no = 2
    allowed_domains = ['1lib.in']
    start_urls = ['https://1lib.in/Algorithms-and-Data-Structures-cat71']

    def parse(self, response):
        items = ZlibraryItem()

        book_name = response.css('h3 a').css('::text').extract()
        author_name = response.css('.color1').css('::text').extract()
        publisher = response.css('h3+ div a').css('::text').extract()
        year_published = response.css('.property_year .property_value').css('::text').extract()
        book_language = response.css('.property_language .property_value').css('::text').extract()
        img_link = response.css('img.cover.lazy::attr(srcset)').extract()
        
        items["book_name"] = book_name
        items["author_name"] = author_name
        items["publisher"] = publisher
        items["year_published"] = year_published
        items["book_language"] = book_language
        items["img_link"] = img_link

        yield items

        next_page = 'https://1lib.in/Algorithms-and-Data-Structures-cat71?page='+str(ZCrawlerSpider.page_no)
        
        if ZCrawlerSpider.page_no <= 10:
            ZCrawlerSpider.page_no += 1
            yield response.follow(next_page,callback=self.parse)
