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
                  'https://www.ratebeer.com/beer/kronenbourg-(original)/4457/1/1/',
                  'https://www.ratebeer.com/beer/kronenbourg-panach%C3%A9/39094/1/1/',
                    'https://www.ratebeer.com/beer/kronenbourg-7.2-blonde/103308/1/1/',
                    'https://www.ratebeer.com/beer/kronenbourg-1664-blanc/35424/1/1/',
                    'https://www.ratebeer.com/beer/leffe-blonde/2514/1/1/',
                    'https://www.ratebeer.com/beer/leffe-tripel-(triple)/2515/1/1/',
                    'https://www.ratebeer.com/beer/leffe-9%C2%B0-%2F-rituel-9/56545/1/1/',
                    'https://www.ratebeer.com/beer/leffe-ruby/91345/1/1/',
                    'https://www.ratebeer.com/beer/leffe-nectar-(tradition-des-moines)/169229/1/1/',
                    'https://www.ratebeer.com/beer/leffe-des-vignes/327362/1/1/',
                    'https://www.ratebeer.com/beer/la-chouffe/1614/1/1/',
                    'https://www.ratebeer.com/beer/heineken/37/1/1/',
                    'https://www.ratebeer.com/beer/bavaria-8.6-(original)/5588/1/1/',
                    'https://www.ratebeer.com/beer/kellegen-extra-forte-8.0/107281/1/1/',
                    'https://www.ratebeer.com/beer/kellegen-pur-malt/50853/1/1/',
                    'https://www.ratebeer.com/beer/davelghem-blonde/117003/1/1/',
                    'https://www.ratebeer.com/beer/fischer-tradition/9760/1/1/',  
                    'https://www.ratebeer.com/beer/hoegaarden/399/1/1/',
                    'https://www.ratebeer.com/beer/hoegaarden-radler-agrum/320429/1/1/',
                    'https://www.ratebeer.com/beer/hoegaarden-radler-lemon--and--lime/320430/1/1/',
                    'https://www.ratebeer.com/beer/hoegaarden-ros%C3%A9e/73158/1/1/',
                    'https://www.ratebeer.com/beer/desperados/4007/1/1/',
                    'https://www.ratebeer.com/beer/desperados-red/94499/1/1/',
                    'https://www.ratebeer.com/beer/desperados-verde/231958/1/1/',
                    'https://www.ratebeer.com/beer/gayant-la-goudale/9157/1/1/',
                    'https://www.ratebeer.com/beer/amsterdam-navigator/8970/1/1/',
                    'https://www.ratebeer.com/beer/amsterdam-maximator/9935/1/1/',
                    'https://www.ratebeer.com/beer/amsterdam-mariner/7270/1/1/',
                    'https://www.ratebeer.com/beer/amsterdam-explorator/15595/1/1/',
                    'https://www.ratebeer.com/beer/mort-subite-kriek/2555/1/1/',
                    'https://www.ratebeer.com/beer/pelforth-brune/4461/1/1/',
                    'https://www.ratebeer.com/beer/pelforth-blonde/4484/1/1/',
                    'https://www.ratebeer.com/beer/affligem-blonde/3733/1/1/'
                    'https://www.ratebeer.com/beer/affligem-dubbel---double/3735/1/1/',
                    'https://www.ratebeer.com/beer/affligem-tripel/3734/1/1/',
                    'https://www.ratebeer.com/beer/grimbergen-blonde/3948/1/1/',
                    'https://www.ratebeer.com/beer/grimbergen-cuv%C3%A9e-ambr%C3%A9e---double-(dubbel)/2978/1/1/',
                    'https://www.ratebeer.com/beer/faxe-10/9950/1/1/',
                    'https://www.ratebeer.com/beer/faxe-premium/7402/1/1/',
                    'https://www.ratebeer.com/beer/duyck-jenlain-ambr%C3%A9e/4677/1/1/',
                    'https://www.ratebeer.com/beer/kronenbourg-panach%C3%A9/39094/1/1/',
                    'https://www.ratebeer.com/beer/fischer-merida/83030/1/1/',
                    'https://www.ratebeer.com/beer/delirium-tremens/1039/1/1/',
                    'https://www.ratebeer.com/beer/dubuisson-cuv%C3%A9e-des-trolls/10682/1/1/',
                    'https://www.ratebeer.com/beer/cuv%C3%A9e-des-trolls-cuv%C3%A9e-sp%C3%A9ciale/134156/1/1/',
                    'https://www.ratebeer.com/beer/maredsous-8-brune-bruin/2526/1/1/',
                    'https://www.ratebeer.com/beer/maredsous-10-tripel/2527/1/1/',
                    'https://www.ratebeer.com/beer/st.-sylvestre-3-monts/7321/1/1/',
                    'https://www.ratebeer.com/beer/pietra/8613/1/1/',
                    'https://www.ratebeer.com/beer/tuborg-sk%C3%B8ll/203775/1/1/',
                    'https://www.ratebeer.com/beer/tuborg-sk%C3%B8ll-ice-apple/417305/1/1/',
                    'https://www.ratebeer.com/beer/corona-extra/742/1/1/',
                    'https://www.ratebeer.com/beer/cubanisto/261743/1/1/',
                    'https://www.ratebeer.com/beer/cubanisto---mojito-flavour/500809/1/1/',
                    'https://www.ratebeer.com/beer/carlsberg-pilsner/709/1/1/',
                    'https://www.ratebeer.com/beer/affligem-cuv%C3%A9e-florem/256788/1/1/',
                    'https://www.ratebeer.com/beer/maredsous-10-tripel/2527/1/1/',
                    'https://www.ratebeer.com/beer/gayant-la-biere-du-demon/4490/1/1/',
                    'https://www.ratebeer.com/beer/jupiler/8042/1/1/',
                    'https://www.ratebeer.com/beer/saint-omer-1866/18145/1/1/',
                    'https://www.ratebeer.com/beer/edelweiss-weissbier-snowfresh/72025/1/1/',
                    'https://www.ratebeer.com/beer/stella-artois/1478/1/1/',
                    'https://www.ratebeer.com/beer/buckler-0%2C0-blanca/216646/1/1/',
                  ]

    

    
    def parse(self, response):
                

