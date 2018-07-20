from datetime import timedelta
import os

from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger('python-tasks')
app = Celery('python-tasks')
app.conf.update(
    BROKER_URL=os.environ['REDIS_URL'],
    CELERY_RESULT_BACKEND=os.environ['REDIS_URL'],
)


@app.task
def say_hello():
    logger.info('Hello, World!')


CELERYBEAT_SCHEDULE = {
    'every-second': {
        'task': 'example.say_hello',
        'schedule': timedelta(seconds=5),
    },
}
