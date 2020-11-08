# -*- coding: utf-8 -*-
import scrapy


class ClearcombrSpider(scrapy.Spider):
    name = 'clearcombr'
    allowed_domains = ['www.clear.com.br']
    start_urls = ['http://www.clear.com.br/']

    def parse(self, response):
        pass
