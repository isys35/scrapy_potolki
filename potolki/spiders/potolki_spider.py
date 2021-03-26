import scrapy
from potolki.items import PotolokItem


class PotolkiSpiderSpider(scrapy.Spider):
    name = 'potolki_spider'
    host = 'https://www.potolki.ru'
    allowed_domains = ['www.potolki.ru']
    start_urls = ['https://www.potolki.ru/catalog/']

    def parse(self, response):
        for href in response.css('li.name a::attr(href)').getall():
            yield scrapy.Request(self.host + href, callback=self.parse_category)

    def parse_category(self, response):
        for href in response.css('div.catalog_item_wrapp a::attr(href)').getall():
            yield scrapy.Request(self.host + href, callback=self.parse_product)

    def parse_product(self, response):
        item = PotolokItem()
        item['sku'] = None
        item['category_1'] = response.css('#bx_breadcrumb_2 a span::text').get()
        item['category_1_1'] = response.css('#bx_breadcrumb_3 a span::text').get()
        item['tage'] = None
        item['name'] = response.css('h1::text').get()
        price = response.css('div.cost.prices.clearfix .price::text').get()
        if price:
            item['price'] = price.replace(' руб.', '').strip()
        item['valute'] = 'руб.'
        images = [self.host + href for href in response.css('a.fancy::attr(href)').getall()]
        item['images'] = '\n'.join(images)
        item['brand'] = response.css('.brand_picture img::attr(title)').get()
        item['description'] = response.css('.detail_text').get()
        yield item
