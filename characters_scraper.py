# -*- coding: utf-8 -*-
import scrapy 

class BlogSpider(scrapy.Spider):
    # the robot's name
    name = 'characterspider'
    # The links
    start_urls = ["https://fr.wikipedia.org./wiki/Cat%C3%A9gorie:Personnage_d'animation"]
    
    # The fucntion that parse the links
    def parse(self, response):
        # In each link with an id 'mw-pages on a div and itself in a class'mw-content-ltr' with a div itself in a li
        for link in response.css('div#mw-pages div.mw-content-ltr li'):
            # Create a dictionnary with the context a link's div and as key the value 'character'
            yield {'character': link.css('a ::text').extract_first()}