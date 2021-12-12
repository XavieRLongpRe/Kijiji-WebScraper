# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scrapy
from challenge1.items import Challenge1Item

class ChanllengeSpider(scrapy.Spider):
    name = 'challenge'
    start_urls = [
        
        'http://books.toscrape.com/catalogue/immunity-how-elie-metchnikoff-changed-the-course-of-modern-medicine_900/index.html',
        'http://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html',
        'http://books.toscrape.com/catalogue/dont-be-a-jerk-and-other-practical-advice-from-dogen-japans-greatest-zen-master_890/index.html',
        'http://books.toscrape.com/catalogue/security_925/index.html'
        
        
        
        ]
    
    
    def parse(self, response):
       
        item = Challenge1Item()
       
        item['title'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1/text()').get()
       
        item['price'] = response.xpath('//p[@class ="price_color"]/text()').get()
       
        item['category'] = response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get()
       
        item['stock'] = response.xpath("normalize-space(//p[@class='instock availability']/i/following::node()[1])").get()
       
        return item
        
    