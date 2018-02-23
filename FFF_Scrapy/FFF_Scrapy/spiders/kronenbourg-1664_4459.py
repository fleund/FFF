# -*- coding: utf-8 -*-
import scrapy
import re
import logging
from scrapy.linkextractors import LinkExtractor

class KronenbourgSpider(scrapy.Spider):
    name = 'kronenbourg'
    allowed_domains = ['www.ratebeer.com', 'ratebeer.com']
    start_urls = [
                  'https://www.ratebeer.com/beer/kronenbourg-1664/4459/1/1/',
                  'https://www.ratebeer.com/beer/kronenbourg-(original)/4457/1/1/',
                    'https://www.ratebeer.com/beer/kronenbourg-1664-blanc/35424/1/1/',
                    'https://www.ratebeer.com/beer/leffe-blonde/2514/1/1/',
                    'https://www.ratebeer.com/beer/leffe-tripel-(triple)/2515/1/1/',
                    'https://www.ratebeer.com/beer/leffe-9%C2%B0-%2F-rituel-9/56545/1/1/',
                    'https://www.ratebeer.com/beer/leffe-ruby/91345/1/1/',
                    'https://www.ratebeer.com/beer/la-chouffe/1614/1/1/',
                    'https://www.ratebeer.com/beer/heineken/37/1/1/',
                    'https://www.ratebeer.com/beer/bavaria-8.6-(original)/5588/1/1/',
                    'https://www.ratebeer.com/beer/kellegen-extra-forte-8.0/107281/1/1/',
                    'https://www.ratebeer.com/beer/davelghem-blonde/117003/1/1/',
                    'https://www.ratebeer.com/beer/fischer-tradition/9760/1/1/',
                  ]
    page_suiv=1
    
    rules = (
            Rule(LinkExtractor(allow=)))
                  
#    def start_requests(self):
#            urls= [
#                'https://www.ratebeer.com/beer/kronenbourg-1664/4459/'       
#            ]
#            for url in urls :
#                    yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for truc in response.css('.reviews-container'):
                yield {
                            'beer_name' : truc.xpath('//div[contains(concat(" ", @class, " "), " user-header ")]/h1/a/span/text()').extract_first(),
                            'user' : truc.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/@href').re_first('(?<=/user/)\d+'),
                            'localisation' : truc.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small').re_first('(?<=\ - ).+(?= -)'),
                            'time_review' : truc.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small').re_first('(?<= - )\w+ \d+, \d+(?=</small>)'),
                            'nr_reviews' : truc.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re_first('(?<=\\xa0\()(\d+)'),
                            'score' :   truc.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div/div/@title').extract_first(),
#                            'comment' :response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]/div/div/div/text()').extract(),
                            
                    }
                
#                yield {
#                            'beer_name' : response.xpath('//div[contains(concat(" ", @class, " "), " user-header ")]/h1/a/span/text()').extract_first(),
#                            'user' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/@href').re_first('(?<=/user/)\d+'),
#                            'localisation' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small').re_first('(?<=\ - ).+(?= -)'),
#                            'time_review' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small').re_first('(?<= - )\w+ \d+, \d+(?=</small>)'),
#                            'nr_reviews' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re_first('(?<=\\xa0\()(\d+)'),
#                            'score' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div/div/@title').extract_first(),
##                            'comment' :response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]/div/div/div/text()').extract(),
#                            
#                    }
                


                
#                for notation in response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title') :
#                            yield {
#                                        'note' :notation.re_first(r'(\d out of 5\.0|\d\.\d out of 5\.0)'),
#                                        'Aromes' : notation.re_first(r'(?<=Aroma )\d+/\d+'),
#                                        'Appearance' : notation.re_first(r'(?<=Appearance )\d+/\d+'),
#                                        'Taste' : notation.re_first(r'(?<=Taste )\d+/\d+'),
#                                        'Palate' : notation.re_first(r'(?<=Palate )\d+/\d+'),
#                                        'Overall' : notation.re_first(r'(?<=Overall )\d+/\d+'),
#                                   }
                                   
                                   #yield {
#                            'beer_name' : response.xpath('//div[contains(concat(" ", @class, " "), " user-header ")]/h1/a/span/text()').extract_first(),
#                            'user' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(\w+)(?=\\xa0)'),
#                            'nr_reviews' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(?<=\\xa0\()(\d+)'),
#                            'comment' :response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]/div/div/div/text()').extract(),
#                            'note' :response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div/div/text()').extract(),
##                            'Aromes' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re_first(r'(?<=Aroma )\d+/\d+'),
##                            'Appearance' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re_first(r'(?<=Appearance )\d+/\d+'),
##                            'Taste' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re_first(r'(?<=Taste )\d+/\d+'),
##                            'Palate' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re_first(r'(?<=Palate )\d+/\d+'),
##                            'Overall' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title').re_first(r'(?<=Overall )\d+/\d+'),
#                        }                    
                           
                
            page_act = re.search(r'(?<=\d/)\d+(?=/>$)', str(response)).group()
            page_suiv = str(int(page_act) +1)
            next_page = response.urljoin(str(page_suiv)+'/')
            
            next_page = next_page[:-(len(str(page_suiv))+len(str(page_act))+2)]+next_page[-(len(str(page_suiv))+1):]
            self.logger.info(next_page)
                
            if int(page_suiv)<=3:                
#            if int(page_suiv) <= int(response.xpath('//*[contains(concat(" ", @class, " "), " ballno ")]/text()').extract()[-1]):
                yield response.follow(next_page, callback=self.parse)
                