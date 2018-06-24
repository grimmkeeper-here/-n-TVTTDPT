#!/usr/bin/python
# -*- coding: utf-8 -*- 
import re
import urllib
import scrapy
import datetime
import isbn
import aes
import os
import json
from datetime import datetime
from datetime import date
from scrapy.http.request import Request
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.http import HtmlResponse
from scrapy.selector import HtmlXPathSelector

class tool(scrapy.Spider):
    
    #Spider name
    name="tool"
    path = './source/'
    #Make Request
    #Origin
    def request(self, url, callback,folder_name):
        request = scrapy.Request(url = url, priority = 2, dont_filter=True, callback= callback)
        request.meta['folder']=folder_name
        return request
    
    #Start tool make Request for Parse
    def start_requests(self):
        #vinabook
        #vinabook_vanhoc
        vinabook_vanhoc="https://www.vinabook.com/c353/sach-van-hoc-trong-nuoc/page-"
        for i in range(1,300):
            url = vinabook_vanhoc+str(i)
            yield self.request(url,self.parse_list_vinabook,'vanhoc')
        #vinabook_kinhte
        vinabook_kinhte="https://www.vinabook.com/c348/sach-kinh-te/page-"
        for i in range(1,160):
            url = vinabook_kinhte+str(i)
            yield self.request(url,self.parse_list_vinabook,'kinhte')
        #vinabook_phattrienbanthan
        vinabook_phattrienbanthan="https://www.vinabook.com/c668/sach-phat-trien-ban-than/page-"
        for i in range(1,160):
            url = vinabook_phattrienbanthan+str(i)
            yield self.request(url,self.parse_list_vinabook,'phattrienbanthan')
        
    #Parse Vinabook
    def parse_list_vinabook(self,response):
        list_item=response.xpath('//a[@class="image-border"]/@href')
        for item in range(len(list_item)):
            item_url = list_item.extract()[item]
            request=scrapy.Request(item_url, dont_filter=True, callback = self.parse_item_vinabook)
            request.meta['folder']=response.meta['folder']
            yield request
    def parse_item_vinabook(self,response):
        folder_name=response.meta['folder']
        uri = self.path + folder_name
        url_id=None
        matches = re.finditer(r"-p(.*)\.html", response.url)    
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                url_id= match.group(1)
        while(url_id.isdigit() == False):
            matches = re.finditer(r"-p(.*)", url_id)    
            for matchNum, match in enumerate(matches):
                matchNum = matchNum + 1
                for groupNum in range(0, len(match.groups())):
                    groupNum = groupNum + 1
                    url_id= match.group(1)
        check = False
        for root, dirs, files in os.walk(uri):
            for file in files:
                file = file.replace(".json","")
                if file == url_id:
                    check = True
                    break
            if check == True:
                break
        if check == False: 
            list_description = response.xpath('//div[@class="full-description"]/p').extract()
            book_description = ''
            for description in list_description:
                temp = self.cleanHTML(description.strip())
                if temp is not '' or temp != u'Mời bạn đón đọc.' or temp != u'mời bạn đón đọc.':
                    book_description = book_description + ' '+temp
            book_name = response.xpath('//*[@itemprop="name"]/text()').extract()[0].strip()
            info=response.xpath('//*[@class="product-feature"]/ul/li')
            book_img=""
            book_ISBN=""
            book_author=""
            book_publisher=""
            for li in info:
                key=li.xpath('strong/text()').extract_first().strip()
                if key == u'Mã Sản phẩm:':
                    book_ISBN=li.xpath('text()').extract()[1].strip()
                if key == u'Tác giả:':
                    value = li.xpath('a/text()').extract_first()
                    if value is not None:
                        book_author= value.strip()
                    else:
                        book_author=li.xpath('span/text()').extract_first().strip()
                if key == u'Nhà phát hành:':
                    value = li.xpath('a/text()').extract_first()
                    if value is not None:
                        book_publisher= value.strip()
                    else:
                        book_publisher=li.xpath('span/text()').extract_first().strip()
            if(book_ISBN is not ''):
                if (book_ISBN[0]==str(2)) or (book_ISBN[0]==str(8)) or (book_ISBN[0]==str(9)):
                    if isbn.isValid(book_ISBN)==True and book_description is not '':
                        book_img=response.xpath('//img[@id="det_img_'+url_id+'"]/@src').extract_first().strip()
                        book_temp = {'name': book_name,
                                    'img': book_img,
                                    'isbn': book_ISBN,
                                    'author': book_author,
                                    'publisher': book_publisher,
                                    'description': book_description,
                                    'class':folder_name
                                    }
                        json.dump(book_temp,open(uri+'/'+url_id+'.json', "wb"))
    ####################
    def cleanHTML(self,raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext