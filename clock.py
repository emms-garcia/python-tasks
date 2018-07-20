from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job runs every three minutes.')


sched.start()
