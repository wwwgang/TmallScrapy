# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmallItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    item_id = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    sold = scrapy.Field()
    quantity = scrapy.Field()
    totalSoldQuantity = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    titleUnderIconList = scrapy.Field()
