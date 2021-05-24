import scrapy
from ..items import AmazonscrapItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_no = 2
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1621793680&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0'
        ]

    def parse(self, response):
        items = AmazonscrapItem()

        book_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        author_name = response.css('.a-color-secondary .a-row .a-size-base+ .a-size-base').css('::text').extract()
        price = response.css('.a-price-whole').css('::text').extract()
        img_link = response.css('.s-image::attr(src)').extract()
        
        items["book_name"] = book_name
        items["author_name"] = author_name
        items["price"] = price
        items["img_link"] = img_link

        yield items

        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page='+str(AmazonSpiderSpider.page_no)+'&qid=1621845589&rnid=1250225011&ref=sr_pg_'+str(AmazonSpiderSpider.page_no)
        
        if AmazonSpiderSpider.page_no <= 75 :
            AmazonSpiderSpider.page_no += 1
            yield response.follow(next_page,callback=self.parse)