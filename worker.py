from datetime import datetime
import os

from huey import RedisHuey, crontab

huey = RedisHuey('python-tasks', host=os.environ.get('REDIS_URL'))


@huey.periodic_task(crontab(minute='*/3'))
def every_3_minutes():
    print('every_3_minutes')
    print(datetime.utcnow())
