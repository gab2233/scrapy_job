# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import scrapy
from scrapy.crawler import CrawlerProcess
from job_spider import scrappy_job
from scrapy.utils.project import get_project_settings
import settings
import logging
from scrapy.utils.log import configure_logging

import pipeline

#logging.basicConfig(
#    level=logging.ERROR,
#    filename='log.txt',
#    format='%(levelname)s: %(message)s'
#    
#)

#configure_logging(get_project_settings())
process = CrawlerProcess(get_project_settings())

process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)','ITEM_PIPELINES' : {'pipeline.jobPipeline':300},'LOG_LEVEL':'ERROR'})
#'FEED_FORMAT': 'json',
#'FEED_URI': 'result.json'})

process.crawl(scrappy_job,job_site='jobboom')

process.start()
