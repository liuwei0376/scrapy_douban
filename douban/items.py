# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #序号
    serial_number = scrapy.Field()
    #电影名称
    movie_name = scrapy.Field()
    #介绍
    introduce = scrapy.Field()
    #星级
    star = scrapy.Field()
    #评价
    evaluate = scrapy.Field()
    #描述
    describle = scrapy.Field()
