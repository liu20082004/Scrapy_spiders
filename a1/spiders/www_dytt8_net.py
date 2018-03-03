# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from a1.items import filmItem
from scrapy import Request
import re

class dytt8Spider(Spider):
	name = 'dytt8'
	start_urls = ['http://www.dytt8.net']
	film_items = []  # 列表,保存film_item
	# header = { 'Accept':'image/webp,image/*,*/*;q=0.8', 'Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6','Connection':'keep-alive' }
	# USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'

	def __init__(self):
		"""初始化函数,暂时用来创建文档"""
		fp = open("dytt8.cvs", "w")
		fp.close()

	def parse(self, response):
		filmTypes = response.xpath('//div[@class="bd3r"]//div[@class="co_area2"]')  # 返回的是selectorList的对象
		for filmType in filmTypes:
			filmTypeTitles = filmType.xpath('.//strong/text()').extract()  # 返回一个list(就是系统自带的那个) 里面是一些你提取的内容
			for eachTitle in filmTypeTitles:
				filmTypeString = eachTitle.encode('utf8')
				films = filmType.xpath('.//tr')
				for film in films:
					film_item = filmItem()
					film_item['type'] = filmTypeString
					try:  # 网站插入其他内容时,防止出错
						film_item['name'] = film.xpath('.//a/text()').extract()[1].encode('utf8')
						film_item['href'] = film.xpath('.//a/@href').extract()[1].encode('utf8')
					except IndexError, e:
						continue
					self.film_items.append(film_item)
					print film_item['name']
					print film_item['href']
					if film_item['href']:
						filmPageURL = 'http://www.dytt8.net' + film_item['href']
						yield Request(filmPageURL, callback=self.parse_download)

	def parse_download(self, response):
		pattern = re.compile('="\s*(?:ftp|http)://.*\.(?:mkv|rmvb|mp4|exe|rar)\s*"', re.I)  # 正则表达式  分组()  (?:)非分组捕获,用于使用|
		ftpURLs = re.findall(pattern, response.text)
		downloadURL = []
		for ftpURL in ftpURLs:
			print ftpURL
			downloadURL.append(ftpURL[2:-1].encode('utf8'))

		# 下面这段存在风险,当不存在film_item时,会出错的
		film_item = [ a for a in self.film_items if a['href'] in response._url ]  # 这里的逻辑是根据response._url与self.film_items中的href比较,如果存在,则证明该下载链接为该item的内容
		if film_item:  # 增加一个判断吧
			film_item[0]['downloadURL'] = downloadURL
			yield film_item[0]

