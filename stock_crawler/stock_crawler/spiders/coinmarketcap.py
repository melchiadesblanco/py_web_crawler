# -*- coding: utf-8 -*-
import scrapy


class CoinmarketcapSpider(scrapy.Spider):
    name = 'coinmarketcap'
    allowed_domains = ['coinmarketcap.com']
    start_urls = ['https://coinmarketcap.com/all/views/all/']

    def parse(self, response):
        currency_rank   = response.xpath('/html/body/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div/table/tbody/tr/td[1]/div/text()')
        #currency_img = 
        currency_name   = response.xpath('/html/body/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div/table/tbody/tr/td/div/a/text()')
        currency_symbol = response.xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div/table/tbody/tr/td[3]/div/text()')
        currency_cap    = response.xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div/table/tbody/tr/td[4]/p/text()')
        currency_price  = response.xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div/table/tbody/tr/td[5]/a/text()')
        currency_supply = response.xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div/table/tbody/tr/td[6]/div/text()')
        currency_volume = response.xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div/table/tbody/tr/td[7]/a/text()')
        currency_var1h  = response.xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div/table/tbody/tr/td[8]/div/text()')
        currency_var24h = response.xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div/table/tbody/tr/td[9]/div/text()')
        currency_Var7d  = response.xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div/table/tbody/tr/td[10]/div/text()')
   
        print ("########################")
        print(currency_name.extract_first())
        print ("########################")

    def persist(self):
        pass