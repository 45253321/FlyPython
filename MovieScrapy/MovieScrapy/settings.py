# -*- coding: utf-8 -*-

# Scrapy settings for MovieScrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'MovieScrapy'

SPIDER_MODULES = ['MovieScrapy.spiders']
NEWSPIDER_MODULE = 'MovieScrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'MovieScrapy (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
    'MovieScrapy.pipelines.MoviePipline': 300,
}
