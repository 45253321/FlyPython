#encoding=utf-8

__author__ = 'lizitai'
import scrapy
from MovieScrapy.items import  MoviesItem
from scrapy import log


class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["10.10.10.10"]
    start_urls = [
        "http://10.10.10.10/4/mvlist_tag_mv.aspx?typeID=0&areaID=15&timeID=0&sortID=0&starLevel=0",

    ]

    def parse(self, response):
        movieList = response.xpath('//div[contains(@class, "movieList")]/div[contains(@class,"movieListOne")]')
        for movie in movieList:
            item = MoviesItem()
            item['title'] = movie.xpath('h3/a/@title').extract()[0]
            item['link'] = movie.xpath('h3/a/@href').extract()[0]
            desc = movie.xpath('p/text()').extract()
            item['actors'] = desc[0]
            item['updatetime'] = desc[1]
            item['playtime'] = desc[len(desc)-1]
            yield item

            # pp = movie.xpath('/p').extract()
            # log.msg("desc:%s" % (desc), level=log.DEBUG)
