# -*- coding: utf-8 -*-
import scrapy


class SpideyratebeerSpider(scrapy.Spider):
    name = 'spideyratebeer'
    allowed_domains = ['https://www.ratebeer.com/beer-ratings/']
    start_urls = ['http://https://www.ratebeer.com/beer-ratings//']

    def start_requests(self):
            urls= [
                'https://www.ratebeer.com/beer/silly-rouge-red/375576/252123/'       
            ]
            for url in urls :
                    yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = [1]
        filename = 'ratebeer-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)