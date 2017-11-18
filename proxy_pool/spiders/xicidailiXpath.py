# -*- coding: utf-8 -*-
import scrapy
from proxy_pool.items import ProxyPoolItem

class XiciXpathSpider(scrapy.Spider):
    name = 'xicixpath'
    allowed_domains = ['xicidali.com']
    start_urls = ['http://www.xicidaili.com/']

    def parse(self, response):
        #typee, now_page = re.findall('com/free/(.*?)/(\d+)/', response.url)[0]
        iplist = response.xpath('//table[@id="ip_list"]/tr')
        #iplist = response.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
        print (iplist)
        print('********************************')

        if iplist:
            for x in iplist:
                data = x.xpath('td/text()').extract()
                if data:
                    item = ProxyPoolItem()
                    item['ip'] = data[0]
                    item['port'] = data[1]
                    item['address'] = data[2]
                    item['types'] = data[3]
                    item['protocol'] = data[4]
                    item['website'] = 'www.xicidali.com'
                    yield item
            #next_page = int(now_page) + 1
            #next_url = 'http://www.kuaidaili.com/free/{}/{}/'.format(typee, next_page)
            #yield Request(next_url, self.parse)