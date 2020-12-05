# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from javbooks.utils.mongo_db_helper import MongoDBHelper
from javbooks.settings import mongo_db_name, mongo_db_collection


class JavbooksPipeline(object):
    def __init__(self):
        dbname = mongo_db_name
        sheetname = mongo_db_collection

        self.post = MongoDBHelper(sheetname, dbname)

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert_item(data)
        return item
