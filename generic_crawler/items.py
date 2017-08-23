# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductListItem(scrapy.Item):
    # define the fields for your item here like:
     url = scrapy.Field()
     site = scrapy.Field()
     pass

class ProductDetailItem(scrapy.Item):
    # define the fields for your item here like:
     url = scrapy.Field()
     price = scrapy.Field()
     name = scrapy.Field()
     description = scrapy.Field()
     sku = scrapy.Field()
     rrp = scrapy.Field()
     brand = scrapy.Field()
     category = scrapy.Field()
     site = scrapy.Field()
     pass
