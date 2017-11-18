# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from proxy_pool.items import ProxyPoolItem

class KuaiSpider(scrapy.Spider):
    name = 'cnproxy'
    allowed_domains = ['cnproxy.com']
    start_urls = ['http://cnproxy.com/proxy1.html']

    def parse(self, response):
        #typee, now_page = re.findall('com/free/(.*?)/(\d+)/', response.url)[0]
        iplist = response.xpath('//div[@id="proxylisttb"]/table/tr')
        #iplist = response.xpath('//table[@id="ip_list"]/tr')
        #print(iplist)

        if iplist:
            for x in iplist:
                data = x.xpath('td/text()').extract()
                if data:
                    item = ProxyPoolItem()
                    item['ip'] = data[0]
                    #item['port'] = data[0].Spider

                    item['protocol'] = data[1]
                    item['address'] = data[3]
                    item['website'] = 'www.cnproxy.com'
                    yield item
            #next_page = int(now_page) + 1
            #next_url = 'http://www.kuaidaili.com/free/{}/{}/'.format(typee, next_page)
            #yield Request(next_url, self.parse)


