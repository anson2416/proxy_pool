# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from proxy_pool.items import ProxyPoolItem

class KuaiSpider(scrapy.Spider):
    name = 'cnproxy'
    allowed_domains = ['cnproxy.com']

    def start_requests(self):
        for i in range(1, 8):
            yield scrapy.Request("http://cnproxy.com/proxy{0}.html".format(i),
                                    callback=self.parse)

    def parse(self, response):
        iplist = response.xpath('//div[@id="proxylisttb"]/table/tr')
        ports_re  = re.compile('write\(":"(.*)\)')
        raw_ports = ports_re.findall(response.text)
        port_map = {'v':'3','m':'4','a':'2','l':'9','q':'0','b':'5','i':'7','w':'6','r':'8','c':'1','+':''}
      
        ports = []
        for port in raw_ports:
            tmp = port
            for key  in port_map:
                tmp = tmp.replace(key, port_map[key])
            ports.append(tmp)

        idx_ports=0
        if iplist:
            for x in iplist:
                data = x.xpath('td/text()').extract()
                if data:
                    item = ProxyPoolItem()
                    item['ip'] = data[0]
                    item['protocol'] = data[1]
                    item['address'] = data[3]
                    item['website'] = 'www.cnproxy.com'
                    item['port'] = ports[idx_ports]
                    idx_ports=idx_ports+1
                    yield item