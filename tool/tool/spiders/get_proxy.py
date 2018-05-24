import scrapy
class get_proxy(scrapy.Spider):
    name = 'get_proxy' 
    start_urls=['https://free-proxy-list.net/']
    def parse(self,response):
        data=''
        list_proxy = response.xpath('//*[@id="proxylisttable"]/tbody/tr')
        for i in range(0,len(list_proxy)):
            host = list_proxy[i].xpath('td[1]/text()').extract_first()
            port = list_proxy[i].xpath('td[2]/text()').extract_first()
            if list_proxy[i].xpath('td[7]/text()').extract_first() == 'yes':
                temp = 'https://'+host+':'+port
            else:
                temp = 'http://'+host+':'+port
            data =data+ temp + '\n'
        file_list  = open('list.txt', 'w')
        file_list.write(data)
        file_list.close()