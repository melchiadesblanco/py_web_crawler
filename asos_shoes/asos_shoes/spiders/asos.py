# -*- coding: utf-8 -*-
import scrapy


class AsosSpider(scrapy.Spider):
    name = 'asos'
    allowed_domains = ['asos.com']
    start_urls = ['http://asos.com/']

    def parse(self, response):
        pass
