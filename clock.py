from apscheduler.scheduler import Scheduler

sched = Scheduler()

@sched.interval_schedule(seconds=5)
def timed_job():
    print 'This job is run every five seconds.'

sched.start()

while True:
    pass