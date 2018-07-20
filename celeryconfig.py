from datetime import timedelta
import os

beat_schedule = {
    'every-3-minutes': {
        'task': 'tasks.every_3_minutes',
        'schedule': timedelta(minutes=3),
    },
}
broker_url = os.environ['REDIS_URL']
result_backend = os.environ['REDIS_URL']
imports = ('tasks')
