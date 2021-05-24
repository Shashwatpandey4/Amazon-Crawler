import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotescrapItem

class Quotespider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/login"
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.form_response(response,formdata={
            'csrf_token':token,
            'username':'john cena',
            'password':'wwe'
        },callback=self.start_scraping)


    def start_scraping(self,response):
        open_in_browser(response)
        items = QuotescrapItem()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:

            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title']=title
            items['author']=author
            items['tag']=tag

            yield items

        next_page = 'https://quotes.toscrape.com/page/'+str(Quotespider.page_no)+'/'

        if Quotespider.page_no < 11:
            Quotespider.page_no += 1
            yield response.follow(next_page,callback = self.parse)
        


