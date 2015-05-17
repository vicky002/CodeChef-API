# -*- coding: utf-8 -*-
import scrapy


class CodeSpider(scrapy.Spider):
    name = "code"
    allowed_domains = ["codechef.com"]
    start_urls = (
        'http://www.codechef.com/',
    )

    def parse(self, response):
        pass
