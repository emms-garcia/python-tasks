from celery import Celery
from celery.utils.log import get_task_logger

from scrappers.amazon import AmazonMXScrapper

app = Celery('python-tasks')
app.config_from_object('celeryconfig')
logger = get_task_logger('python-tasks')


@app.task
def amazon_scrapper():
    logger.info('Scrapping data from Amazon MX')
    scrapper = AmazonMXScrapper()

    found_items = list(scrapper.find_items())
    logger.info('Found %s items that meet the spcified criteria.', len(found_items))
    for item in found_items:
        logger.info('{title} - ${price}\nLink: {link}'.format(**item))

    logger.info('Done')


@app.task
def heart_beat():
    logger.info('I\'m Alive!')
