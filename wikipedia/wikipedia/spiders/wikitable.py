# -*- coding: utf-8 -*-
import scrapy


class WikitableSpider(scrapy.Spider):
    name = 'wikitable'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/']

    def parse(self, response):
        pass
