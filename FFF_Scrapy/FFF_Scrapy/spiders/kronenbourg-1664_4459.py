# -*- coding: utf-8 -*-
import scrapy
import re
import logging

class KronenbourgSpider(scrapy.Spider):
    name = 'kronenbourg'
    allowed_domains = ['www.ratebeer.com', 'ratebeer.com']
    start_urls = [
                  'https://www.ratebeer.com/beer/kronenbourg-1664/4459/1/1/',
                  ]
    page_suiv=1

                  
#    def start_requests(self):
#            urls= [
#                'https://www.ratebeer.com/beer/kronenbourg-1664/4459/'       
#            ]
#            for url in urls :
#                    yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):

                yield {
                            'beer_name' : response.xpath('//div[contains(concat(" ", @class, " "), " user-header ")]/h1/a/span/text()').extract_first(),
                            'user' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/@href').re('(?<=/user/)\d+'),
                            'localisation' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small').re('(?<=\ - ).+(?= -)'),
                            'time_review' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small').re('(?<= - )\w+ \d+, \d+(?=</small>)'),
                            'nr_reviews' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(?<=\\xa0\()(\d+)'),
                            'score' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div/div/@title').extract_first().strip('<br />'),
                            'comment' :response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]/div/div/div/text()').extract(),
                            
                    }
                                
                for notation in response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title') :
                            yield {
                                        'note' :notation.re_first(r'(\d out of 5\.0|\d\.\d out of 5\.0)'),
                                        'Aromes' : notation.re_first(r'(?<=Aroma )\d+/\d+'),
                                        'Appearance' : notation.re_first(r'(?<=Appearance )\d+/\d+'),
                                        'Taste' : notation.re_first(r'(?<=Taste )\d+/\d+'),
                                        'Palate' : notation.re_first(r'(?<=Palate )\d+/\d+'),
                                        'Overall' : notation.re_first(r'(?<=Overall )\d+/\d+'),
                                   }
                                   
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
                
                if int(page_suiv) <= int(response.xpath('//*[contains(concat(" ", @class, " "), " ballno ")]/text()').extract()[-1]):
                    yield response.follow(next_page, callback=self.parse)
                