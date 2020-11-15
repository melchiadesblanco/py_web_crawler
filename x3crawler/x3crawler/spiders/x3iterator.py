# -*- coding: utf-8 -*-
from time import sleep
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException
 


class X3iteratorSpider(Spider):
    name = 'x3iterator'
    #allowed_domains = ['x3.com']
    start_urls = ['https://intech.sageerpx3.com.br/auth/login/page']

    def start_requests(self):
        self.driver = webdriver.Chrome('C:\\Users\\melch\\Documents\\GitHub\\py_web_crawler\\LIB\\driver\\chromedriver.exe')
        #self.driver.get('http://books.toscrape.com')
        self.driver.get('https://intech.sageerpx3.com.br/auth/login/page')

        self.driver.find_element_by_id('login').send_keys('####')
        self.driver.find_element_by_id('password').send_keys('####')
        self.driver.find_element_by_xpath(r'/html/body/div/div/div[1]/form/div[4]/input[1]').click()

        #Wait for it to load
        sleep(5)
        #self.driver.find_element_by_css_selector('a[data-s-sitemap-link="restWebServices"]').get_attribute('href')

        self.driver.get(r'https://intech.sageerpx3.com.br/syracuse-main/html/main.html?url=%2Fsdata%2Fsyracuse%2Fcollaboration%2Fsyracuse%2FrestWebServices%3Frepresentation%3DrestWebService.%24query')

        sel = Selector(text=self.driver.page_source)
        trs = sel.xpath('//table/tr')
        for tr in trs:
            nome = tr.xpath('.//td[@class="s-grid-cell s-filter-criteria-col s-inplace"][1]/div[@class="s-inplace-value-read"]/a[@class="s-inplace-link"]/text()').extract_first()
            url_base = tr.xpath('.//td[@class="s-grid-cell s-filter-criteria-col s-inplace"][2]/div[@class="s-inplace-value-read"]/text()').extract_first()
            tipo_conteudo = tr.xpath('.//td[@class="s-grid-cell s-filter-criteria-col s-filter-criteria-col-with-btn s-inplace"][1]/div[@class="s-inplace-value-read"]/text()').extract_first()
            autenticacao = tr.xpath('.//td[@class="s-grid-cell s-filter-criteria-col s-filter-criteria-col-with-btn s-inplace"][2]/div[@class="s-inplace-value-read"]/text()').extract_first()

            yield {
                'nome': nome,
                'url_base': url_base,
                'tipo_conteudo': tipo_conteudo,
                'autenticacao' : autenticacao
            }


        # while True:
        #     try:
        #         next_page = self.driver.find_element_by_xpath('/html/body/div/div/div/div/section/div[2]/div/ul/li/a[text()="next"]')
                
        #         sleep(3)
        #         self.logger.info('Sleep for 3 secs')
        #         next_page.click()
        #         sel = Selector(text=self.driver.page_source)
        #         books = sel.xpath('//h3/a/@href').extract()
        #         for book in books:
        #             url = 'http://books.toscrape.com/' + book
        #             yield Request(url, callback=self.parse_book)
                    
        #     except NoSuchElementException:
        #         self.logger.info('No more pages to load')
        #         self.driver.quit()
        #         break

    def parse_book(self, response):
        pass