#           
        for i in range(10) : 
            if response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re('((?<=Aroma )\d+/\d+|(?<=<br) />\',$)') == []:
                    Aromes = 'NaN'
                    Appearance = 'NaN'
                    Taste = 'NaN'
                    Palate = 'NaN'
                    Overall = 'NaN'
            else :
                    Aromes = int(response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Aroma )\d+(?=/\d+)|(?<=<br) />\',$)')[0])
                    Appearance = int(response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Appearance )\d+(?=/\d+)|(?<=<br) />\',$)')[0])
                    Taste = int(response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Taste )\d+(?=/\d+)|(?<=<br) />\',$)')[0])
                    Palate = int(response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Palate )\d+(?=/\d+)|(?<=<br) />\',$)')[0])
                    Overall = int(response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Overall )\d+(?=/\d+)|(?<=<br) />\',$)')[0])
            
            if response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small')[i].re(r'(?<=href="/RatingsQA.htm">)does not count')==[] : 
                does_count = True
            else : 
                does_count = False
                
            if response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(?<=\\xa0\()(\d*)')[i]=='':
                nr_reviews = ''
            else :
                nr_reviews = int(response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/text()').re('(?<=\\xa0\()(\d*)')[i])
                
            tags = " ".join(response.xpath('//*[contains(concat(" ", @class, " "), " tags ")]//a//text()').extract())
            yield {
                            'beer_name' : response.xpath('//div[contains(concat(" ", @class, " "), " user-header ")]/h1/a/span/text()').extract_first(),
                            'total_rating_for_beer' : int(response.xpath('//*[contains(concat(" ", @class, " "), " stats-container ")]/small//big//span//text()').extract_first()),
                            'ratingValue /5' : float(response.xpath('//*[contains(concat(" ", @class, " "), " stats-container ")]/small/a/big/strong/span/text()').extract_first()),
                            'calories' : int(response.xpath('//*[contains(concat(" ", @class, " "), " stats-container ")]/small/big/text()').extract_first()),
                            'ABV %' : float(response.xpath('//*[contains(concat(" ", @class, " "), " stats-container ")]/small/big/strong/text()').re_first(r'.+(?=%)')),                            
#                            'rating_value' : response.xpath('//*[contains(concat(" ", @class, " "), " stats-container ")]/text()').extract_first(),
                            'bottle_availability' : response.xpath('//*[contains(concat(" ", @class, " "), " availability-box ")]//table//tr//td//p//text()').extract()[0]+" "+response.xpath('//*[contains(concat(" ", @class, " "), " availability-box ")]//table//tr//td//p//text()').extract()[1],
                            'tap_availability' : response.xpath('//*[contains(concat(" ", @class, " "), " availability-box ")]//table//tr//td//p//text()').extract()[2]+" "+response.xpath('//*[contains(concat(" ", @class, " "), " availability-box ")]//table//tr//td//p//text()').extract()[3],
                            'user' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small//a/@href').re('(?<=/user/)\d+')[i],
#                            'localisation' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small').re(r'(?<= - )(\s?|(.+[A-Z] ))(?=- [A-Z])')[i*2+1],
                            'localisation' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small').re(r'(?<= - )(\s?|(.+ ))(?=- [A-Z])')[i*2+1],
#                            .re('(?<=- )( |[^-]+)(?=- [A-Z])')[i],
                            'time_review' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//small').re('(?<= - )\w+ \d+, \d+\s?(?=<)')[i],
                            'nr_reviews' : nr_reviews,
#                            'score' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div/div/@title').extract()[i],
                            'note' :float(response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div/div/text()').extract()[i]),
                            #'Aromes' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Aroma )\d+/\d+|(?<=<br) />\',$)'),
                            'Aromes /10' : Aromes,
                            'Appearance /5': Appearance,
                            'Taste /10' : Taste,
                            'Palate /5' : Palate,
                            'Overall /20' : Overall,
#                					 'Appearance_old' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Appearance )\d+/\d+|(?<=<br) />\',$)'),
#                            'Taste' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Taste )\d+/\d+|(?<=<br) />\',$)'),
#                            'Palate' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Palate )\d+/\d+|(?<=<br) />\',$)'),
#                            'Overall' : response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div//div//@title')[i].re(r'((?<=Overall )\d+/\d+|(?<=<br) />\',$)'),
                            'comment' :response.xpath('//*[contains(concat(" ", @class, " "), " reviews-container ")]//div//div//div[contains(@style, "line-height: 1.5")]//text()').re(r'^(?!UPDATED).+')[i],
                            'does_count' : does_count,
                            'tags' : tags,
                            'adress': response.url,
                            'Nth_comment_page' : i+1,
                    }
        
        page_act = re.search(r'(?<=\d/)\d+(?=/>$)', str(response)).group()
        page_suiv = str(int(page_act) +1)
        next_page = response.urljoin(str(page_suiv)+'/')
        
        next_page = next_page[:-(len(str(page_suiv))+len(str(page_act))+2)]+next_page[-(len(str(page_suiv))+1):]
               
        if int(page_suiv) <= int(response.xpath('//*[contains(concat(" ", @class, " "), " ballno ")]/text()').extract()[-1]):
            yield response.follow(next_page, callback=self.parse)      
                
