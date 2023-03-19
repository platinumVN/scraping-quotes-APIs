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
        quotes = response_json.get("quotes")
        has_next_page = response_json.get('has_next')
        yield {
            'current_page' : current_page,
            'quotes_data' : quotes 
        }

        # if next page exists:
        if has_next_page:
            next_page_url = f"https://quotes.toscrape.com/api/quotes?page={int(current_page) + 1}"

            yield scrapy.Request(
                url=next_page_url,
                callback=self.parse
            )
