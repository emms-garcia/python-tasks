from celery import Celery
from celery.utils.log import get_task_logger

app = Celery('python-tasks')
app.config_from_object('celeryconfig')
logger = get_task_logger('python-tasks')


@app.task
def every_3_minutes():
    logger.info('I run every 3 minutes!')
