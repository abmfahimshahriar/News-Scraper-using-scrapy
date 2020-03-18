# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import pymongo package for mongoDB
import pymongo

class NewsscraperPipeline(object):
    def __init__(self):
        # creating connection with the database
        self.conn = pymongo.MongoClient("mongodb+srv://fahimshahriar:<password>@newsscraper-xwzpv.mongodb.net")
        db = self.conn['BBCnews']
        self.collection = db['news_tb']

    # storing the data of items into the mongoDB
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

