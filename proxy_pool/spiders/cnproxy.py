# -*- coding: utf-8 -*-
import scrapy
import re
from proxy_pool.items import ProxyPoolItem


class XicidailiSpider(scrapy.Spider):
    name = 'cnproxy'
    allowed_domains = ['cn-proxy.com']
    start_urls = ['http://cn-proxy.com/']

    def parse(self, response):
        ips = re.findall('<td>(\d+\.\d+\.\d+\.\d+)</td>', response.text)
        ports = re.findall('<td>(\d+)</td>', response.text)
        #types = re.findall('<td class="country">([^<]+)</td>', response.text)
        #protocols = re.findall('<td>(HTTPS?)</td>', response.text)
        for ip, port in zip(ips, ports):
            yield ProxyPoolItem({
                'ip': ip,
                #'protocol': protocol,
                'port': port
                #'types': _type
            })
