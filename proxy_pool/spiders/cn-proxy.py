# -*- coding: utf-8 -*-
# author: Bobo
import re
import scrapy
from proxy_pool.items import ProxyPoolItem


class CnProxySpider(scrapy.Spider):
    name = 'cn-proxy'
    allowed_domains = ['cn-proxy.com']
    start_urls = ['http://cn-proxy.com/']

    def parse(self, response):
        ips = re.findall('<td>(\d+\.\d+\.\d+\.\d+)</td>', response.text)
        ports = re.findall('<td>(\d+)</td>', response.text)
        address = re.findall('<td>(\w+)</td>', response.text)

        for ip, port, addr in zip(ips, ports, address):
            yield ProxyPoolItem({
                'protocol':'',
                'website': 'cn-proxy.com',
                'address' : addr,
                'score':'',
                'ip': ip,
                'port': port,
                'types':''
            })
