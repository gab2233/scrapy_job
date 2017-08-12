# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import scrapy
import cx_Oracle
import time
import job_dictionnary
from item import job_item
import html2text
import logging
    
class scrappy_job(scrapy.Spider):
    name = "jobs"
    
    def __init__(self, job_site='', *args, **kwargs):
        super(scrappy_job, self).__init__(*args, **kwargs)
        self.start_urls = [getattr(job_dictionnary,job_site)['url_start']]
        self.site = job_site
        
    def start_requests(self):
       
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    
    def parse(self, response):
        #print(response.css(getattr(job_dictionnary,self.site)['job_tag']))
    
        for job in response.css(getattr(job_dictionnary,self.site)['job_tag']):
            h = html2text.HTML2Text()
            h.ignore_links = True
            h.ignore_image = True
            h.decode_errors = 'replace'
            
            item = job_item()
            #get data in item
            item['titre'] = h.handle(job.css(getattr(job_dictionnary,self.site)['job_title']).extract_first())
            item['site_provenance'] = ('jobboom')
            #get link to a job page
            job_page = job.css(getattr(job_dictionnary,self.site)['job_link_tag']).extract_first()
            job_page = response.urljoin(job_page)
            #get more data
            item['lien'] = (job_page) 
            item['nom_compagnie'] = h.handle(job.css(getattr(job_dictionnary,self.site)['boss_tag']).extract_first())
            item['date_dernier_poste'] = (time.strftime("%Y%m%d"))
            #cascade request to company to get data then to the annonce
            position_page = job.css('div.logo a::attr(href)').extract_first()
            position_page = response.urljoin(position_page)
            yield scrapy.Request(position_page,callback =self.parse_position,meta={'job_page': job_page, 'item': item})
            
            
            
            
            
            
        #next page on the site    
        next_page = response.css(getattr(job_dictionnary,self.site)['next_page_tag']).extract_first()
        if next_page is not None:
           yield response.follow(next_page, callback=self.parse)
    
    def parse2(self, response):
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_image = True
        h.decode_errors = 'replace'
        item = response.meta['item']
        item['texte'] = h.handle( response.css('div#job-description').extract_first())
        yield item
        #print(response.css('div#job-description').extract_first().encode('utf-8','ignore'))
        
        
    def parse_position(self, response):
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_image = True
        h.decode_errors = 'replace'
        item = response.meta['item']
        job_page = response.meta['job_page']
        item['position'] = h.handle(response.css('div.detailsEmployeur').extract_first())
        yield scrapy.Request(job_page, callback =self.parse2,meta={'item': item})
        #print(h.handle(response.css('div.detailsEmployeur').extract_first()))
        