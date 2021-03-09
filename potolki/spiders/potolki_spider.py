import scrapy


class PotolkiSpiderSpider(scrapy.Spider):
    name = 'potolki_spider'
    host = 'https://www.potolki.ru'
    allowed_domains = ['www.potolki.ru']
    start_urls = ['https://www.potolki.ru/catalog/']

    def parse(self, response):
        for href in response.css('li.name a::attr(href)').getall():
            yield scrapy.Request(self.host+href, callback=self.parse_category)

    def parse_category(self, response):
        for href in response.css('div.catalog_item_wrapp a::attr(href)').getall():
            yield scrapy.Request(self.host + href, callback=self.parse_product)

    def parse_product(self, response):
        sku = None
        category_1 = response.css('#bx_breadcrumb_2 a span::text').get()
        category_1_1 = response.css('#bx_breadcrumb_3 a span::text').get()
        tage = None
        name = response.css('h1::text').get()
        price = response.css('div.cost.prices.clearfix .price::text').get().replace(' руб.', '').strip()
        valute = 'руб.'
        images = [self.host + href for href in response.css('a.fancy::attr(href)').getall()]
        images = '\n'.join(images)
        brand = response.css('.brand_picture img::attr(title)').get()
        description = response.css('.detail_text').get()