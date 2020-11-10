# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import FormRequest

class FormreqSpider(Spider):
    name = 'formreq'
    allowed_domains = ['www.hkexnews.hk']
    start_urls = ['https://www.hkexnews.hk/sdw/search/searchsdw.aspx']

    def parse(self, response):
        data = {'__EVENTTARGET': 'btnSearch',
        '__VIEWSTATE': response.xpath('//*[@name="__VIEWSTATE"]/@value').extract_first(),
        '__VIEWSTATEGENERATOR': response.xpath('//*[@name="__VIEWSTATEGENERATOR"]/@value').extract_first(),
        'today': '20201109',
        'sortBy': 'shareholding',
        'sortDirection': 'desc',
        'txtShareholdingDate': '2020/11/09',
        'txtStockCode': '00001'}

        page = FormRequest('https://www.hkexnews.hk/sdw/search/searchsdw.aspx', formdata=data)

        #At this point, the result should be visible in response?
        #PARSING PHASE
    
        table = response.xpath('//table[@class="table table-scroll table-sort table-mobile-list "]')
        trs = table.xpath('.//tr')
        for tr in trs:
            participant_id = tr.xpath('.//td[@class="col-participant-id"]/div[@class="mobile-list-body"]/text()').extract_first()
            name = tr.xpath('.//td[@class="col-participant-name"]/div[@class="mobile-list-body"]/text()').extract_first()
            address = tr.xpath('.//td[@class="col-address"]/div[@class="mobile-list-body"]/text()').extract_first()
            shareholding = tr.xpath('.//td[@class="col-shareholding text-right"]/div[@class="mobile-list-body"]/text()').extract_first()
            number_issues = tr.xpath('.//td[@class="col-shareholding-percent text-right"]/div[@class="mobile-list-body"]').extract_first()

            yield {
                'participant_id': participant_id,
                'name': name,
                'address': address,
                'shareholding': shareholding,
                'number_issues': number_issues
            }