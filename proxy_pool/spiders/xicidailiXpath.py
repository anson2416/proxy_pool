# -*- coding: utf-8 -*-
import scrapy
from proxy_pool.items import ProxyPoolItem

class XicidailiXpath(scrapy.Spider):
    name = 'xicixpath'
    allowed_domains = ['xicidali.com']
    start_urls = ['http://www.xicidaili.com/']

    def parse(self, response):
        #sites = response.xpath('/body/div[@class="main"]')
        #sites = response.xpath('//*[@id="ip_list"]/tbody/tr')
        # ok sites = response.xpath("//div[@class='main']")
        sites = response.xpath("//[@id='ip_list']")
        print('===========================1s')
        print(sites)
        print('===========================1e')

        for site in sites:
            print('===========================2s')
            print(site)
            print(site.xpath('td[2]/text()').extract())
            print('===========================2e')
            # item = ProxyPoolItem()
            # item['ip'] = site.xpath('td[2]/text()').extract()
            # item['port'] = site.xpath('td[3]/text()').extract()
            # yield item