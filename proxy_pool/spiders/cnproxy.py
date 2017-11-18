# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from proxy_pool.items import ProxyPoolItem

class KuaiSpider(scrapy.Spider):
    name = 'cnproxy'
    allowed_domains = ['cnproxy.com']

    def start_requests(self):
        for i in range(1, 10):
            yield scrapy.Request("http://cnproxy.com/proxy{0}.html".format(i),
                                    callback=self.parse)

    def parse(self, response):
        iplist = response.xpath('//div[@id="proxylisttb"]/table/tr')

        if iplist:
            for x in iplist:
                data = x.xpath('td/text()').extract()
                if data:
                    item = ProxyPoolItem()
                    item['ip'] = data[0]
                    #item['port'] = data[0] //不会extract
                    item['protocol'] = data[1]
                    item['address'] = data[3]
                    item['website'] = 'www.cnproxy.com'
                    yield item


