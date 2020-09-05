# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RockautoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Part(scrapy.Item):
    CarModel = scrapy.Field()
    Prod_Cat = scrapy.Field()
    Sub_Cat = scrapy.Field()
    ID = scrapy.Field()
    Alt_ID = scrapy.Field()
    Manufacturer = scrapy.Field()
    Info = scrapy.Field()
    Description = scrapy.Field()
    price = scrapy.Field()