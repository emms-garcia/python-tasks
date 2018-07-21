from datetime import timedelta
import os

beat_schedule = {
    'amazon-scrapper': {
        'task': 'tasks.amazon_scrapper',
        'schedule': timedelta(hours=1),
    },
    'heart-beat': {
        'task': 'tasks.heart_beat',
        'schedule': timedelta(minutes=1),
    },
}
broker_url = os.environ['REDIS_URL']
imports = ('tasks')
