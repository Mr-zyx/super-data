# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JavbooksItem(scrapy.Item):
    source_url = scrapy.Field()
    serial = scrapy.Field()
    title = scrapy.Field()
    cover_img = scrapy.Field()
    publish_time = scrapy.Field()
    duration = scrapy.Field()
    director = scrapy.Field()
    producer = scrapy.Field()
    publisher = scrapy.Field()
    series = scrapy.Field()
    categories = scrapy.Field()
    actress = scrapy.Field()
    galleries = scrapy.Field()
    download_infos = scrapy.Field()
