# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


BOT_NAME = 'jobbot_the_hut'
SPIDER_MODULES = ['scrappy_job.spiders']
NEWSPIDER_MODULE = 'scrappy_job.spiders'

ITEM_PIPELINES = {'pipeline.jobPipeline': 300}
USER_AGENT =  'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FORMATTER = 'scrapy.logformatter.LogFormatter'
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
LOG_STDOUT = False
LOG_LEVEL = 'ERROR'
LOG_FILE = 'log.txt'
LOG_SHORT_NAMES = False
"""
DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'scrapy': {
            'level': 'error',
        },
        'twisted': {
            'level': 'ERROR',
        },
    }
}"""
