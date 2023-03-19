import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    # start_urls = ["https://quotes.toscrape.com/scroll"]
    start_urls = ["https://quotes.toscrape.com/api/quotes?page=1"]

    def parse(self, response):
        response_json = response.json()
        current_page = response_json.get("page")
        quotes = response_json.get(quotes)
        yield {
            'current_page' : current_page
        }
