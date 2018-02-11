# -*- coding: utf-8 -*-
import scrapy
import re
import logging

class SpideyratebeerSpider(scrapy.Spider):
    name = 'spideyratebeer'
    allowed_domains = ['www.ratebeer.com', 'ratebeer.com']
    start_urls = [
                  'https://www.ratebeer.com/beer/kronenbourg-1664/4459/1/1/'
                  ]
    page_suiv=1

                  
#    def start_requests(self):
#            urls= [
#                'https://www.ratebeer.com/beer/kronenbourg-1664/4459/'       
#            ]
#            for url in urls :
#                    yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        #        while(page_suiv < 10) :
#        if response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re(r'(?<=Aroma )\d+/\d+') == []:
            yield {
                    'beer_name' : response.xpath('//div[contains(concat(" ", @class, " "), " user-header ")]/h1/a/span/text()').extract_first(),
                    'user' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(\w+)(?=\\xa0)'),
                    'nr_reviews' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(?<=\\xa0\()(\d+)'),
                    'comment' :response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]/div/div/div/text()').extract(),
                    'note' :response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div/div/text()').extract(),
                    'Aromes' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re(r'(?<=Aroma )\d+/\d+'),
                    'Appearance' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re(r'(?<=Appearance )\d+/\d+'),
                    'Taste' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re(r'(?<=Taste )\d+/\d+'),
                    'Palate' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re(r'(?<=Palate )\d+/\d+'),
                    'Overall' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re(r'(?<=Overall )\d+/\d+'),
                }
#        else : 
#                self.logger.info('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
#                yield {
#                    'user' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(\w+)(?=\\xa0)'),
#                    'nr_reviews' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(?<=\\xa0\()(\d+)'),
#                    'Aromes' : 'NaN',
#                    'Appearance' : 'NaN',
#                    'Taste' : 'NaN',
#                    'Palate' : 'NaN',
#                    'Overall' : 'NaN',
#                }
        
#            num_page = 
#            next_page = response.xpath('//*[contains(concat(" ", @class, " "), " ballno ")]['+str(page_suiv)+']/@href').extract()
#            if num_page is not None:
            page_act = re.search(r'(?<=\d/)\d+(?=/>$)', str(response)).group()
            page_suiv = str(int(page_act) +1)
            next_page = response.urljoin(str(page_suiv)+'/')
#            self.logger.info(next_page + "response.urljoin")
#            yield response.follow(next_page, self.parse)
#            self.logger.info(next_page[:-(len(str(page_suiv))+3)]+next_page[-(len(str(page_suiv))+1):])
            next_page = next_page[:-(len(str(page_suiv))+len(str(page_act))+2)]+next_page[-(len(str(page_suiv))+1):]
            self.logger.info(next_page)
#        self.logger.info(page_act + "page_act")
#        self.logger.info(page_suiv + "page_suiv")
#        self.logger.info(next_page + "next_page")
#            self.logger.info(str(len(str(page_suiv))) + "len page_suiv")
            if int(page_suiv) <= 176:
                yield response.follow(next_page, callback=self.parse)
#                else : 
#                    yield response.follow(next_page[:-(len(page_suiv)+2)]+next_page[-len(page_suiv):], self.parse)