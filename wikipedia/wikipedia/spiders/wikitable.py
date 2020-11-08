# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class WikitableSpider(Spider):
    name = 'wikitable'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']

    def parse(self, response):
        pass
