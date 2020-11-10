# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class WikitableSpider(Spider):
    name = 'wikitable'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']

    def parse(self, response):
        table =  response.xpath('//table[contains(@class, "wikitable sortable")][1]')
        trs = table.xpath('.//tr')[1:]

        for tr in trs:
            #GETTER ROUND
            rank  = tr.xpath('./td[1]/text()').extract_first()
            city  = tr.xpath('./td[2]//a/text()').extract_first()
            state = tr.xpath('.//*[@class="flagicon"]/following-sibling::a/text()|'
                             './/*[@class="flagicon"]/following-sibling::text()').extract_first()

            #DATA CLEANING ROUND
            if city == '[k]':
                city  = tr.xpath('./td[2]//a/i/text()').extract_first()

            #YIELDING RESULT
            yield {
                'rank': rank.replace('\n', ''),
                'city': city.replace('\n', ''), 
                'state': state.replace('\n', '')
            }
