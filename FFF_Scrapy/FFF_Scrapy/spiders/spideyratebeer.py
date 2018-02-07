# -*- coding: utf-8 -*-
import scrapy
import re
import logging

class SpideyratebeerSpider(scrapy.Spider):
    name = 'spideyratebeer'
    allowed_domains = ['www.ratebeer.com', 'ratebeer.com']
    start_urls = [
                  'https://www.ratebeer.com/beer/kronenbourg-1664/4459/'
                  ]

                  
#    def start_requests(self):
#            urls= [
#                'https://www.ratebeer.com/beer/kronenbourg-1664/4459/'       
#            ]
#            for url in urls :
#                    yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
#            reAromes=[]
##            test = response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').extract(),
#            test = response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').extract(),
#            for i in range(len(test)):
#                reAromes[i] = re.search(r'(?<=Aroma )\d+/\d+', test[i]).group(),
#                print (reAromes)
            Aromes = response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re(r'(?<=Aroma )\d+/\d+')
            if Aromes is not None :
                self.logger.info('IIIIIIIIIIIIIIIMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMIIIIIIIIIIIIIiii')
                yield {
                    'user' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(\w+)(?=\\xa0)'),
                    'nr_reviews' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(?<=\\xa0\()(\d+)'),
                    'Aromes' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re(r'(?<=Aroma )\d+/\d+'),
                    'Appearance' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re(r'(?<=Appearance )\d+/\d+'),
                    'Taste' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re(r'(?<=Taste )\d+/\d+'),
                    'Palate' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re(r'(?<=Palate )\d+/\d+'),
                    'Overall' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re(r'(?<=Overall )\d+/\d+'),
                }
            else : 
                self.logger.info('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
                yield {
                    'user' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(\w+)(?=\\xa0)'),
                    'nr_reviews' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(?<=\\xa0\()(\d+)'),
                    'Aromes' : 'NaN',
                    'Appearance' : 'NaN',
                    'Taste' : 'NaN',
                    'Palate' : 'NaN',
                    'Overall' : 'NaN',
                }