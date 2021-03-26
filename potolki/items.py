import scrapy


class PotolokItem(scrapy.Item):
    sku = scrapy.Field()
    category_1 = scrapy.Field()
    category_1_1 = scrapy.Field()
    tage = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    valute = scrapy.Field()
    images = scrapy.Field()
    brand = scrapy.Field()
    description = scrapy.Field()