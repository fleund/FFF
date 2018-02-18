# -*- coding: utf-8 -*-
import scrapy
#from scrapy.spiders import CrawlSpider, Rule
#from scrapy.linkextractors import LinkExtractor


class CasinoSpider(scrapy.Spider):
    name = 'casino'
    allowed_domains = ['mescoursescasino.fr']
    start_urls = ['http://www.mescoursescasino.fr/ecommerce/affichageCatalog/WE92528/C-104156-bieres']
    

#    rules = (
#            Rule(LinkExtractor(allow=('/ecommerce/affichageDetailProduit/WE92528/F-151131-203-_-bieres-et-panaches/')), callback='parse'),
#            )
    
    def parse(self, response):
        autes_pages = response.xpath('//div[contains(concat(" ", @class, " "), " central ")]/article/script').re('(?<={\\\'url\\\' :")/\w+\d+/\d+/\d+(?=", \\\')')
        for i in range(len(response.xpath('//div[contains(concat(" ", @class, " "), " description ")]/a/@title').extract())):
            yield{
                'beer' : response.xpath('//div[contains(concat(" ", @class, " "), " description ")]/a/@title')[i].extract(),
                'quantite' : response.xpath('*//span[contains(concat(" ", @class, " "), " info ")]/text()')[i].re(r'(?<=\t).+(?= \|)'),
                'prix/Litre': response.xpath('*//span[contains(concat(" ", @class, " "), " info ")]/text()')[i].re(r'(?<=\|).+(?=\r)'),
                'prix' : response.xpath('*//div[contains(concat(" ", @class, " "), " prix ")]/text()')[i].re(r'\d*,\d*'),
            }
#         
            
        pages_données = "http://www.mescoursescasino.fr/ecommerce/LazyLoadingListeProduits"+autres_pages
#            item = scrapy.Item()
#            item['beer'] = response.xpath('//div[contains(concat(" ", @class, " "), " description ")]/a/@title').extract()
#            item['quantite'] = response.xpath('*//span[contains(concat(" ", @class, " "), " info ")]/text()').re(r'(?<=\t).+(?= \|)')
#            item['prix_litre'] = response.xpath('*//span[contains(concat(" ", @class, " "), " info ")]/text()').re(r'(?<=\|).+(?=\r)')
#            item['prix'] = response.xpath('*//div[contains(concat(" ", @class, " "), " prix ")]/text()').re(r'\d*,\d*')
#            return item