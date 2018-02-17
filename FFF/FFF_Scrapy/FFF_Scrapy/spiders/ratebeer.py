# -*- coding: utf-8 -*-
import scrapy
import re
import logging
from scrapy.loader import ItemLoader

import pprint as pp





class RatebeerSpider(scrapy.Spider):
    name = 'ratebeer'

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
    iterator = 'iternodes'
    itertag = 'item'
    


#    def start_requests(self):
#            urls= [
#                'https://www.ratebeer.com/beer/kronenbourg-1664/4459/'       
#            ]
#            for url in urls :
#                    yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
                

#           
        for i in range(10) : 
                yield {
                            'beer_name' : response.xpath('//div[contains(concat(" ", @class, " "), " user-header ")]/h1/a/span/text()').extract_first(),
                            'total_rating_for_beer' : response.xpath('//*[contains(concat(" ", @class, " "), " stats-container ")]/small//big//span//text()').extract_first(),
                            'ratingValue' : response.xpath('//*[contains(concat(" ", @class, " "), " stats-container ")]/small/a/big/strong/span/text()').extract_first()+'/5',
                            'calories' : response.xpath('//*[contains(concat(" ", @class, " "), " stats-container ")]/small/big/text()').extract_first(),
                            'ABV' : response.xpath('//*[contains(concat(" ", @class, " "), " stats-container ")]/small/big/strong/text()').extract_first(),                            
#                            'rating_value' : response.xpath('//*[contains(concat(" ", @class, " "), " stats-container ")]/text()').extract_first(),
                            'bottle_availability' : response.xpath('//*[contains(concat(" ", @class, " "), " availability-box ")]//table//tr//td//p//text()').extract()[0]+" "+response.xpath('//*[contains(concat(" ", @class, " "), " availability-box ")]//table//tr//td//p//text()').extract()[1],
                            'tap_availability' : response.xpath('//*[contains(concat(" ", @class, " "), " availability-box ")]//table//tr//td//p//text()').extract()[2]+" "+response.xpath('//*[contains(concat(" ", @class, " "), " availability-box ")]//table//tr//td//p//text()').extract()[3],
                            'user' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/@href').re('(?<=/user/)\d+')[i],
#                            'localisation' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small').re(r'(?<= - )(\s?|(.+[A-Z] ))(?=- [A-Z])')[i*2+1],
                            'localisation' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small').re(r'(?<= - )(\s?|(.+ ))(?=- [A-Z])')[i*2+1],
#                            .re('(?<=- )( |[^-]+)(?=- [A-Z])')[i],
                            'time_review' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small').re('(?<= - )\w+ \d+, \d+\s?(?=<)')[i],
                            'nr_reviews' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(?<=\\xa0\()(\d*)')[i],
#                            'score' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div/div/@title').extract()[i],
                            'note' :response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div/div/text()').extract()[i],
                            'Aromes' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Aroma )\d+/\d+|(?<=<br) />\',$)'),
                            'Appearance' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Appearance )\d+/\d+|(?<=<br) />\',$)'),
                            'Taste' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Taste )\d+/\d+|(?<=<br) />\',$)'),
                            'Palate' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Palate )\d+/\d+|(?<=<br) />\',$)'),
                            'Overall' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Overall )\d+/\d+|(?<=<br) />\',$)'),
                            'comment' :response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div[contains(@style, "line-height: 1.5")]//text()').re(r'^(?!UPDATED).+')[i],
                            'does_count' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small')[i].re(r'(?<=href="/RatingsQA.htm">)does not count'),
                            'tags' : response.xpath('//*[contains(concat(" ", @class, " "), " tags ")]//a//text()').extract(),
                            'adress': response.url,
                            'Nth_comment_page' : i+1,
                    }
        
        page_act = re.search(r'(?<=\d/)\d+(?=/>$)', str(response)).group()
        page_suiv = str(int(page_act) +1)
        next_page = response.urljoin(str(page_suiv)+'/')
        
        next_page = next_page[:-(len(str(page_suiv))+len(str(page_act))+2)]+next_page[-(len(str(page_suiv))+1):]
#                self.logger.info(next_page)
            
#        if int(page_suiv)<=20:                
        if int(page_suiv) <= int(response.xpath('//*[contains(concat(" ", @class, " "), " ballno ")]/text()').extract()[-1]):
            yield response.follow(next_page, callback=self.parse)      
                
