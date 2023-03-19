import scrapy
from scrapy import FormRequest

class QuotesLoginSpider(scrapy.Spider):
    name = "quotes_login"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/login"]

    def parse(self, response):
        """
            Payload of the login request include:
                csrf_token
                username
                password
        """
        csrf_token = response.xpath('//input[@name="csrf_token"]/@value').get()
        yield FormRequest.from_response(
            response,
            formxpath='//form',
            formdata={
                'csrf_token' : csrf_token,
                'username' : 'admin',
                'password' : 'admin'
            },
            callback=self.check_after_login
        )
    def check_after_login(self, response):
        """Verify that logged in
        """
        if response.xpath('//a[@href="/logout"]/text()').get():
            print('Successfully logged in')