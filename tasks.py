from datetime import datetime
import os

from celery import Celery

app = Celery('python-tasks')
app.conf.update(
    BROKER_URL=os.environ['REDIS_URL'],
    CELERY_RESULT_BACKEND=os.environ['REDIS_URL'],
)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(30.0, every_minute.s(), expires=10)


@app.task
def every_minute():
    print('every_minute')
    print(datetime.utcnow())
