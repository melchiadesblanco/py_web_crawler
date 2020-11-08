# -*- coding: utf-8 -*-
from time import sleep
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException
 

class SeleniumSpider(Spider):
    name = 'selenium'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver = webdriver.Chrome('C:\\Users\\melch\\Documents\\GitHub\\stock_crawler\\stock_crawler\\stock_crawler\\driver\\chromedriver.exe')
        #self.driver.get('http://books.toscrape.com')
        self.driver.get('http://books.toscrape.com/catalogue/page-40.html')

        # sel = Selector(text=self.driver.page_source)
        # books = sel.xpath('//h3/a/@href').extract()

        # for book in books:
        #     url = 'http://books.toscrape.com/' + book
        #     yield Request(url, callback=self.parse_book)

        while True:
            try:
                next_page = self.driver.find_element_by_xpath('/html/body/div/div/div/div/section/div[2]/div/ul/li/a[text()="next"]')
                
                sleep(3)
                self.logger.info('Sleep for 3 secs')
                next_page.click()
                sel = Selector(text=self.driver.page_source)
                books = sel.xpath('//h3/a/@href').extract()
                for book in books:
                    url = 'http://books.toscrape.com/' + book
                    yield Request(url, callback=self.parse_book)
                    
            except NoSuchElementException:
                self.logger.info('No more pages to load')
                self.driver.quit()
                break

    def parse_book(self, response):
        pass