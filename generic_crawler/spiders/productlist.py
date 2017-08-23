import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from generic_crawler.items import ProductListItem

class ProductList(CrawlSpider):
    name = 'productlist'
    custom_settings = {
    	'ITEM_PIPELINES': {'scrapy_dynamodb.DynamoDbPipeline': 1}
	}

    start_urls = [
      	'https://www.awave.com.au/product-category/outboard/',
	'https://www.awave.com.au/product-category/',
        'https://www.awave.com.au/product-category/monitoring/',
	'https://www.awave.com.au/product-category/consoles/',
	'https://www.awave.com.au/product-category/instruments/',
	'https://www.awave.com.au/product-category/computer-music/',
	'https://www.awave.com.au/product-category/accessories/'
	]


    def parse(self, response):
        # self.logger.info('Hi, this is an item page! %s', response.url)
        product = ProductListItem()

        # product['url'] = response.url
	# prices = response.xpath('//*[@class="woocommerce-Price-currencySymbol"]/following-sibling::text()').extract()
	# names = response.xpath('//*[@class="woocommerce-loop-product__title"]/text()').extract()
	producturls = response.css('.woocommerce-LoopProduct-link::attr(href)').extract() 

	# print(prices)
	# print(names)
	# print(producturls)

	# print('Products on this page: %s',len(names))

	for i in xrange(0,len(producturls)):
	   # if len(prices) > i:
           #    product['price'] = prices[i]
	   # else:
	   #     product['price'] = '0.00'
           # product['name'] = names[i]
           # if len(prices) > i:
           product['url'] = producturls[i]
	   product['site'] = 'awave.com.au'
	   #else:
	   #    product['producturl'] = ''
	   # self.logger.info('Processing:! %s', names[i])
           yield product

	next_page = response.css('.next::attr(href)').extract_first()
        if next_page is not None:
           next_page = response.urljoin(next_page)
           yield scrapy.Request(next_page, callback=self.parse)
