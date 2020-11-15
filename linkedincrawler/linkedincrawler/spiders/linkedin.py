# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class LinkedinSpider(Spider):
    name = 'linkedin'
    allowed_domains = ['linkedin.com']
    start_urls = ['https://www.linkedin.com/']
    driver = None

    def parse(self, response):
        page = 1
        self.driver = webdriver.Chrome(r'C:\Users\melch\Documents\GitHub\py_web_crawler\LIB\driver\chromedriver.exe')
        #driver.maximize_window()
        self.driver.get('https://www.linkedin.com/login')

        #LOGIN
        usr = getattr(self,'usr','')
        pwd = getattr(self,'pwd','')
        self.driver.find_element_by_xpath('//input[@name="session_key"]').send_keys(usr)
        self.driver.find_element_by_xpath('//input[@name="session_password"]').send_keys(pwd)
        self.driver.find_element_by_xpath('//button[@data-litms-control-urn="login-submit"]').click()
        sleep(3)

        #SEARCH TYPE
        #1º and 2º
        #https://www.linkedin.com/search/results/people/?facetNetwork=%5B%22F%22%2C%22S%22%5D&origin=FACETED_SEARCH

        #1º
        #https://www.linkedin.com/search/results/people/?facetNetwork=%5B%22F%22%5D&origin=FACETED_SEARCH

        #SEARCH
        self.driver.get(r'https://www.linkedin.com/search/results/people/?facetNetwork=%5B%22F%22%5D&origin=FACETED_SEARCH')
        
        if getattr(self, 'search', ''):
            self.driver.find_element_by_xpath('//input[starts-with(@class, "search-global-typeahead__input")]').send_keys(getattr(self, 'search', ''))
            self.driver.find_element_by_xpath('//input[starts-with(@class, "search-global-typeahead__input")]').send_keys(Keys.RETURN)
            sleep(3)
        else:
            pass #parse every result

        #PARSE SEARCH RESULT
        while True:
            try:
                self.logger.info('##########> PARSING PAGE ' + str(page))

                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.25)")
                sleep(0.5)
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.50)")
                sleep(0.5)
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.75)")
                sleep(0.5)
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight*1.00)")
                sleep(0.5)
                sel = Selector(text=self.driver.page_source)
                
                lis = sel.xpath('.//li')
                for li in lis:
                    name = li.xpath('.//span[@class="name actor-name"]/text()').extract_first()
                    connection_grade =  li.xpath('.//span[@class="dist-value"]/text()').extract_first()
                    subline = li.xpath('.//p[contains(@class, "subline-level-1")]/text()').extract_first()
                    local = li.xpath('.//p[contains(@class, "subline-level-2")]/text()').extract_first()
                    
                    if name:
                        if subline:
                            subline = subline.strip()
                        if local:
                           local = local.strip()

                        yield {
                            'name': name, 
                            'connection_grade': connection_grade,
                            'subline': subline,
                            'local': local
                        }
                 #next page?
                next_page = self.driver.find_element_by_xpath('//button[contains(@aria-label, "Avançar")][not(@disabled)]')
                next_page.click() #Will throuw noSuchElementException at the last page due to @disable
                page += 1
                sleep(2)
            except NoSuchElementException: 
                self.logger.info('No more pages to load.')
                self.driver.quit()
                break



           
        