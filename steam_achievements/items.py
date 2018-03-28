# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AchievementPercentage(scrapy.Item):
    appid = scrapy.Field()
    appname = scrapy.Field()
    name = scrapy.Field()
    percent = scrapy.Field()
