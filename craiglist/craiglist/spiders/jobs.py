# # -*- coding: utf-8 -*-
# import scrapy


# class JobsSpider(scrapy.Spider):
#     name = 'jobs'
#     allowed_domains = ['newyork.craigslist.org']
#     start_urls = ['https://newyork.craigslist.org/search/egr']

#     def parse(self, response):
#         listings = response.xpath('//li[@class="result-row"]')
#         for listing in listings:
#             date = listing.xpath('.//*[@class="result-date"]/@datetime').extract_first()
#             link = listing.xpath('.//a[@class="result-title hdrlnk"]/@href').extract_first()
#             text = listing.xpath('.//a[@class="result-title hdrlnk"]/text()').extract_first()
            
#             yield scrapy.Request(link, 
#                                  callback=self.parse_listing, 
#                                  meta= { 
#                                     'date': date,
#                                     'link': link,
#                                     'text': text
#                                     })
#         next_page_url = response.xpath('//a[text()="next > "]/@href').extract_first()
#         if next_page_url:
#             yield scrapy.Request(response.urljoin(next_page_url) , callback=self.parse)

#     def parse_listing(self, response):
#         date = response.meta['date']
#         link = response.meta['link']
#         text = response.meta['text']

#         compensation = response.xpath('//p[@class="attrgroup"]/span[1]/b/text()').extract_first()
#         type = response.xpath('//*[@class="attrgroup"]/span[2]/b/text()').extract_first()
#         images = response.xpath('//*[@id="thumbs"]//@src').extract()
#         address = response.xpath('//*[@id="postingbody"]/text()').extract()

#         yield {
#             'date': date, 
#             'link': link,
#             'text': text,
#             'compensation': compensation,
#             'type': type,
#             'images': images,
#             'address': address
#         }
import scrapy
from scrapy import Request
 
class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://newyork.craigslist.org/search/egr"]
 
    def parse(self, response):
        jobs = response.xpath('//p[@class="result-info"]')
        for job in jobs:
            relative_url = job.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)
            title = job.xpath('a/text()').extract_first()
            address = job.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
            yield Request(absolute_url, callback=self.parse_page, meta={'URL': absolute_url, 'Title': title, 'Address':address})
        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        absolute_next_url = "https://newyork.craigslist.org" + relative_next_url
 
        yield Request(absolute_next_url, callback=self.parse)
 
    def parse_page(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        address = response.meta.get('Address')
        description = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').extract())
        compensation = response.xpath('//p[@class="attrgroup"]/span[1]/b/text()').extract_first()
        employment_type = response.xpath('//p[@class="attrgroup"]/span[2]/b/text()').extract_first()
 
        yield{'URL': url, 'Title': title, 'Address':address, 'Description':description, 'Compensation':compensation, 'Employment Type':employment_type}