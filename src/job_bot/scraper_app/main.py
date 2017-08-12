# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.spider_jobboom import scrappy_job
from scrapy.utils.project import get_project_settings
import settings
import logging
from scrapy.utils.log import configure_logging
from subprocess import Popen
import pipelines
import ctypes, sys

#execution of batch script to establish new VPN connection
p = Popen("check_access.bat")
stdout, stderr = p.communicate()
""""
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():

    p = Popen("check_access.bat")
    stdout, stderr = p.communicate()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)"""




#configure_logging(get_project_settings())
#process = CrawlerProcess(get_project_settings())
process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)','ITEM_PIPELINES' : {'pipelines.jobPipeline':300}})
#process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)','ITEM_PIPELINES' : {'pipelines.jobPipeline':300},'LOG_LEVEL':'ERROR'})


process.crawl(scrappy_job,job_site='jobboom')

process.start()
