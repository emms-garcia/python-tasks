from datetime import datetime
import os

from huey import RedisHuey, crontab

huey = RedisHuey('python-tasks', host=os.environ.get('REDIS_URL'))


@huey.periodic_task(crontab(minute='*/1'))
def every_minute():
    print('every_minute')
    print(datetime.utcnow())
