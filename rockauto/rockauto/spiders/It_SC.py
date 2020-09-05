import scrapy
import json
from lxml import etree as ET
from lxml import html
from ..items import Part




class ItScSpider(scrapy.Spider):
    name = 'It_SC'
    allowed_domains = ['www.rockauto.com']
    start_urls = ['https://www.rockauto.com/']

    def __init__(self) :
        data = json.load(open('F4F.json',mode='r'))
        self.start_urls.pop()
        for i in range(len(data)):
            self.start_urls.append(data[i]['url'])
        #self.start_urls.append(data[3]['url'])   


    def parse(self, response):
        Body = response.xpath("//table/tbody[contains(@id, 'listingcontainer')]")   
        
        
        d = response.url[36:]
        S = d.split(',')
        
        for Bod in Body:
            source = html.fromstring(Bod.extract())



            P = Part()

            P['CarModel'] =   ' '.join([S[0],S[1],S[2],S[3]])
            P['Prod_Cat'] =   S[5]
            P['Sub_Cat'] =    S[6].replace('+',' ')

            P['Manufacturer'] = source.xpath('//span[contains(@class,"listing-final-manufacturer")]/text()')
            
            P['price'] = source.xpath('//span[contains(@id,"dprice")]/text()')

            P['ID'] = source.xpath("//span[contains(@class, 'listing-final-partnumber')]/text()")  
            
            P['Alt_ID'] = source.xpath('//span[contains(@title,"Replaces these Alternate/ OE Part Numbers")]/text()')
            
            P['Info'] = source.xpath('//div[contains(@class,"listing-text-row")]/span/span/text()')
            
            P['Description'] = source.xpath('//span[contains(@class,"span-link-underline-remover")]/text()')

            yield P
            


    def parse_old(self, response):
        #issue : when data is missing it results in total misplacement of data following it
        Rec = response.xpath("//span[contains(@class, 'listing-final-partnumber')]/text()")
        ID = response.xpath('//span[contains(@id,"dprice")]/text()')
        Manufacturer = response.xpath('//span[contains(@class,"listing-final-manufacturer")]/text()')
        Info = response.xpath('//div[contains(@class,"listing-text-row")]/span/span/text()')
        #Desc = response.xpath('//div[contains(@class,"listing-text-row")]/span/span/text()')

        for i in range(len(ID)):
            P = Part()
            P['ID'] = Rec[i].get()
            P['price'] = ID[i].extract()
            P['Manufacturer'] = Manufacturer[i].get()
            P['Info'] = Info[i].get()
            #print(Desc[i].get())
            #input()
            yield P 
