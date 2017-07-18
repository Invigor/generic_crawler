import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from generic_crawler.items import ProductDetailItem
from bs4 import BeautifulSoup

class ProductDetail(CrawlSpider):
    name = 'productdetail'
    custom_settings = {
        'ITEM_PIPELINES': {'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline' : 100}
        }
      
    # allowed_domains = ['awave.com.au']
    start_urls = [
	# Open the Product URLs CSV ignoring the first line
      	l.strip() for l in open('producturls.csv').readlines()[1:]
	]

    def parse(self, response):
        # self.logger.info('Hi, this is an item page! %s', response.url)
        productdetail = ProductDetailItem()
	productdetail['url'] = response.url
        productdetail['price'] = response.xpath('//*[@class="woocommerce-Price-amount amount"]/text()').extract_first().replace(",", "")
        productdetail['name'] = response.xpath('//*[@class="summary entry-summary"]/h1/text()').extract_first()

        description_html = response.xpath('//*[@id="tab-description"]').extract()
	productdetail['description'] = BeautifulSoup(''.join(description_html),'lxml').get_text()
        productdetail['sku'] = response.xpath('//*[@class="sku"]/text()').extract_first()
        productdetail['rrp'] = ''
     	productdetail['site'] = 'awave'
	productdetail['brand'] = response.xpath('//*[@class="wb-posted_in"]/a/text()').extract_first()
	productdetail['category'] = response.xpath('//*[@class="posted_in"]/a/text()').extract()
	# print(productdetail)

        yield productdetail
