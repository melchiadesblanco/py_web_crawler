# -*- coding: utf-8 -*-
import scrapy
from scrapy_items.items import ScrapyItemsItem


class SampleItemsSpider(scrapy.Spider):
    name = 'sample_items'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        authors = response.xpath('//*[@class="author"]/text()').extract()

        item = ScrapyItemsItem()
        item['authors'] = authors
        return item
        
         
