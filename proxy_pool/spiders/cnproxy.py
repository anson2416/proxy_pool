# -*- coding: utf-8 -*-
import re
import scrapy
from proxy_pool.items import ProxyPoolItem


class CnProxySpider(scrapy.Spider):
    name = 'cnproxy'
    allowed_domains = ['cn-proxy.com']
    start_urls = ['http://cn-proxy.com/']

    def parse(self, response):
        ips = re.findall('<td>(\d+\.\d+\.\d+\.\d+)</td>', response.text)
        ports = re.findall('<td>(\d+)</td>', response.text)

        for ip, port in zip(ips, ports):
            yield ProxyPoolItem({
                'website': 'cn-proxy.com',
                'ip': ip,
                'port': port
            })
