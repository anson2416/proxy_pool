# -*- coding: utf-8 -*-
import scrapy
import re
from proxy_pool.items import ProxyPoolItem


class CnProxySpider(scrapy.Spider):
    name = 'cnproxy'
    allowed_domains = ['cn-proxy.com']
    start_urls = ['http://cn-proxy.com/']

    def parse(self, response):
        ips = re.findall('<td>(\d+\.\d+\.\d+\.\d+)</td>', response.text)
        ports = re.findall('<td>(\d+)</td>', response.text)
        #checkTimes = re.findall('<td>(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})</td>', response.text)
        #types = re.findall('<td class="country">([^<]+)</td>', response.text)
        #protocols = re.findall('<td>(HTTPS?)</td>', response.text)
        for ip, port in zip(ips, ports):
            yield ProxyPoolItem({
                'ip': ip,
                'port': port
                #'checkTime': checkTime,
                #'types': _type
            })
