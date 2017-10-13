# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class A1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class titleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    pass

class filmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()  # 电影类型
    name = scrapy.Field()  # 电影名称
    href = scrapy.Field()  # 具体网页链接
    downloadURL = scrapy.Field()  # 具体下载链接
    pass
