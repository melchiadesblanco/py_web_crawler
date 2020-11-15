# -*- coding: utf-8 -*-
from scrapy import Spider
from selenium import webdriver
from time import sleep

class LinkedinSpider(Spider):
    name = 'linkedin'
    allowed_domains = ['linkedin.com']
    start_urls = ['https://www.linkedin.com/login']

    def parse(self, response):
        driver = webdriver.Chrome(r'C:\Users\melch\Documents\GitHub\py_web_crawler\LIB\driver\chromedriver.exe')
        driver.maximize_window()
        driver.get('https://www.linkedin.com/')

        #driver.get_element_by_xpath()
        driver.find_element_by_xpath('//input[@name="session_key"]').send_keys('melchiades.blanco@live.com')
        sleep(10) # time to type the password
        driver.find_element_by_xpath('//button[@class="sign-in-form__submit-button"]').click()

