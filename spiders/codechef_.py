# -*- coding: utf-8 -*-
import scrapy


class CodechefSpider(scrapy.Spider):
    name = "codechef_"
    allowed_domains = ["codechef.com"]
    start_urls = (
        'http://www.codechef.com/users/vicky002',
    )

    def parse(self, response):
    	filename = response.url.split("/")[-2]
    	with open(filename,'wb') as f:
    		f.write(response.body)
        pass
