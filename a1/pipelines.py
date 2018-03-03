# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class A1Pipeline(object):
	def process_item(self, item, spider):
		fp = open("dytt8.cvs", "a")
		fp.write(item['type'] + '\t' + item['name'] + '\t' + item['href'] + '\t')
		for downloadURL in item['downloadURL']:
			fp.write(downloadURL + '\t')
		fp.write('\n')
		fp.close()
		# return item
