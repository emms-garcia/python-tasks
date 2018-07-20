from datetime import timedelta
import os

from celery import Celery


app = Celery('python-tasks')
app.conf.update(
    BROKER_URL=os.environ['REDIS_URL'],
    CELERY_RESULT_BACKEND=os.environ['REDIS_URL'],
)


@app.task
def say_hello():
    print('Hello, World!')


CELERYBEAT_SCHEDULE = {
    'every-second': {
        'task': 'example.say_hello',
        'schedule': timedelta(seconds=5),
    },
}
