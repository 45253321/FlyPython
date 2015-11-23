# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MoviescrapyPipeline(object):
    def process_item(self, item, spider):
        return item

class MoviePipline(object):

    def __init__(self):

        self.file = open("movie.txt","w")

    def process_item(self, item, spider):
        actor = item["actors"]
        title = item["title"]
        link = item["link"]
        playtime = item["playtime"]
        update = item['updatetime']

        line =  "actor:%s title:%s link:%s playtime:%s updatetime:%s\n" % \
            (actor.encode("utf-8"), title.encode("utf-8"),link.encode("utf-8"), playtime.encode("utf-8") , update.encode("utf-8"))
        self.file.write(line)
        return item
