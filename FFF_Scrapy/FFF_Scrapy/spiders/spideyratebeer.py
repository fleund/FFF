# -*- coding: utf-8 -*-
import scrapy


class SpideyratebeerSpider(scrapy.Spider):
    name = 'spideyratebeer'
    allowed_domains = ['https://www.ratebeer.com/']
    start_urls = ['https://www.ratebeer.com/beer/kronenbourg-1664/4459/']

    def start_requests(self):
            urls= [
                'https://www.ratebeer.com/beer/kronenbourg-1664/4459/'       
            ]
            for url in urls :
                    yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
            for ratebeer in response.xpath('div.ratebeer'):
#                Modificaiton pour git
                yield {
                    test = response.xpath('//*[contains(concat(" ",@class," ")," reviews-container ")]//div//div//div//div//@title').extract()
                    for i in range(len(test)):
                        reAromes[i] = re.search(r'(?<=Aroma )\d+/\d+', test[i])
#                    if(reAromes[i]) is None : 
#                        reAromes[i]="NaN"
                    
                }
                    