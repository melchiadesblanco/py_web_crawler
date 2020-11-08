# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class ClasscentralspiderSpider(Spider):
    name = 'classcentralspider'
    allowed_domains = ['www.classcentral.com']
    start_urls = ['https://www.classcentral.com/subjects']

    def __init__(self, subject=None):
        self.subject = subject


    def parse(self, response):
        if self.subject:
            subjects_url = response.xpath('//a[contains(@title, "'+ self.subject +'")]').extract()
            if subjects_url:
                for subject in subjects_url:
                    absolute_url = response.urljoin(subject)
                    yield Request(absolute_url, callback=self.parse_subject)

            #if there is a next page
            #get the next url page
            #yield self.parse
        else:
            self.log('### Scrapping all subjects ###')

            subjects_url = response.xpath('//h3[@class="row vert-align-middle"]/a[1]/@href').extract()
            if subjects_url:
                for subject in subjects_url:
                    absolute_url = response.urljoin(subject)
                    yield Request(absolute_url, callback=self.parse_subject)


    def parse_subject(self, response):
        #get the subject name
        subject_name = response.xpath('//h1[@class="head-1"]/text()').extract_first()
        follow_count = response.xpath('//span[@class="cmpt-follow-count bg-blue-black radius-small padding-horz-xxsmall margin-left-xsmall"]/text()').extract_first()
        
        #get a list of course
        courses = response.xpath('//tr/td/a')

        #get the info of the course
        for course in courses:
            course_name = course.xpath('.//*[@itemprop="name"]/text()').extract_first()
            course_url = course.xpath('./@href').extract_first()
            course_abs_url = response.urljoin(course_url)
            if course_name:
                yield {
                    'subject_name': subject_name,
                    'follow_count': follow_count,
                    'course_name': course_name.replace('\n', '').replace(' ', ''),
                    'course_abs_url': course_abs_url
                }

        next_page = response.xpath('//link[@rel="next"]/@href').extract_first()
        next_abs_page = response.urljoin(next_page)
        if next_page:
            yield Request(next_abs_page, callback=self.parse_subject)

