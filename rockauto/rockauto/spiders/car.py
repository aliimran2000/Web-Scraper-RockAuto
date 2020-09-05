import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule



counter = 1
class CarSpider(CrawlSpider):
    name = 'car'
    allowed_domains = ['www.rockauto.com']
    start_urls = ['https://www.rockauto.com/en/catalog/ford']

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths="//td[@class='nlabel']/a",allow=('ford,2018')), 
            callback='parse_item', 
            follow=True ,
            ),
    )


    def parse_item(self, response):
            
        d = response.url[36:]
        S = d.split(',')

        if len(S) >= 7 :
            yield{
                'url': response.url
            }

        

        

    