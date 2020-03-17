# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#items class for storing the data
class NewsscraperItem(scrapy.Item):
    # define the fields for your item here like:
    news_title = scrapy.Field()
    news_link = scrapy.Field()
    news_article = scrapy.Field()
    news_tag = scrapy.Field()