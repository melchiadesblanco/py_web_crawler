# -*- coding: utf-8 -*-
from scrapy import Spider


class CrunchbaseSpider(Spider):
    name = 'crunchbase'
    allowed_domains = ['crunchbase.com']
    start_urls = ['https://www.crunchbase.com/organization/medical-body-sculpting#section-overview']

    def parse(self, response):
        pass
